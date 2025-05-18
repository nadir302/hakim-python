from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        cursor_factory=RealDictCursor
    )
    return conn

# Create books table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Initialize the database when the app starts
init_db()

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(books)

# GET a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE id = %s;', (book_id,))
    book = cur.fetchone()
    cur.close()
    conn.close()
    
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        return jsonify({"error": "Bad request, title and author are required"}), 400
    
    title = request.json['title']
    author = request.json['author']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO books (title, author) VALUES (%s, %s) RETURNING *;',
        (title, author)
    )
    new_book = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(new_book), 201

# PUT to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # First check if book exists
    cur.execute('SELECT * FROM books WHERE id = %s;', (book_id,))
    book = cur.fetchone()
    
    if not book:
        cur.close()
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    
    if not request.json:
        cur.close()
        conn.close()
        return jsonify({"error": "Bad request"}), 400
    
    title = request.json.get('title', book['title'])
    author = request.json.get('author', book['author'])
    
    cur.execute(
        'UPDATE books SET title = %s, author = %s WHERE id = %s RETURNING *;',
        (title, author, book_id)
    )
    updated_book = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(updated_book)

# DELETE a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # First check if book exists
    cur.execute('SELECT * FROM books WHERE id = %s;', (book_id,))
    book = cur.fetchone()
    
    if not book:
        cur.close()
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    
    cur.execute('DELETE FROM books WHERE id = %s;', (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"result": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
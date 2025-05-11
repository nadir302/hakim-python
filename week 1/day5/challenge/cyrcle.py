import turtle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def draw(self, color="black"):
        """Draw the circle using turtle graphics"""
        pos = turtle.pos()
        turtle.penup()
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.pendown()
        turtle.color(color)
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(pos)
        turtle.setheading(0)

def draw_circles(circles):
    turtle.speed(0)
    turtle.hideturtle()
    colors = ["red", "blue", "green", "purple", "orange", "brown", "pink", "yellow"]

    for i, (circle, color) in enumerate(zip(circles, colors * 3)):
        if i % 3 == 0:
            turtle.clear()
            turtle.reset()
            turtle.speed(0)
            turtle.hideturtle()

        circle.draw(color)
        turtle.forward(circle.radius * 2 + 20)

        if (i + 1) % 3 == 0:
            input("Press Enter to see next set...")

    turtle.done()

if __name__ == "__main__":
    circles = [Circle(radius=50), Circle(radius=30), Circle(radius=80), 
               Circle(radius=20), Circle(radius=60), Circle(radius=40)]

    circles.sort()
    print(circles)

    draw_circles(circles)

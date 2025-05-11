def sort_words(input_str):
     
    words = sorted([word.strip() for word in input_str.split(',')])
    return ','.join(words)

 
input_str = "without,hello,bag,world"
result = sort_words(input_str)
print(f"Input: {input_str}")
print(f"Output: {result}")
 




def longest_word(sentence):
     
    words = sentence.split()
    
    if not words:
        return None
    
     
    return max(words, key=len)

 
print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))    
print(longest_word("Forgetfulness is by all means powerless!"))   
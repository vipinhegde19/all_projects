def word_builder(letters, positions):
    
    result = ""
    
    for pos in positions:
        
        result += letters[pos]
    
    return result
_string=input("Enter the string: ")
_int=input("Enter the positions: ")
print(word_builder(_string,_int))

# # Test cases
# print(word_builder(["g", "e", "o"], [1, 0, 2]))  # Output: "ego"
# print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))  # Output: "test"
# print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]))  # Output: "edabit"
 
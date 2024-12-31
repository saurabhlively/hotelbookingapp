def find_biggest_word(word_list):
    if not word_list:  # Check if the list is empty
        return None
    # Find the word with the maximum length
    biggest_word = max(word_list, key=len)
    print(biggest_word)
    return biggest_word


words = ["python", "elephant", "sky", "unbelievable", "star"]
biggest_word = find_biggest_word(words)
if biggest_word:
    print(f"The biggest word is: {biggest_word}")
else:
    print("The list is empty.")
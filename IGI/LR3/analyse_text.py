from decorator import decorator_it

@decorator_it
def lowercase_count(text: str):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    lower_count = 0
    for char in text:
        if char.islower():
            lower_count += 1

    return lower_count

def num_count(text: str):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    num_count = 0
    words = text.split()
    for word in words:
        if word.isnumeric():
            num_count += 1 
    return num_count



def is_consonant(char):
    vowels = "aeiouyAEIOUY"
    return char.isalpha() and char not in vowels

def starts_with_consonants_count(text: str):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    count = 0
    words = text.split()

    for word in words:
        if is_consonant(word[0]):
            count += 1
    
    return count

def has_double_letters(word: str):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False
        

def get_words_with_double_letters(text: str):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = text.split()
    words_with_double_letters = []

    count = 0
    indices = []
    for word in words:
        if has_double_letters(word):
            words_with_double_letters.append(word)
            index = count
            indices.append(index)
        count += 1
    
    result = zip(words_with_double_letters, indices)

    return list(result)

def get_words_in_alphorder(text: str):
    if not isinstance(text, str):
        raise TypeError("Input must be a string") 
    
    words = [word.lower() for word in text.split()]
    words.sort()
    
    return words
            





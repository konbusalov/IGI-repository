from analyse_text import starts_with_consonants_count, get_words_with_double_letters, get_words_in_alphorder

def task4():
    text = '''
            So she was considering in her own mind, as well as she could, for the hot day made her feel
            very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by
            her.
            '''
    
    words_starting_with_consonant = starts_with_consonants_count(text)
    words_with_double_letters = get_words_with_double_letters(text)
    words_in_alphorder = get_words_in_alphorder(text)

    print('-'*100)
    print(f"Words starting with consonant: {words_starting_with_consonant}")
    print(f"Words with double letters: {words_with_double_letters}")
    print(f"Words in alpabetical order: {words_in_alphorder}")
    print('-'*100)





    
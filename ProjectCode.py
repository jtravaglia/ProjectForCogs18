import re

import re

def is_vowel(char):
    return char.lower() in 'aeiou'

def piglatin_encode(word):
    if any(char.isalpha() for char in word):
        capitalization = word[0].isupper()
        first_vowel_index = next((i for i, char in enumerate(word) if is_vowel(char)), None)

        if first_vowel_index is not None:
            if capitalization:
                return word[first_vowel_index].upper() + word[first_vowel_index + 1:] + word[:first_vowel_index].lower() + 'ay'
            else:
                return word[first_vowel_index:] + word[:first_vowel_index] + 'ay'
        else:
            return word + 'ay'
    return word

def piglatin_decode(word):
    if word.isalpha() and word.endswith('ay'):
        capitalization = word[0].isupper()

        if is_vowel(word[-4]):
            decoded_word = word[:-2]
        else:
            decoded_word = word[-3] + word[:-3]

        return decoded_word.capitalize() if capitalization else decoded_word.lower()
    return word

def piglatin_decode_sentence(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    decoded_words = [piglatin_decode(word) for word in words]
    return ' '.join(decoded_words)

def process_text(text, func):
    words = re.findall(r'\b\w+\b', text)
    result = [func(word) for word in words]
    return ' '.join(result)


def main():
    print("Welcome to Julia's Pig Latin Encryption program!")
    
    while True:
        choice = input("Do you want to encode  from Pig Latin? (Type 'encode'): ").lower()
            
        if choice not in ['encode']:
            print("Invalid choice, silly. Please enter 'encode'.")
            continue
        
        user_input = input(f"Enter the text to {choice} (including punctuation): ")
        
        if choice == 'encode':
            result = process_text(user_input, piglatin_encode)
            print(f"\nEncoded Pig Latin: {result}\n")
            
        another = input("Shall we try another sentence? (yes/no): ").lower()
        if another == 'no':
            print("Okay, it was nice chatting with you!")
            break
    
if __name__ == "__main__":
    main()
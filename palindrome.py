'''
Created Date: Sunday August 1st 2021 12:45:35 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday August 1st 2021 1:18:46 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''

def is_palindrome(word: str) -> bool:
    word_normalizaed = word.replace(' ', '').strip().lower()
    reversed_word = word_normalizaed[::-1]
    return word_normalizaed == reversed_word

def print_menu() -> None:
    print("""
    Check if a word is palindrome
        - Type "x" if you want to close the program

        
    """)
def main() -> None:
    print_menu()
    word: str = input("Type the word you want to check: ")
    while word != "x":        
        if(is_palindrome(word)):
            print("YEAHHH!, it is a palindrome")
        else:
            print('NOPE!, it is not a palindrome')
            
        print_menu()
        word = input("Type the word you want to check: ")

if __name__ == '__main__':
    main()
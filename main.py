def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print_report(text, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_letters(text):
    text = text.lower()
    letters = {}
    for letter in text:
        if letter.isalpha() == False:
            continue
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def myFunc(e):
    return e

def print_report(text, num_words):
    letters = get_book_letters(text).items()
    sorted_letters = sorted(letters, key=lambda letter:letter[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n")
    for key, value in sorted_letters:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()
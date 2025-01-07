
def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    characters = character_count(text)
    num_words = count_words(text)
    print(f"--- Report of {book_path} ---")
    print(f"There are {num_words} words in the text.")
    for c in characters:
        if c.isalpha():
            print(f"The characater {c} appears {characters[c]} times.")
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def character_count(text):
    repository={}
    for i in range(len(text)):
        lowered = text[i].lower()
        if lowered in repository:
            repository[lowered] += 1
        else:
            repository[lowered] = 1
    return repository

main()
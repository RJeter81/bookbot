def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = character_count(text)
    # print(f"{num_words} words found in the document.")
    # print(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    string_split = list(text.lower())
    for char in string_split:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = character_count(text)
    sorted_report = book_report(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    print()

    for item in sorted_report:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
        else:
            continue
    
    print()
    print("--- End Report ---")

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

def sort_on(dict):
    return dict["num"]

def book_report(dict):
    sorted_list = []
    for i in dict:
        sorted_list.append({"char": i, "num": dict[i]})        

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
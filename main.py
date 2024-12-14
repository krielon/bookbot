def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in document")
    
    character_counts = count_characters(text)

    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
     
    for character, count in sorted_characters:
        print(f"The '{character}' character was found {count} times")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(text):
    text = text.lower()
    character_counts = {}
    for char in text:
        if char.isalpha():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

main()
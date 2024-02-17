def main():
    file_path = "books/frankenstein.txt"
    text = get_file_text(file_path)
    words_count = count_words(text)
    chars_count = count_chars(text)
    print_chars_count_report(file_path, words_count, chars_count)


def get_file_text(file_path):
    with open(file_path) as f:
        text = f.read()
        f.close() 
        return text

def count_words(text):
    if type(text) != str:
        raise TypeError("Text must be string")
    return len(text.split())


def count_chars(full_text):
    if type(full_text) != str:
        raise TypeError("full_text must be string")
  
    full_text_lower = full_text.lower()
    chars = {}

    for letter in full_text_lower:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def print_chars_count_report(file_path, words_count, chars_count, ):
    if type(chars_count) != dict:
        TypeError("letters_count should be a dictionary")
    
    sorted_list = []

    def sort_on(dict):
        return dict["count"]

    for char in chars_count:
        char_dict = { "char": char, "count": chars_count[char] }
        sorted_list.append(char_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file_path} ---")
    print(f"{words_count} was found in the document")
    for d in sorted_list: 
        if not d["char"].isalpha(): continue
        print(f"The '{d["char"]}' character was found {d["count"]} times")
    print(f"--- End report ---")


try:
    main()
except TypeError as e:
    print("Invalid Argument:")
    print(e)
except Exception as e:
    print("Unexpected error happened:")
    print(e)
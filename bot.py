import sys
import os
from print import Print

class Bot:
    def __init__(self, options):
        self.print = Print()
        self.options = options

    def __get_file_path(self):
        # sys.argv[0] is the name of this file  
        # running this script 'python main.py some_text_file.txt
            # result in ['main.py', 'some_text_file.txt']
        books_files = os.listdir("books")

        if len(books_files) == 0:
            raise Exception("There is no files in Books directory")

        if self.options["--target-file"]:
            file_from_arg = self.options.file
            if file_from_arg not in books_files:
                raise Exception(f"cannot find '{file_from_arg}' file")
            return f"books/{file_from_arg}"

        print(f"\nWarning: File path is missing, we'll read first file in books -> '{books_files[0]}'\n\n")
        self.print.warning(str(f"\nWarning: File path is missing, we'll read first file in books -> '{books_files[0]}'\n\n"))
        return f"books/{books_files[0]}"

    def __get_file_text(self, file_path):
        with open(file_path) as f:
            text = f.read()
            f.close() 
            return text

    def __count_words(self, text):
        if type(text) != str:
            raise TypeError("Text must be string")
        return len(text.split())


    def __count_chars(self, full_text):
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

    def __count_lines(self, text):
        lines = text.split("\n")
        return len(lines)

    def __print_chars_count_report(self, file_path, words_count, chars_count, lines_count):
        if type(chars_count) != dict:
            TypeError("letters_count should be a dictionary")
        
        sorted_list = []

        def sort_on(dict):
            return dict["count"]

        for char in chars_count:
            char_dict = { "char": char, "count": chars_count[char] }
            sorted_list.append(char_dict)
        
        sorted_list.sort(reverse=True, key=sort_on)

        self.print.bold(f"--- Begin report of {file_path} ---")
        self.print.normal()
        
        if self.options["--words-count"] or self.options["--lines-count"]:
            self.print.info("File Info: ")
        if self.options["--words-count"]:
            self.print.normal(f"- {words_count} was found in the document")
        if self.options["--lines-count"]:
            self.print.normal(f"- The document contains {lines_count} lines")
        self.print.normal()
        
        if self.options["--characters-count"]:
            for d in sorted_list: 
                if not d["char"].isalpha(): continue    
                self.print.fancy(f"The '{d["char"]}' character was found {d["count"]} times")

        self.print.info(f"--- End report ---")

    def analyze(self):
        file_path = self.__get_file_path()
        text = self.__get_file_text(file_path)
        words_count = self.__count_words(text)
        chars_count = self.__count_chars(text)
        lines_count = self.__count_lines(text)
        self.__print_chars_count_report(file_path, words_count, chars_count, lines_count)
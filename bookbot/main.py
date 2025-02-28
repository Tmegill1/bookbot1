from stats import get_num_words
from stats import count_char

#getting the path to the book text file
def get_book_text(filepath):
    try:
        with open(filepath, encoding ='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found. Please make sure it exists.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {e}")
        return None
    

    
def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(text)
    char_count = count_char(text)
    if text:
        #print(text)
        print(f"{num_words}, words found in the document")
        print(char_count)

if __name__ == "__main__":
    main()
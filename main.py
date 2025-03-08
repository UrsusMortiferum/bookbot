from stats import get_num_words, get_char_count

def get_boot_text(file_path):
    with open(file_path) as file:
        content = file.read()
        return content

def main():
    file_path = "./books/frankenstein.txt"
    # print(get_boot_text(file_path))
    content = get_boot_text(file_path)
    num_words = get_num_words(content)
    print(f"{num_words} words found in the document")
    print(get_char_count(content))

main()

from stats import get_num_words, get_char_count, sort_char_count

def get_boot_text(file_path):
    with open(file_path) as file:
        content = file.read()
        return content

def main():
    file_path = "./books/frankenstein.txt"
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path.removeprefix("./")}...""")

    content = get_boot_text(file_path)
    num_words = get_num_words(content)
    print(f"""----------- Word Count ----------
Found {num_words} total words""")

    char_count = get_char_count(content)
    sorted = sort_char_count(char_count)
    print("--------- Character Count -------")
    for i in sorted:
        char = i["char"]
        if char.isalpha():
            print(f"{char}: {i["count"]}")
    print("============= END ===============")

main()

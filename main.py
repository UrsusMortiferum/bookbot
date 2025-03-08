def get_boot_text(file_path):
    with open(file_path) as file:
        content = file.read()
        return content

def get_num_words(content):
    words = content.split()
    return len(words)

def main():
    file_path = "./books/frankenstein.txt"
    # print(get_boot_text(file_path))
    content = get_boot_text(file_path)
    num_words = get_num_words(content)
    print(f"{num_words} words found in the document")

main()

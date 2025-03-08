def get_boot_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    print(get_boot_text(file_path))

main()

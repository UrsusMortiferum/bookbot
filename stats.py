def get_num_words(content):
    words = content.split()
    return len(words)

def get_char_count(content):
    char_count = {}
    for i in content.lower():
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    return char_count

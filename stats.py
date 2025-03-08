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

def sort_on(dict):
    return dict["count"]

def sort_char_count(char_count):
    sorted = [] 
    for k, v in char_count.items():
        temp = {}
        temp["char"] = k
        temp["count"] = v
        sorted.append(temp)
    sorted.sort(reverse=True, key=sort_on)
    return sorted

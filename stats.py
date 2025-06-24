def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_chars(text):
    text = text.lower()
    num_chars = {}
    for char in text:
        if num_chars.get(char):
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def chars_dict_with_keys(text):
    chars_dict = get_num_chars(text)
    ret_val = []
    for thing in chars_dict:
        ret_val.append({ "char": thing, "num": chars_dict[thing] })
    return ret_val

def sort_on(items):
    return items["num"]

def get_sorted_chars(text):
    unsorted_chars_dict = chars_dict_with_keys(text)
    unsorted_chars_dict.sort(reverse=True, key=sort_on)
    return unsorted_chars_dict
    
def word_counter(input_text):
    words = input_text.split()
    word_count = len(words)
    return word_count

def character_counter(input_text):
    char_counts = {}
    for char in input_text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted_char_list(char_counts):
    chars_list = []
    
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    
    def get_count(dict_item):
        return dict_item["count"]
    
    chars_list.sort(reverse=True, key=get_count)
    

    return chars_list
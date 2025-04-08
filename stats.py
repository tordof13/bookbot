def get_num_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    char_dict = {}
    for character in text:
        character = character.lower()
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict

def create_report(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_dict = {'char': char, 'count': count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    

    char_list.sort(reverse=True, key=sort_on)

    return char_list
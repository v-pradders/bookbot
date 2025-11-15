def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_character_count(file_contents):
    character_counter ={}
    for char in file_contents:
        char_lower = char.lower()
        if char_lower in character_counter:
            character_counter[char_lower] += 1
        else:
            character_counter[char_lower] = 1

    return character_counter

    
def get_report(character_counter):

    character_count_list = []
    for key, value in character_counter.items():
        if key.isalpha():
            character_count_list.append({"char":key, "num": value})

    character_count_list.sort(reverse=True, key= lambda x: x['num'])

    return character_count_list




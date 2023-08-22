def is_anagram(first_string: str, second_string: str) -> (str, str, bool):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return (
            string_ordner(first_string.lower()),
            string_ordner(second_string.lower()), False
        )
    first_string_char_counter = char_counter(first_string, second_string)
    second_string_char_counter = char_counter(second_string, first_string)
    if first_string_char_counter == second_string_char_counter:
        return (
            string_ordner(first_string.lower()),
            string_ordner(second_string.lower()), True
        )
    else:
        return (
            string_ordner(first_string.lower()),
            string_ordner(second_string.lower()), False
        )
    # raise NotImplementedError


def char_counter(first_string, second_string):
    char_counter = {}
    for index in range(len(first_string)):
        letter_first_string = first_string[index].lower()
        if letter_first_string in second_string.lower():
            if letter_first_string in char_counter:
                char_counter[letter_first_string] += 1
            else:
                char_counter[letter_first_string] = 1
        else:
            char_counter[letter_first_string] = 0
    return char_counter


def string_ordner(string: str) -> str:
    new_string = list(string)
    list_length = len(new_string)
    for index in range(list_length - 1):
        min_letter_index = index
        for search_index in range(index + 1, list_length):
            if new_string[search_index] < new_string[min_letter_index]:
                min_letter_index = search_index      
        curr_char = new_string[index]
        new_string[index] = new_string[min_letter_index]
        new_string[min_letter_index] = curr_char
    return "".join(new_string)

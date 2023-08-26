def is_anagram(first_string: str, second_string: str) -> (str, str, bool):
    ordered_first_string = list(first_string.lower())
    string_merge_sort(
        ordered_first_string, 0, len(ordered_first_string)
    )
    ordered_second_string = list(second_string.lower())
    string_merge_sort(
        ordered_second_string, 0, len(ordered_second_string)
    )
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return (
            "".join(ordered_first_string),
            "".join(ordered_second_string),
            False,
        )
    first_string_char_counter = char_counter(first_string, second_string)
    second_string_cahr_counter = char_counter(second_string, first_string)
    if first_string_char_counter == second_string_cahr_counter:
        return (
            "".join(ordered_first_string),
            "".join(ordered_second_string),
            True,
        )
    else:
        return (
            "".join(ordered_first_string),
            "".join(ordered_second_string),
            False,
        )


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


def string_merge_sort(string: [str], start=0, end=None) -> [str]:
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        string_merge_sort(string, start, mid)
        string_merge_sort(string, mid, end)
        merge_string(string, start, mid, end)


def merge_string(string: [str], start: int, mid: int, end: int):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index += 1
        else:
            string[general_index] = right[right_index]
            right_index += 1

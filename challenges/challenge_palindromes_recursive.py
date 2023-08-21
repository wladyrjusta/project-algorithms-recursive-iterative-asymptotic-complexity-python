def is_palindrome_recursive(word, low_index, high_index):
    if word == "" or word[low_index] != word[high_index]:
        return False
    if high_index == 0:
        return True
    while low_index < len(word) - 1:
        if word[low_index] == word[high_index]:
            print(low_index, (len(word) - 1))
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True

    # raise NotImplementedError

def is_palindrome_iterative(word):
    if word == "" or word is None:
        return False
    word = word.lower()
    if word[::-1] == word:
        return True
    else:
        return False
    # raise NotImplementedError

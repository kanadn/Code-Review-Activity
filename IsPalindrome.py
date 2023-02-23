def is_palindrome(word):
    reverse_word = ""
    for i in range(len(word), 0, -1):
        reverse_word += word[i]
    return word == reverse_word

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

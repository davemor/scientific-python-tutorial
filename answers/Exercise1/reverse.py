def reverse(word):
    letters = list(word)
    letters.reverse()
    return "".join(letters)

in_word = input("Enter word: ")
print(reverse(in_word))
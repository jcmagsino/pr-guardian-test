def alphabet_sum(text):
    total = 0
    for char in text.lower():
        if char.isalpha():
            total += ord(char) - ord('a') + 1

    print(total)
    return total
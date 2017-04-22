def number_needed(a, b):
    # make a dictionary with the char counts for each string
    count = 0
    a_letters = {}
    b_letters = {}
    for char in a:
        if char in a_letters:
            a_letters[char] += 1
        else:
            a_letters[char] = 1
    for char in b:
        if char in b_letters:
            b_letters[char] += 1
        else:
            b_letters[char] = 1
    for char in a_letters:
        if char not in b:
            count += a_letters[char]
            a_letters[char] = None
        else:
            a_char_count = a_letters[char]
            b_char_count = b_letters[char]
            char_count_diff = abs(a_char_count - b_char_count)
            if a_char_count > b_char_count:
                a_letters[char] -= char_count_diff
                count += char_count_diff
            elif a_char_count < b_char_count:
                b_letters[char] -= char_count_diff
                count += char_count_diff
    for char in b_letters:
        if char not in a:
            count += b_letters[char]
            b_letters[char] = None

    return count

# print number_needed("happy", "chaps")

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

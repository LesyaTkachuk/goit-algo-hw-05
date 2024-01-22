def build_shift_table(pattern):
    # boyer_moore shift table creation
    table = {}
    length = len(pattern)

    # for each symbol in pattern string set the shift equals to the pattern string length
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    # if there is no such symbol in the table, the shift will be equal the pattern string length
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    # shift table creation for the pattern string
    shift_table = build_shift_table(pattern)
    i = 0

    # move through the text and compare with the pattern
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # starting from the pattern end

        # compare symbols from the pattern end to the start
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # move to the pattern start

        # if all pattern coincides return its index in the text
        if j < 0:
            return i  # pattern was found

        # shifting the index based on the shift table to jump over uncoinciding parts
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # if the pattern was not found
    return -1

if __name__=="__main__":
    text = "Being a developer is not easy"
    pattern = "developer"

    position = boyer_moore_search(text, pattern) 
    print(position)

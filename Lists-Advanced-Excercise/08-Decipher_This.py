# 08. Decipher This!
def replace_character_code(word: str):
    chr_code_str = ''
    new_word = []

    for ch in word:
        if ch.isnumeric():
            chr_code_str += ch
        else:
            new_word.append(ch)

    ch_at_beginning = chr(int(chr_code_str))

    new_word.insert(0, ch_at_beginning)

    return new_word


def decipher_word(word: str):
    new_word = replace_character_code(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return "".join(new_word)


words = input().split()

deciphered_words = [decipher_word(word) for word in words]

print(' '.join(deciphered_words))
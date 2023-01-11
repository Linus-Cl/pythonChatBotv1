
PUNCTUATION_CHARS = ['.', '?', '!']


def split_sentence(sentence):
    words = sentence.lower().split()
    for i in range(len(words)):
        last_char = words[i][-1]
        # cut punctuation
        if last_char in PUNCTUATION_CHARS:
            words[i] = words[i][:-1]

    return words

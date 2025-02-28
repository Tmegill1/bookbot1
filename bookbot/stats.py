def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_char(text):
    word_list_lower = text.lower()
    freq = {}
    for c in set(word_list_lower):
        if c.isalpha():  # only count alphabet letters
            freq[c] = word_list_lower.count(c)
    return dict(sorted(freq.items()))
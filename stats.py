def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    counts = {}
    for i in range(0, len(text)):
        c = text[i].lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sort_by_char(dict):
    return dict["char"]

def get_sorted_counts(num_chars):
    output = []
    for c in num_chars:
        output.append({"char": c, "num": num_chars[c]})
    output.sort(key=sort_by_char)
    return output
        
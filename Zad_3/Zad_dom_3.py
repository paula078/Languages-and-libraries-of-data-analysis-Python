import re

# Zad_1
def count_words(filename, amount_most_common=None):
    with open(filename, encoding='utf-8') as infile:
        content = infile.read().lower()
        words = re.findall(r'\b\w+\b', content)

    return counter(words, amount_most_common)


def counter(words, amount_most_common=None):
    counter_dict = {}
    for item in words:
        counter_dict[item] = counter_dict.get(item, 0) + 1
    sorted_items = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    if amount_most_common is not None:
        result = sorted_items[:amount_most_common]
        for item in range(amount_most_common, len(sorted_items) - 1):
            if sorted_items[amount_most_common - 1][1] == sorted_items[item][1]:
                result.append(sorted_items[item])
    else:
        result = sorted_items
    return result

print(count_words('potop.txt', 200))

# Zad_2
def count_ngrams(filename, number_grams, amount_most_common=None):
    with open(filename, 'r', encoding='utf-8') as infile:
        content = infile.read().lower()
        words = re.findall(r'\b\w+\b', content)
        ngrams = list(zip(*[words[i:] for i in range(number_grams)]))

    return counter(ngrams, amount_most_common)

print(count_ngrams('potop.txt', 3, 30))


# Zad_3
class open_conll:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        else:
            parts = line.split()
            return tuple(parts)


with open_conll('nkjp.conll') as infile:
    for token in infile:
        print(token)

import random

ignore_list = ['it', 'the', 'and', 'or', 'if', 'to', 'of', 'that', 'them', 'they', 'he', 'she', 'an', 'a', 'it\'s', 'is', 'for', 'in', 'off', 'with', 'this']


def random_gernerater():
    randomlist = []
    begin = 1
    end = 20
    for i in range(0,10):
        n = random.randint(begin,end)
        begin = begin + 20
        end = end + 20
        randomlist.append(n)
    return randomlist


def word_return(index):
    return words[index] if index < len(words) else "Index Not found"


text = input("Input text:")
text = text.replace(',', '')
text = text.replace('.', '')
words = text.split()
words = list(dict.fromkeys(words))
result = []

# remove words that should be ignored
for idx in range(len(ignore_list)):
    if ignore_list[idx] in words:
        words.remove(ignore_list[idx])


# randomly generate indice
indice = random_gernerater()
for index in indice:
    tmp = word_return(index-1) # modify
    result.append(tmp)

print(result)
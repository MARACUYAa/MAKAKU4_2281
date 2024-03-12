from itertools import product
k = 0
words = product('01234567', repeat = 5)
for w in words:
    word = ''.join(w)
    if word.count('4') == 2 and word[0] != '0':
        word = word.replace('3','1').replace('5','1').replace('7','1')
        if '14' not in word and '41' not in word:
            k += 1
print(k)
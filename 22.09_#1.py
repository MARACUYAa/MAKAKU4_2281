from itertools import product
k = 0 
words = product('01234567', repeat=5)
for w in words:
    word = ''.join(w)
    if word.count('6') == 1 and word[0] != '0':
        word = word.replace('3', '1').replace('5','1').replace('7', '1')
        if '16' not in word and '61' not in word:
            k += 1
print(k)
def prost(x):
    for i in range(2, int(x**0.5) +1):
        if x % i == 0:
            return False
    return True
def delit(n):
    a =[]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    return(sorted(set(a)))
# # #1
# k = 1
# d = {}
# for a in range(1532040, 1532161):
#     d[a] = k
#     k+=1
#     if prost(a) == True:
#         print(d[a], a)

#2
# from fnmatch import fnmatch
# for x in range(0,10**9,17):
#     if fnmatch(str(x), '1?34567?9') == True:
#         print(x, x//17)
# 113456759 6673927
# 133456749 7850397
# 153456739 9026867
# 173456729 10203337
# 193456719 11379807

# #3
k = 0
a = []


for i in range(97**3, 10000000):
    a = delit(i)
    h = 0
    b = []
    for x in a:
        if (len(str(x)) == 3) and ((str(x)[-1]) == '3'):
            h += 1
            b.append(x)
    if h == 3:
        print(i, min(b))
        k += 1
    if k == 5:
        break







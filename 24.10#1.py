def calculate_minimum_packs(n):
    if n % 2 == 0:     
        min_packs = n // 6
    else:        
        min_packs = (n + 2) // 6    
        return min_packs
min_packstotal_students = int(input())
print(calculate_minimum_packs(30) )
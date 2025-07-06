# --TASK-1
# Given a side of square. Find its perimeter and area.
a = int(input('Kvadratni Tomonini Kiriting: '))
perimetri = 4 * a
yuzi = a * a

print(f'Kvadratni Perimetri {perimetri}')
print(f'Kvadratni Yuzasi {yuzi}')



# --TASK-2
# Given diameter of circle. Find its length.
diametri = int(input('Aylananing diametrini kiriting: '))
p = 3.14
uzunlik = diametri * p

print(f'Aylananing uzunligi {uzunlik}')



# --TASK-3
# Given two numbers a and b. Find their mean.
a = int(input('A son Kiriting: '))
b = int(input('B son Kiriting: '))
urtachasi = (a + b) / 2

print(f'{a} va {b} ning urtacha qiymati {urtachasi}')



# --TASK-4
# Given two numbers a and b. Find their sum, product and square of each number.
a = int(input('A son Kiriting: '))
b = int(input('B son Kiriting: '))
yigindisi = a + b
kupaytmasi = a * b
a_kvadrati = a * a
b_kvadrati = b * b

print(f'{a} va {b} ning yigindisi {yigindisi}')
print(f'{a} va {b} ning kupaytmasi {kupaytmasi}')
print(f'{a} ning kvadrati {a_kvadrati}')
print(f'{b} ning kvadrati {b_kvadrati}')

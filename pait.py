import random

spisok = []
for i in range(10):
    spisok.append(random.randint(-10, 10))

print("Zadanie 1")
print("Spisok:", spisok)

summa_otr = 0
summa_chet = 0
summa_nechet = 0
proizv_3 = 1

for i in range(len(spisok)):
    if spisok[i] < 0:
        summa_otr = summa_otr + spisok[i]
    if spisok[i] % 2 == 0:
        summa_chet = summa_chet + spisok[i]
    else:
        summa_nechet = summa_nechet + spisok[i]
    if i % 3 == 0:
        proizv_3 = proizv_3 * spisok[i]

ind_min = spisok.index(min(spisok))
ind_max = spisok.index(max(spisok))
if ind_min > ind_max:
    ind_min, ind_max = ind_max, ind_min

proizv_min_max = 1
for i in range(ind_min + 1, ind_max):
    proizv_min_max = proizv_min_max * spisok[i]

perv_pol = -1
posl_pol = -1
for i in range(len(spisok)):
    if spisok[i] > 0:
        if perv_pol == -1:
            perv_pol = i
        posl_pol = i

summa_pol = 0
if perv_pol != -1 and perv_pol != posl_pol:
    for i in range(perv_pol + 1, posl_pol):
        summa_pol = summa_pol + spisok[i]

print("Summa otricatelnih:", summa_otr)
print("Summa chetnih:", summa_chet)
print("Summa nechetnih:", summa_nechet)
print("Proizvedenie s indeksami kratnimi 3:", proizv_3)
print("Proizvedenie mezhdu min i max:", proizv_min_max)
print("Summa mezhdu pervim i poslednim polozhitelnimi:", summa_pol)

print("Zadanie 2")
spisok2 = []
for i in range(10):
    spisok2.append(random.randint(-10, 10))

print("Ishodniy spisok:", spisok2)

chetnie = []
nechetnie = []
otricatelnie = []
polozhitelnie = []

for chislo in spisok2:
    if chislo % 2 == 0:
        chetnie.append(chislo)
    else:
        nechetnie.append(chislo)
    if chislo < 0:
        otricatelnie.append(chislo)
    if chislo > 0:
        polozhitelnie.append(chislo)

print("Chetnie:", chetnie)
print("Nechetnie:", nechetnie)
print("Otricatelnie:", otricatelnie)
print("Polozhitelnie:", polozhitelnie)

#By Kevin Alvaro Adianto
"""
tup1=("A","B","C","D","E")
tup2=("F","G","H","I","J")
"""
tup1=(1,2,3,4,5)
tup2=(10,11,12,13,14)

lst1,lst2=list(tup1),list(tup2)
hasil1,hasil2=list(),list()

pilihan=int(input("Tukar Ganjil atau Genap (1:ganjil & 2:Genap) :"))

if pilihan == 1:
    for i in range(len(lst1)):
        if i%2 ==1:
            hasil1.append(lst1[i])
        else:
            hasil1.append(lst2[i])
    for x in range(len(lst2)):
        if x%2 ==1:
            hasil2.append(lst2[x])
        else:
            hasil2.append(lst1[x])
elif pilihan ==2:
    for i in range(len(lst1)):
        if i%2 ==0:
            hasil1.append(lst1[i])
        else:
            hasil1.append(lst2[i])
    for x in range(len(lst2)):
        if x%2 ==0:
            hasil2.append(lst2[x])
        else:
            hasil2.append(lst1[x])
else:
    print("mohon masukkan pilihan yang tepat")

hasil1,hasil2=tuple(hasil1),tuple(hasil2)
print(hasil1)
print(hasil2)

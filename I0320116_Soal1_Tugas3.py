list1 = ["Rana","Ano","Fredi","Rafli","Leo","Hitler","Naufal","Dwi","Ruli","Javier"]
print('Nama index 4:', list1[4])
print('Nama index 6:', list1[6])
print('Nama index 7:', list1[7])

print ("sebelum:", list1)

list1[3] = "Rafathar"
list1[5] = "Aura"
list1[9] = "Carol"
print ("sesudah:", list1)


list1.append("Salsabila")
list1.append("Abyan:")
print("list teman baru :", list1)


print("total ada", (len(list1))), "makhluk"
for teman in list1:
    print(list1)
s1 = {"Name":"Zedi",
      "Hobi":["Baca","basket","nonton"],
      "Social medias":["Zedikram", "Line : Zedikram","youtube : zedi ikram el fathi"],
      "Lagu kesukaan":["Heal The World","bila waktu tlah berakhir"],
      "Makanan favorit":["Tempe","ayam goreng"] }

print(s1)

#mengubah hobi
s1["Hobi"][1] = ("catur")
s1["Social medias"][2] = ("zikram")

#menghapus 2 makanan favorit
del s1["Makanan favorit"][0:2]

#menambah 1 hobi
s1.update({"Hobi":["Baca","basket","makan","pergi"]})

print(s1)


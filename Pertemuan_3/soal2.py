# Gunakan aturan pertambahan, pengurangan, dan perkalian saja.

# Diketahui kelereng Aldi sebanyak N maka anda dapat mengetahui banyak kelereng Budi, Anto, dan Agung.

print("================================================")
print("==========  PERHITUNGAN KELERENG ============")
print("================================================")

jumlahDicari = int(input("masukan jumlah aldi :  "))

Budi = jumlahDicari - 15

# (Aldi mempunyai kelereng 15 lebih banyak dari budi)

Anto = 2 * (jumlahDicari+ Budi)

# (anto mempunyai kelerang 2x jumlah kelereng aldi dan budi)

Agung = (jumlahDicari + Budi + Anto) - 5

# (agung memiliki kelerang 5 buah lebih sedikit dari jumlah kelereng aldi, budi dan anto)

# Jadi,

# Input >> N

# // N mengacu pada banyaknya kelereng Aldi

# Output << Budi + Anto + Agung

print("Total kelereng Aldi adalah : ",jumlahDicari) 
print("Total kelereng Budi adalah : ",Budi) 
print("Total kelereng Anto adalah : ",Anto) 
print("Total kelereng Agung adalah : ",Agung) 
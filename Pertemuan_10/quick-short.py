def qs(list,awal,akhir):
    if awal < akhir:
        pindex = partisi(list,awal,akhir)
        qs(list,awal,pindex-1)
        qs(list,pindex+1,akhir)
 
def partisi(list,awal,akhir):
    tengah = int(akhir/2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal,tengah):
        if list[i]>=pivot:
            list[i],list[pindex]=list[pindex],list[i]
            pindex = pindex + 1
    list[pindex],list[tengah]=list[tengah],list[pindex]
    print(list)
    return pindex
 
list = [25,20,15,3,7,2,1]
nama_kelompok=[
    ["1","Cherry Citra","17211107"], 
    ["2","Afri Astio","17210126"],
    ["3","Arief Laksono","17210204"],
    ["4","Ahmad Jalaludin","17210673"],
    ["5","Ezhra Harrison ","17210219"],
    
    ]
print("===== DAFTAR NAMA KELOMPOK ========")
print("Kelompok Pertemuan 10 : ")
print("Kelas : 17.1A.25 ")
print(nama_kelompok[0])
print(nama_kelompok[1])
print(nama_kelompok[2])
print(nama_kelompok[3])
print(nama_kelompok[4])
print("==========================")
print('Data yang akan di sort :', list)
print('Quick Sort :')
qs(list,0,len(list)-1)

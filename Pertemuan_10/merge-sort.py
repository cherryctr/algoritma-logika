
def ms(list):
    print('Memecah List', list)
    n = len(list)
    if n < 2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]
 
        ms(left)
        ms(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):

            list[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list)
 
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


ms(list)

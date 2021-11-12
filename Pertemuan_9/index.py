def cetak_matriks(matriks):
    for row in matriks:
        print(row)


def pjg_matriks(matriks):
    return len(matriks[0])


def lbr_matriks(matriks):
    return len(matriks)


def jumlahkan_matriks(mat_a, mat_b):
    temp_row = []
    temp_mat = []

    for i in range(0, lbr_matriks(mat_a)):
        for j in range(0, pjg_matriks(mat_a)):
            temp_row.append(mat_a[i][j] + mat_b[i][j])
        temp_mat.append(temp_row)
        temp_row = []
    return temp_mat
print("===== DAFTAR NAMA KELOMPOK ========")
nama_kelompok=[
    ["1","Cherry Citra","17211107"], 
    ["2","Afri Astio","17210126"],
    ["3","Arief Laksono","17210204"],
    ["4","Ahmad Jalaludin","17210673"],
    ["5","Ezhra Harrison ","1721XXX"],
    
    ]
print("Kelompok Pertemuan 9 : ")
print(nama_kelompok[0])
print(nama_kelompok[1])
print(nama_kelompok[2])
print(nama_kelompok[3])
print(nama_kelompok[4])
print("==========================")
matriks_a=[[1, 2, 3, 5], [3, 1, 5, 4], [2, 5, 1, 4]]
matriks_b=[[3, 2, 0, 1], [5, 3, 4, 1], [1, 3, 5, 2]]

print("Array Matrix A : ")
cetak_matriks(matriks_a)

print("Array Matrix B : ")
cetak_matriks(matriks_b)
print("hasil penjumlahan matriks : ")


hasil=jumlahkan_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)





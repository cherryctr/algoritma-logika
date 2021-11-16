l = [3,6,9,13,16,26,38,58]

# variable di cari tinggal di isi angka yang ingin di cari misal : 10,13,16
 
dicari = 16
print('Mencari nilai',dicari,'dengan binary search','pada list',l)
ditemukan = False
batas_awal = 0
batas_akhir = len(l) - 1
while not ditemukan and batas_awal <= batas_akhir:
  pos_cari = batas_awal + (batas_akhir-batas_awal)//2 # ambil posisi tengah
  print('posisi pencarian: index',pos_cari,'dengan nilai',l[pos_cari])  
  if l[pos_cari] == dicari:
    ditemukan = True 
  elif l[pos_cari] > dicari:
    batas_akhir = pos_cari-1 # geser 1 titik lebih kecil dari posisi sekarang
  else:
    batas_awal = pos_cari+1 # geser 1 titik lebih besar dari posisi sekarang

if ditemukan:
  print('Nilai',dicari,'ditemukan pada indeks',pos_cari)
else:
  print('Nilai',dicari,'tidak ditemukan')
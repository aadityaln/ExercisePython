## Menghitung Nilai Rata-rata Siswa Menggunakan Tipe Data List

# memasukkan nilai variabel
nilai = [89, 72, 93, 90, 98]

# menghitung total jumlah nilai
totalNilai = sum(nilai)

# menghitung jumlah siswa
jumlahSiswa = len(nilai) #len digunakan untuk menghitung banyaknya jumlah data dalam tipe data list

# menghitung nilai rata - rata siswa
rataRata = totalNilai / jumlahSiswa

# memunculkan nilai rata-rata
print("Jumlah Nilai : ", totalNilai)
print("Jumlah Siswa : ", jumlahSiswa)
print("Rata-rata Nilai : ", rataRata)
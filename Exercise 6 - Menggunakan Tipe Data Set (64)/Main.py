## Program Untuk Mengelolo Data Anggota Klub Menggunakan Tipe Data Set

# mendefinisikan dua set anggota klub
klubA = {"ochaa", "yesha", "kocha", "nopal"}
klubB = {"ochaa", "azhar", "am", "kocha"}

# menentukan anggota klub gabungan
anggotaGabungan = klubA.union(klubB)
print("Anggota Gabungan Klub A dan B:", anggotaGabungan)

# menentukan anggota klub yang merupakan anggota keduanya
anggotaBersama = klubA.intersection(klubB)
print("Anggota Bersama Klub A dan B:", anggotaBersama)

# menampilkan anggota yang hanya bergabung dengan klub A
anggotaKlubA = klubA.difference(klubB)
print("Anggota Klub A Saja:", anggotaKlubA)

# menampilkan anggota yang hanya bergabung dengan klub B
anggotaKlubB = klubB.difference(klubA)
print("Anggota Klub B Saja:", anggotaKlubB)
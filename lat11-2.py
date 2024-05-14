Data = ('Gabriel Sachio Atmadjaja', '71231052', 'Yogyakarta, DI Yogyakarta')

nama, nim, alamat = Data
print(f"NIM            : {nim}")
print(f"NAMA           : {nama}")
print(f"ALAMAT         : {alamat}\n")

nama = nama.split(" ")
print(f"NIM            : {tuple(nim)}\n")
print(f"NAMA DEPAN     : {tuple(nama[0])}\n")
print(f"NAMA TERBALIK  : {tuple(nama[::-1])}\n")
nama ="Dita"
alamat="lutang"
tanggal_lahir=10
jenis_kelamin= "perempuan"
tinggibadan= 155
berat_badan=40.3

print(alamat,type(alamat))
print(tanggal_lahir, type(tanggal_lahir))
print(jenis_kelamin, type(jenis_kelamin))
print(tinggibadan, type(tinggibadan))
print(berat_badan,type(berat_badan))
print("soal yang di kerjakan")

print(''' Nim D0221351
    Gaji Pokok = 5.000.000
    Gaji lembur/ jam = 1.000.000
    Lama Lembur =  angka terakhir  nim di kurangi 30
    Gaji Lembur = (gaji lembur /jam)* lama lembur
    pajak = 15%''')
gaji_pokok=5000000
gaji_lembur_per_jam=1000000
lama_lembur=(51-30)
gaji_lembur=1000000*lama_lembur
pendapatan_kotor=gaji_pokok+gaji_lembur
potongan=5000000*15/100
pendapatan_bersih=pendapatan_kotor-potongan
print("gaji_pokok:",gaji_pokok)
print("gaji lembur per jam :",gaji_lembur_per_jam)
print("lama lembur:",lama_lembur)
print("gaji lembur :",gaji_lembur)
print("pendapatan kotor :",pendapatan_kotor)
print("potongan:",potongan)
print("pendapatan bersih:",pendapatan_bersih)

nilai=-13
if nilai > 0 :
    print("nilai merupakan bilangan positif ")
elif nilai < 0:
    print("nilai merupakan bilangan negatif ")
else:
    print("nilai bukan bilangan negatif dan bilangan positif ")
    
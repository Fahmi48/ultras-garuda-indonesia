#LATIHAN DASAR PEMROGRAMAN
print("-----------------------------")
print("====GEROBAK FRIED CHICKEN====")
print("-----------------------------")
print(" Kode   JenisPotong   Harga ")
print("-----------------------------")
print("  D        Dada      Rp3000  ")
print("  P        Paha      Rp2500  ")
print("  S       Sayap      Rp5000  ")
print("-----------------------------")

#Proses Input
bj=int(input("Banyak Jenis: "))
kode=[]
bp=[]
jp=[]
ha=[]
jumlah=[]
i=0
for i in range(bj) :
    print("Jenis Ke-", i+1)
    kode.append(input("Kode Potong [D/P/S]: "))
    bp.append(int(input("Banyak Potong: ")))
    if kode[i]=="D" :
        jp.append("Dada")
        ha.append("3000")
        jumlah.append(bp[i]*int("3000"))
    elif kode[i]=="P":
        jp.append("Paha")
        ha.append("2500")
        jumlah.append(bp[i]*int("2500"))
    elif kode[i]=="S" :
        jp.append("Sayap")
        ha.append("5000")
        jumlah.append(bp[i]*int("5000"))
    else :
        jp.append(input("Kode Yang Anda Masukan Salah"))
        ha.append(input("0"))
        jumlah.append(bp[i]*int(0))

#Proses Output
print("-------------------------------")
print("=====GEROBAK FRIED CHICKEN=====")
print("-------------------------------")
print("No. Jenis  Harga Banyak  Jumlah")
print("    Potong Satuan  Beli   Harga")
print("-------------------------------")

jb=0
a=0
while a<bj :
    jb=jb+jumlah[a]
    print("%i  %s  %s  %i  %i" % (a+1, jp[a], ha[a], bp[a], jumlah[a]))
    a=a+1
print("-------------------------------")
pajak=jb+0.1
tb=jb+pajak
print("       Jumlah Bayar Rp.", jb)
print("        Pajak 10% Rp.", pajak)
print("        Total Bayar Rp.", tb)
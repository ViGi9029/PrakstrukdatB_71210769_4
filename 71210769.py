import json
    
karyawan = {}
kolega = [{},{}]

jmlkrwn = int(input("Masukkan jumlah karyawan baru : "))


for i in range(jmlkrwn):
    nama1 = input("Masukkan nama :")
    alamat = input("Masukkan alamat:")
    jmlkolega = int(input("Masukkan jumlah kolega:"))
    for j in range(jmlkolega):
        kol = input("Masukkan nama kolega ke-"+str(j+1)+":")
    karyawan[nama1][0]["alamat"] = alamat
    karyawan[nama1][1]["kolega"] = kolega

# with open("karyawan.json","r+")as file:
#     file_data = json.load(file)
# data[3] =
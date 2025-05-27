import pymysql
import os
import time

mydb = pymysql.connect(
host="localhost",
user= "root",
password="Kereta1000.",
database="tester1"
)

def create():
    NamaBarang = input("Masukan nama barang: ")
    StokBarang = int(input("Masukan stok barang: "))

    formula = "INSERT INTO tabel1 (nama, stok) VALUES (%s, %s)"
    buat = (NamaBarang, StokBarang)
    mycursor = mydb.cursor()
    mycursor.execute(formula, buat)
    mydb.commit()
    print("data telah ditambahkan!")
    time.sleep(3)
    os.system('cls')


def read():
    cari_apa=input("Cari apa masehh??:")

    cari= f"SELECT * FROM tabel1 Where nama='{cari_apa}'"
    mycursor = mydb.cursor()
    mycursor.execute(cari)
    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

    time.sleep(3)
    os.system('cls')

def update():
    ganti_nama = input("Barang apa yang ingin diganti stoknya?: ")
    ganti_stok = int(input("Masukan Stok Baru: "))

    formula=f"UPDATE tabel1 SET stok = {ganti_stok} WHERE nama = '{ganti_nama}'"
    mycursor=mydb.cursor()
    mycursor.execute(formula)
    mydb.commit()

    print("Data telah berhasil diupdate")
    
    time.sleep(3)
    os.system('cls')

def delete():
    hapus_barang = input("Barang apa yang ingin dihapus?: ")

    formula=f"DELETE FROM tabel1 WHERE nama = '{hapus_barang}'"
    mycursor=mydb.cursor()
    mycursor.execute(formula)
    mydb.commit()

    print()
    print("Data telah berhasil dihapus")
    
    time.sleep(3)
    os.system('cls')

main = True

while main:
    print("CRUD PERTAMA MENGGUNAKAN SQL")
    print()
    print("SELECT ONE:")
    print("1. Cari Data")
    print("2. Import Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Keluar")
    print()
    
    pilih = input("Pilih (Ketik Hanya Angka saja): ")

    if pilih == "1":
        read()
    
    elif pilih== "2":
        create()
    
    elif pilih == "3":
        update()
    
    elif pilih == "4":
        delete()

    elif pilih == "5":
        main = False
        print("Keluar dari program...")

    else:
        print("Pilihan tidak valid, coba lagi.")
    

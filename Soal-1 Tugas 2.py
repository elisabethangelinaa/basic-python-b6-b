def show_contact():
    print ("Daftar Kontak: ")
    print ("Nama: Angel")
    print ("No Telepon: 0812890678")
    print ("Nama: Joko")
    print ("No Telepon: 08128675345")

def insert_contact():
    Nama = input("Nama: ")
    No_telepon= input ("No telepon: ")
    print("Kontak berhasil ditambahkan")

def exit():
    print("Program selesai, sampai jumpa!")

def show_menu():
    print ("Selamat Datang!")
    print("==Menu==")
    print("[1] Daftar Kontak")
    print("[2] Tambah Kontak")
    print("[3] Keluar")
    menu= int(input("Pilih menu: "))  

    if menu == 1:
        show_contact()
    elif menu == 2:
        insert_contact()
    elif menu == 3:
        exit()
    else:
        print("Menu tidak tersedia")
show_menu()












    







     
   


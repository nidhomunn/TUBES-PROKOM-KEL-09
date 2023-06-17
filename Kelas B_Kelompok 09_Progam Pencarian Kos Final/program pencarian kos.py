import csv
import random

#menu awal
def menu():
    print("========================================================================================")
    print("=                        SELAMAT DATANG DI PROGRAM PENCARIAN KOST!                     =")
    print("========================================================================================")
menu()

def read_csv(datauser):
    data = []
    with open(datauser, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(datauser, data):
    with open(datauser, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#sign in
def signin():
    print("\nSign In")
    username = input("Masukkan email atau username akun Anda: ")
    password = input("Masukkan password akun Anda           : ")
    data = read_csv('datauser.csv')
    for row in data:
        if (row[0] == username or row[1] == username) and row[2] == password:
            print("========================================================================================\n")
            print("                                  INFORMASI PENGGUNA                                    ")
            print("Selamat datang,", row[1])
            print("Sign In telah berhasil.")
            return
        
    print("Username atau password Anda tidak valid.")
    signin()

#sign up
def signup():
    print("\nSign Up")
    email    = input("Masukkan email                        : ")
    username = input("Masukkan username                     : ")
    password = input("Masukkan password                     : ")
    data = read_csv('datauser.csv')
    for row in data:
        if row[0] == email or row[1] == username:
            print("Email atau username telah digunakan.\n")
            signup()
            return
        
    data.append([email, username, password])
    write_csv('datauser.csv', data)
    print("Akun berhasil dibuat, silakan lakukan Sign In.")
    signin()

#akun
def akun():
    print("\nPilih Sign Up jika belum memiliki akun atau pilih Sign In jika sudah memiliki akun.")
    print("1. Sign In")
    print("2. Sign Up")
    try:
        opsi = int(input("Pilih opsi (1/2)                      : "))
        if opsi == 1:
            signin()
        elif opsi == 2:
            signup()
        else:
            print("Pilihan tidak valid.")
            akun()
    except ValueError:
        print("Kesalahan: Masukan harus berupa angka (1/2).")
        akun()
akun()

def buka_detail_data(pilihkost):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == pilihkost:
                print('==============================================================\n')
                print("                         DETAIL KOST                         ")
                print("")
                print(f"Nama Kost                   : {i[1]}")
                print(f"Alamat                      : {i[3]}")
                print(f"Ukuran                      : {i[4]}")
                print(f"Harga Kost/Tahun            : {i[5]}")
                print(f"Fasilitas                   : {i[6]}")
                print(f"Narahubung                  : {i[7]}")
                print(f"Jumlah Kamar yang Tersedia  : {i[8]}")
                print('==============================================================')
                return True
        return False

def aplikasi():
    global total_harga
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print("\nSelamat datang di Program Pencarian Kost!")
        print("Pilih Jenis Kost (L/P)")
        daftar_kost = []
        jeniskost = input("Jenis Kost: ")
        if jeniskost.upper() == 'L':
            print("\nBerikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.001")
            print("2. Rp. 5.000.001 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            try:
                harga = int(input("Pilih Daftar Harga Kost/Tahun (1/2/3) : "))
                if harga == 1:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if int(i[5]) <= 5000000 and i[2] == 'L':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                elif harga == 2:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if 5000000 < int(i[5]) <= 10000000 and i[2] == 'L':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                elif harga == 3:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if int(i[5]) > 10000000 and i[2] == 'L':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                else:
                    print("Pilihan tidak valid.")
                    print('==============================================================')
                    aplikasi()
            except ValueError:
                print("Kesalahan: Masukan harus berupa angka (1/2/3).")
                aplikasi()

        elif jeniskost.upper() == 'P':
            print("\nBerikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.001")
            print("2. Rp. 5.000.001 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            try:
                harga = int(input("Pilih Daftar Harga Kost/Tahun (1/2/3) : "))
                if harga == 1:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if int(i[5]) <= 5000000 and i[2] == 'P':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                elif harga == 2:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if 5000000 < int(i[5]) <= 10000000 and i[2] == 'P':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                elif harga == 3:
                    print('==============================================================\n')
                    print("DAFTAR KOST:")
                    for i in csv_reader:
                        if int(i[5]) > 10000000 and i[2] == 'P':
                            daftar_kost.append(i)
                            print(f'{i[0]}. {i[1]}')
                else:
                    print("Pilihan tidak valid.")
                    print('==============================================================')
                    aplikasi()
            except ValueError:
                print("Kesalahan: Masukan harus berupa angka (1/2/3).\n")
                aplikasi()
                
        else:
            print("Pilihan tidak valid.")
            print('==============================================================')
            aplikasi()
        
    print('==============================================================')
    print("\nApakah Anda ingin membuka detail salah satu kost?")
    print("1. Ya")
    print("2. Tidak")
    try:
        pilihan = int(input("Masukkan pilihan (1/2): "))
        if pilihan == 1:
            pilihkost = input("Pilih nomor kost pada daftar untuk melihat detail: ")
            kost_ditemukan = False
            for kost in daftar_kost:
                if kost[0] == pilihkost:
                    buka_detail_data(pilihkost)
                    kost_ditemukan = True
                    print("")
                    jumlahkamar = int(input("Masukkan jumlah kamar kost yang ingin disewa: "))
                    if 1 <= jumlahkamar <= int(kost[8]):
                        total_harga = jumlahkamar * int(kost[5])
                        print(f'Total harga sewa: Rp {total_harga}')
                        print("Apakah anda ingin melanjutkan ke menu pembayaran?")
                        print("1. Ya")
                        print("2. Tidak")
                        try:
                            keputusan = int(input("Masukkan pilihan (1/2): "))
                            if keputusan == 1:
                                pembayaran()
                            elif keputusan == 2:
                                print("Silakan kembali ke menu awal")
                                aplikasi()
                            else:
                                print("Pilihan tidak valid.")
                                aplikasi()
                        except ValueError:
                            print("Kesalahan: Masukan harus berupa angka (1/2).")
                            aplikasi()
                    else:
                        print("Kamar yang tersedia tidak cukup, akan dikembalikan ke menu awal.")
                        aplikasi() 
            if not kost_ditemukan:
                print("Detail kos tidak tersedia.")
                aplikasi()
        elif pilihan == 2:
            aplikasi()
        else:
            print("Pilihan tidak valid.")
            aplikasi()
    except ValueError:
                print("Kesalahan: Masukan harus berupa angka (1/2).")
                aplikasi()

def pembayaran():
    print("\nPilih metode pembayaran:")
    print("1. BANK MANDIRI")
    print("2. BANK BCA")
    print("3. GOPAY")
    print("4. CASH")
    try:
        pilihan_metode = int(input("Masukkan nomor metode pembayaran yang dipilih: "))
        if pilihan_metode == 1:
            print("Anda memilih pembayaran dengan BANK MANDIRI : 1234567890 .")
            total_pembayaran = int(input("Masukkan total pembayaran: "))
            if total_pembayaran == total_harga:
                kode_bayar = generate_kode_pembayaran()
                print("Kode pembayaran:", kode_bayar)
                kode_input = input("Masukkan kode bayar: ")
                if kode_input == kode_bayar:
                    print("Kode pembayaran valid.")
                    print("Pembayaran berhasil")
                    bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
                else:
                    print("Kode pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                    pembayaran()
            else:
                print("Total pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                pembayaran()

        elif pilihan_metode == 2:
            print("Anda memilih pembayaran dengan BANK BCA :0987654321.")
            total_pembayaran = int(input("Masukkan total pembayaran: "))
            if total_pembayaran == total_harga:
                kode_bayar = generate_kode_pembayaran()
                print("Kode pembayaran:", kode_bayar)
                kode_input = input("Masukkan kode bayar: ")
                if kode_input == kode_bayar:
                    print("Kode pembayaran valid.")
                    print("Pembayaran berhasil")
                    bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
                else:
                    print("Kode pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                    pembayaran()
            else:
                print("Total pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                pembayaran()

        elif pilihan_metode == 3:
            print("Anda memilih pembayaran dengan GOPAY :2222222222.")
            total_pembayaran = int(input("Masukkan total pembayaran: "))
            if total_pembayaran == total_harga:
                kode_bayar = generate_kode_pembayaran()
                print("Kode pembayaran:", kode_bayar)
                kode_input = input("Masukkan kode bayar: ")
                if kode_input == kode_bayar:
                    print("Kode pembayaran valid.")
                    print("Pembayaran berhasil")
                    bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
                else:
                    print("Kode pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                    pembayaran()
            else:
                print("Total pembayaran tidak valid, pembayaran gagal. Silakan lakukan pembayaran ulang.")
                pembayaran()

        elif pilihan_metode == 4:
            print("Silahkan melakukan pembayaran sebesar Rp", total_harga, "dengan pemilik kost.")

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            pembayaran()
    
    except ValueError:
        print("Kesalahan: Masukan harus berupa angka (1/2/3/4).\n")
        pembayaran()

def generate_kode_pembayaran():
    kode_bayar = ''.join(random.choices('0123456789', k=6))
    return kode_bayar

def bukti_pembayaran(pilihan_metode, kode_bayar, total_harga ):
    print("Bukti Pembayaran:")
    if pilihan_metode == 1:
        metode_pembayaran = "BANK MANDIRI"
    elif pilihan_metode == 2:
        metode_pembayaran = "BANK BCA"
    elif pilihan_metode == 3:
        metode_pembayaran = "GOPAY"
    else:
        metode_pembayaran = "CASH"
    print()
    print('==============================================================')
    print("                         STRUK PEMESANAN                      ")
    print('==============================================================\n')
    print("                 Metode Pembayaran:", metode_pembayaran)
    print("                 Dengan Kode Bayar:", kode_bayar)
    print("                 Total pembayaran :", total_harga)
    print("          Pemesanan kost sudah otomatis masuk kedalam sistem")
    print("                 Terima kasih atas pembayaran Anda.\n")

aplikasi()
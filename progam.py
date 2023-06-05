#ini bikinya disini ya ges
#SEMANGATTT!!

def login():
    email = input ("masukkan email anda:")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek username dan password
    if email == "@gmail.com" and username == "user" and password == "password":
        return True
    else:
        return False

def signup():
    email = input ("masukkan email anda:")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    # Simpan informasi akun pengguna baru ke dalam database atau file
    # ...

    print("Akun berhasil dibuat. Silakan login.")

# Pilihan menu
print("Selamat datang!")
print("1. Sign In")
print("2. Sign Up")

choice = input("Pilih opsi: ")

if choice == "1":
    if login():
        print("Login berhasil!")
        # Panggil fungsi atau tampilkan menu setelah login berhasil
    else:
        print("Username atau password salah.")
        # Panggil fungsi login kembali atau berikan pesan error
elif choice == "2":
    signup()
else:
    print("Pilihan anda tidak valid.")

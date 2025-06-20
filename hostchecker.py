import socket

domain = input("Masukkan domain (contoh: google.com): ")
try:
    ip = socket.gethostbyname(domain)
    print(f"IP dari {domain} adalah: {ip}")
except:
    print("❌ Gagal mendapatkan IP")

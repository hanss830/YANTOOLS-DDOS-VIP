import os
import time
from colorama import Fore, Style

def warna(text, warna_code):
    return warna_code + text + Style.RESET_ALL

def animate_text(text, delay=0.07):
    current = ""
    for char in text:
        current += char
        print(warna(".......", Fore.MAGENTA) + warna(current, Fore.YELLOW))
        time.sleep(delay)
    return current

os.system("clear")
print(warna("🔥 Starting YANTOOLS-DDOS-VIP 🔥", Fore.MAGENTA))
time.sleep(1)

animate_text("YANTOOLS-DDOS VIP EDITION", 0.05)
print(warna("🔰 TOOLS GACOR BY @YanOfficialID 🔰\n", Fore.YELLOW))
time.sleep(0.5)

print(warna("💖 Dev: @YanOfficialID", Fore.MAGENTA))
print(warna("📞 CS: Telegram Ready...", Fore.YELLOW))
print(warna("🌐 Use: Domain atau IP, tampilan warna GACOR
", Fore.MAGENTA))
time.sleep(0.5)

print(warna("┌─[ MENU TOOLS ]─┐", Fore.YELLOW))
print(warna("│ 1. CEK IP HOST", Fore.MAGENTA))
print(warna("│ 2. DDOS DOMAIN/IP", Fore.MAGENTA))
print(warna("│ 3. STATUS TOOLS", Fore.MAGENTA))
print(warna("└────────────────┘", Fore.YELLOW))

menu = input(warna("\nPilih menu (1/2/3): ", Fore.YELLOW))

if menu == "1":
    os.system("python hostchecker.py")
elif menu == "2":
    os.system("python ddosgacor.py")
elif menu == "3":
    os.system("python status.py")
else:
    print(warna("❌ Menu tidak valid.", Fore.MAGENTA))

import urllib.request
import socket
import os

socket.setdefaulttimeout(3)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_bad_proxy(proxy):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User -Agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        
        response = urllib.request.urlopen('http://www.google.com', timeout=6)
        return False
    except Exception as e:
        return True

def read_proxies_from_file(filename):
    try:
        with open(filename, 'r') as file:
            proxies = [line for line in file.read().splitlines() if line.strip()]
        return proxies
    except FileNotFoundError:
        print(f"Không Tồn Tại '{filename}' Vui Lòng Để Chung Tool Và '{filename}' Vào 1 Thư Mục")
        return []

def write_proxies_to_file(filename, proxies):
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")

clear_screen()
print("Check Proxy — nhta [ t.me/Hani_Network ]")
print("—————————————————————————————————————————————")
filename = input("Nhập File Chứa Proxy (VD: proxy.txt):  ")
proxyList = read_proxies_from_file(filename)
print(f"'{filename}' Hiện Đang Có {len(proxyList)} Proxy")
print("—————————————————————————————————————————————")
remove_duplicates = input("Bạn Có Muốn Xoá Những Proxy Trùng Nhau Không? (y/n):  ").strip().lower()

if remove_duplicates == 'y':
    unique_proxies = list(set(proxyList))
    write_proxies_to_file(filename, unique_proxies)
    print(f"Đã Xoá Những Proxy Trùng Nhau — Còn Lại {len(unique_proxies)} Proxy")
    print("—————————————————————————————————————————————")
    proxyList = unique_proxies
elif remove_duplicates == 'n':
    print("—————————————————————————————————————————————")

print("Tool Sẽ Tự Động Xoá Proxy DIE Khỏi File Và Giữ Proxy LIVE")
input("Ấn 'Enter' Để Tiến Hành Check Proxy")

print("—————————————————————————————————————————————")

live_proxies = []

for proxy in proxyList:
    if is_bad_proxy(proxy):
        print(f"❌ DIE — Đã Xoá | {proxy}")
        proxyList.remove(proxy)
        write_proxies_to_file(filename, proxyList)
    else:
        print(f"✅ LIVE | {proxy}")
        live_proxies.append(proxy)

write_proxies_to_file(filename, live_proxies)
print("—————————————————————————————————————————————")
print(f"Đã Check Xong Các Proxy, {len(live_proxies)} Proxy Live Của Bạn Đã Được Lưu")
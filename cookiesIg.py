import requests
import time
import pickle

# url melakukan login ke instagram
URL = "https://www.instagram.com/accounts/login/ajax/"

# header agar bisa login menggunakan metode ajax
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/",
    "X-Instagram-AJAX": "1",
    "X-CSRFToken": "",  # di ambil di requests (1)
    "Content-Type": "application/x-www-form-urlencoded",
}

# inputan username 
AdiyZd_username = input("Masukan Username : ")
AdiyZd_password = input("Masukan Password : ")

# data yang telah di input akan di kirim ke post agar bisa mengfalidasi login
# jangan di ganti sembarangan nanti losak!!!
data = {
    "username": AdiyZd_username,
    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(time.time()), AdiyZd_password),
    "queryParams": {},
    "optIntoOneTap": "false"
}

# biyar cookies lu bertahan gak basi nih gw buatin borax nya
session = requests.Session()


# mengirim permintaan login tadi dan agar bisa mendapat tooken CSRF_token
mbuh_kagaktau_guweh = session.get("https://www.instagram.com/accounts/login/")
headers['X-CSRFToken'] = mbuh_kagaktau_guweh.cookies['csrftoken']

# mengirim kan permintaan post untuk kirim
gerakan = session.post(URL, data=data, headers=headers)

# falidasi login lu nih kontol
if gerakan.status_code == 200 and gerakan.json().get("authenticated"):
    print("berhasil login kontol")


    # nih cookies lo kontol
    cookies = session.cookies.get_dict()


    # ge simpenin di file agar gak lupa
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)

    print("cookies sudah tak simpankan di file 'cookies_frash'")
else:
    print("login gagal periksa username dan password, nih response dari server", gerakan.text)



# jangan lupa sama saya AdiyZd#1
# ini 100% aman
# jan lupa makan jan crack saja 

# cookies di batasi sampai 10 jam 
# biyar tidur gak crack saja



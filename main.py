import os
import sys

GITHUB_SO_URL = "https://raw.githubusercontent.com/hhtethtet277-svg/wi/refs/heads/main/un.so"

if not os.path.exists("un.so"):
    print("[*] Downloading required components (un.so)...")
    try:
        import requests
        response = requests.get(GITHUB_SO_URL, stream=True)
        if response.status_code == 200:
            with open("un.so", "wb") as f:
                f.write(response.content)
            print("[+] Download complete successfully.")
        else:
            os.system(f'curl -L -o un.so "{GITHUB_SO_URL}"')
    except Exception:
        os.system(f'curl -L -o un.so "{GITHUB_SO_URL}"')

print("[*] Launching un.so module...")

try:
    import un
    # HWID check တဲ့နေရာမှာ sys.exit(0) ဖြစ်ပြီး တန်းပိတ်မသွားအောင် 
    # အောက်က feature ထဲကို အတင်းဝင်ခိုင်းပြီး Error ထုတ်ခိုင်းတာပါ
    if hasattr(un, 'current_wifi'):
        print("[+] Module loaded. Starting current_wifi function...")
        # check_security() နေရာမှာ ပိတ်နေရင် ကျော်ပြီး တန်းပွင့်လာအောင် စမ်းသပ်ခြင်း
        un.current_wifi("Developer Bypass Mode")
    else:
        print("[-] Error: current_wifi function not found in un.so")
except ImportError as e:
    print(f"[-] Import Error: {e}")
    print("[!] Please make sure your Python version matches the compiled .so file version.")
except Exception as e:
    print(f"[-] Runtime Error occurred: {e}")

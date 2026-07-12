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
    if hasattr(un, 'current_wifi'):
        print("[+] Security Bypass Active. Starting Tool...")
        # HWID check ကို ကျော်ပြီး wifi function ဆီ တိုက်ရိုက်သွားခိုင်းခြင်း
        un.current_wifi("Verified (Bypass Mode)")
    else:
        print("[-] Error: current_wifi function not found in un.so")
except ImportError as e:
    print(f"[-] Import Error: {e}")
    print("[!] Please make sure your Python version matches the compiled .so file version.")
except Exception as e:
    print(f"[-] Runtime Error: {e}")

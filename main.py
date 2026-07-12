import os
import sys

# ၁။ သင်ပေးထားသော GitHub ပေါ်က un.so ဖိုင်၏ Raw Link အတိအကျ
# (မှတ်ချက်- ဤနေရာတွင် un.so ကို တင်ထားသည့် သင်၏ GitHub Raw Link ကို ထည့်ပေးရပါမည်)
GITHUB_SO_URL = "https://raw.githubusercontent.com/hhtethtet277-svg/wi/refs/heads/main/un.so"

# ၂။ စက်ထဲမှာ un.so ဖိုင် ရှိမရှိ စစ်ဆေးပြီး မရှိပါက အလိုအလျောက် ဒေါင်းလုဒ်ဆွဲခြင်း
if not os.path.exists("un.so"):
    print("\033[1;33m[*] Downloading required components (un.so)... \033[1;00m")
    try:
        import requests
        response = requests.get(GITHUB_SO_URL, stream=True)
        if response.status_code == 200:
            with open("un.so", "wb") as f:
                f.write(response.content)
            print("\033[1;32m[+] Download complete successfully.\033[1;00m")
        else:
            # requests ဖြင့် ဒေါင်းလုဒ်ဆွဲ၍ အဆင်မပြေပါက curl ဖြင့် ဒုတိယနည်းလမ်းပြောင်းဆွဲခြင်း
            os.system(f'curl -L -o un.so "{GITHUB_SO_URL}"')
    except Exception:
        os.system(f'curl -L -o un.so "{GITHUB_SO_URL}"')

# ၃။ ဒေါင်းလုဒ်ဆွဲပြီးပါက .so ဖိုင်ကို လှမ်းခေါ်ပြီး တန်း Run ခြင်း
try:
    import un
except ImportError as e:
    print(f"\033[1;31m[-] Import Error: {e}\033[1;00m")
    print("\033[1;33m[!] Please make sure your Python version matches the compiled .so file version.\033[1;00m")

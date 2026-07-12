import un
import sys

if __name__ == "__main__":
    try:
        # un.py ထဲက check_security() ကို ခေါ်ခြင်း
        is_valid, expiry_info = un.check_security()
        if is_valid:
            # un.py ထဲက current_wifi() ကို ခေါ်ခြင်း
            un.current_wifi(expiry_info)
    except KeyboardInterrupt:
        print("\n[!] Stopped by User.")
    except Exception as e:
        print(f"\n[!] Error: {e}")

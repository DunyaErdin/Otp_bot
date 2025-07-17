import subprocess
import json
import re
import time
import requests

token = "o.Pf0fBOfNtKuAWtCxBm0JIvY4yj15s9uV"

def send_pushbullet(title, message):
    data = {
        "type": "note",
        "title": title,
        "body": message
    }
    headers = {
        "Access-Token": token,
        "Content-Type": "application/json"
    }
    response = requests.post("https://api.pushbullet.com/v2/pushes", json=data, headers=headers)
    if response.status_code == 200:
        print("Pushbullet bildirimi gönderildi")
    else:
        print("Push gönderilemedi", response.text)

def extract_otp(text):
    match = re.search(r"doğrulama kodunuz[:：]?\s*(\d{4,8})", text, re.IGNORECASE)
    return match.group(1) if match else None

def get_sms_list(limit=5):
    result = subprocess.run(['termux-sms-list', '-l', str(limit)], capture_output=True, text=True)
    sms_list = json.loads(result.stdout)
    return sms_list

def main():
    seen_ids = set()
    last_otp = None  # En son gönderilen OTP'yi tutacak
    print("OTP bot başlatıldı... Gelen SMS'ler dinleniyor.")
    while True:
        sms_list = get_sms_list()
        vfs_msgs = [sms for sms in sms_list if "KOSMOSVIZE" in sms.get('body', '').upper()]
        if not vfs_msgs:
            time.sleep(12)
            continue

        latest_sms = max(vfs_msgs, key=lambda x: x.get('received', ''))
        sms_id = latest_sms.get('_id')
        if sms_id not in seen_ids:
            otp = extract_otp(latest_sms['body'])
            if otp:
                if otp != last_otp:   # Yeni OTP eskiyle aynı mı kontrolü
                    print(f"[✅] Yeni OTP: {otp}")
                    send_pushbullet("VFS Yeni OTP", otp)
                    last_otp = otp
                else:
                    print("[ℹ️] Aynı OTP, bildirim gönderilmedi.")
            seen_ids.add(sms_id)
        time.sleep(12)

if __name__ == "__main__":
    main()

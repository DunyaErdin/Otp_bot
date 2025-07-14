#!/data/data/com.termux/files/usr/bin/bash

echo "📦 Gerekli paketler kuruluyor..."
pkg update -y
pkg install -y python termux-api git

echo "🐍 Python modülleri yükleniyor..."
pip install requests

echo "📁 Script klasörü oluşturuluyor..."
mkdir -p ~/otpbot
cd ~/otpbot

echo "📄 Bot scripti indiriliyor..."
curl -O https://raw.githubusercontent.com/DunyaErdin/Otp_bot/main/Android/otp_bot.py

echo "🚀 Başlangıç betiği oluşturuluyor..."
mkdir -p ~/.termux/boot
echo -e "#!/data/data/com.termux/files/usr/bin/bash\npython ~/otpbot/otp_bot.py" > ~/.termux/boot/start
chmod +x ~/.termux/boot/start

echo "📌 Bot ilk defa başlatılıyor..."
nohup python ~/otpbot/otp_bot.py > /dev/null 2>&1 &

echo "✅ Kurulum tamamlandı!"
echo "🔁 Telefon yeniden başladığında bot otomatik çalışacak."
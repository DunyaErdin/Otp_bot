# OTP Yakalama ve Bildirim Botu

Bu proje, SMS yoluyla gönderilen OTP (tek kullanımlık şifre) kodlarını otomatik olarak yakalamak ve anlık bildirim yapmak amacıyla geliştirilmiştir. Özellikle vize başvuru ve randevu sitelerinde SMS ile gelen doğrulama kodlarının hızlı ve güvenli şekilde alınmasını sağlar.

---

## Özellikler

- 📲 **SMS Okuma**  
  Android cihazda Termux kullanılarak telefonun gelen kutusundaki SMS’ler okunur.

- 🔔 **Anlık Bildirim**  
  Pushbullet API ile SMS içeriğindeki OTP kodları anlık olarak bildirilir.

- 🔐 **Güvenli ve Hızlı**  
  Kodlar kullanıcı müdahalesi olmadan hızlıca alınır, manuel giriş ihtiyacını azaltır.

---

## Kullanılan Teknolojiler

- Termux (Android terminal emülatörü)  
- Bash / Python scriptleri (SMS okuma için)  
- Pushbullet API  
- Python / Node.js (isteğe bağlı bildirim entegrasyonu)

---

## Ortam Değişkenleri

| Değişken Adı         | Açıklama                    |
|----------------------|-----------------------------|
| `PUSHBULLET_API_KEY` | Pushbullet API erişim anahtarı |

---

## Lisans

Bu proje GNU Lisansı ile yayımlanmıştır.

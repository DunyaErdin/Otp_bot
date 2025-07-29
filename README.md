# Vize Takip ve Yönetim Paneli

Türkiye'deki vize danışmanlık firmaları için geliştirilmiş kapsamlı ve profesyonel bir vize başvuru yönetim sistemidir. Başvuru takibi, evrak yönetimi, vize türü seçimi ve işlem durumları gibi tüm süreçleri merkezi ve kullanıcı dostu bir panel üzerinden kolayca kontrol etmenizi sağlar. Ayrıca, müşterilerin kendi başvuru süreçlerini takip edebileceği entegre bir **müşteri portalı** ile iletişim ve süreç yönetimini hızlandırır.

---

## ✨ Özellikler

- 📌 **Başvuru Takibi**  
  Her başvuru ayrı ayrı takip edilir; başvuru durumları (ön kayıt, evrak bekleniyor, randevu alındı, sonuçlandı vb.) sistem üzerinden izlenebilir.

- 🗂️ **Evrak Yönetimi**  
  Vize türüne göre gerekli belgeler tanımlanabilir. Evrakların durumu “eksik”, “tamamlandı” gibi statülerle takip edilir.

- 🌍 **Vize Türü ve Ülke Bazlı Özelleştirme**  
  Turistik, ticari, öğrenci, aile birleşimi gibi farklı vize türlerine ve ülkelere göre özelleştirilebilir yapı.

- 👤 **Müşteri Portalı**  
  Başvuru sahipleri, portal üzerinden süreçlerini, evrak durumlarını ve eksik belgeleri online olarak takip edebilir.

- 👥 **Çok Kullanıcılı Yapı ve Yetkilendirme**  
  Kullanıcı rolleri (danışman, yönetici, personel) ile yetkilendirme sağlanır.

- 🔐 **Güvenli Giriş Sistemi ve JWT Desteği**  
  Token tabanlı kimlik doğrulama ve oturum yönetimi.

- 📤 **E-posta Bildirimleri**  
  Evrak eksikliği ve işlem durumları hakkında otomatik e-posta bilgilendirmeleri.

- 🧾 **Pasaport ve Vize MRZ (Machine Readable Zone) Okuma Desteği**  
  Pasaport ve vize üzerindeki MRZ alanları otomatik okunarak veri girişinin hızlı ve doğru yapılması sağlanır. Görüntü kalitesine bağlı olarak doğruluk değişebilir.

- 🔐 **OTP Yakalama ve Bildirim Sistemi**  
  Termux ile telefona gelen SMS’ler okunur ve Pushbullet API aracılığıyla OTP kodları anlık bildirilir. SMS doğrulamalı işlemlerde otomasyon sağlar.

- 📁 **Dosya Yükleme Desteği**  
  Evraklar sistem üzerinden PDF/JPEG formatında yüklenebilir ve görüntülenebilir.

- 📊 **İstatistiksel Raporlama (Opsiyonel)**  
  Başvuru sayıları, vize türlerine göre dağılım ve aylık raporlar.

---

## 👤 Müşteri Portalı Özelliği

Müşteriler, kendilerine özel oluşturulan portal aracılığıyla başvuru süreçlerini takip edebilir, istenen belgeleri görebilir ve eksik evrakları öğrenebilir. Böylece firmalarla iletişim yükü azalır, süreçler daha şeffaf ve hızlı ilerler.

---

## ❓ Sık Sorulan Sorular (SSS)

**1. Bu panel hangi vize türlerini destekliyor?**  
Turistik, ticari, öğrenci, aile birleşimi, transit gibi birçok vize türü için özelleştirilebilir.

**2. Başvuruların evrak takibi nasıl yapılır?**  
Her başvuruya özel evrak listesi oluşturulur ve evraklar “eksik” veya “tamamlandı” olarak işaretlenir.

**3. Müşteri başvurusunu kendisi takip edebilir mi?**  
Evet, müşteri portalı üzerinden tüm süreçler şeffaf şekilde görüntülenebilir.

**4. OTP kodları nasıl yakalanıyor?**  
Telefon üzerindeki SMS’ler Termux ile okunur ve Pushbullet API ile anlık bildirim yapılır.

**5. MRZ okuma ne kadar güvenilir?**  
Görüntü kalitesi MRZ doğruluğunu etkiler; kaliteli fotoğraflarda yüksek doğruluk sağlar.

**6. Çoklu kullanıcı ve yetkilendirme mevcut mu?**  
Evet, farklı roller tanımlanabilir ve yetki seviyeleri ayarlanabilir.

---

## 🧱 Kullanılan Teknolojiler

- ASP.NET Core 8 (MVC)  
- Entity Framework Core  
- MSSQL Server  
- Razor View Engine  
- Bootstrap 5  
- jQuery / AJAX  
- DataTables.js  
- Azure Document Intelligence / Tesseract OCR (MRZ Okuma)  
- JWT Authentication  
- SMTP (MailKit veya System.Net.Mail)  
- Pushbullet API (OTP Bildirim)  
- Termux (SMS Yakalama)  
- LINQ  
- FluentValidation (opsiyonel)  

---

## ⚙️ Ortam Değişkenleri (Environment Variables)

| Değişken Adı             | Açıklama |
|--------------------------|----------|
| `ASPNETCORE_ENVIRONMENT` | Uygulama ortamı (Development, Production) |
| `DB_CONNECTION_STRING`   | Veritabanı bağlantı cümlesi |
| `SMTP_HOST`              | SMTP sunucu adresi |
| `SMTP_PORT`              | SMTP portu |
| `SMTP_USERNAME`          | SMTP kullanıcı adı |
| `SMTP_PASSWORD`          | SMTP şifresi |
| `JWT_SECRET_KEY`         | JWT gizli anahtarı |
| `PUSHBULLET_API_KEY`     | Pushbullet API erişim anahtarı |
| `CLIENT_PORTAL_URL`      | Müşteri portalı URL’si |
| `ADMIN_EMAIL`            | Yönetici e-posta adresi |
| `FILE_UPLOAD_PATH`       | Evrak dosya yükleme klasörü |

---

## 📄 Lisans

Bu proje [GNU General Public License v3.0 (GPL-3.0)](https://www.gnu.org/licenses/gpl-3.0.en.html) lisansı altında yayımlanmıştır. Projeyi özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz. Ancak türev çalışmalarınızda da aynı lisansın devam ettirilmesi zorunludur.

---

*İyi çalışmalar! Eğer README dosyasının diğer bölümlerinde de yardım istersen ya da örnek kod, deploy rehberi gibi ek içeriklere ihtiyaç duyarsan, söylemen yeterlidir.*

FTP Sunucusu Kontrol ve Dosya Yönetim Paneli

📖 Proje Hakkında

Bu proje, Python ve pyftpdlib kütüphanesi kullanılarak basit bir FTP sunucusu oluşturur. Kullanıcı, tanımlanan port üzerinden FTP bağlantısı kurarak dosya yükleyebilir, indirebilir ve yönetim işlemleri gerçekleştirebilir.

🚀 Özellikler

Belirlenen bir klasöre FTP erişimi sağlar.

Kullanıcı oluşturma ve yetkilendirme.

Dosya yükleme, indirme, silme, yeniden adlandırma işlemleri.

FTP dizininde dosya listeleme ve klasör oluşturma.

Basit ve anlaşılır arayüz.

🛠 Kurulum Adımları

1. Gereksinimler

Python 3.x

pyftpdlib

2. Gerekli Paketleri Yükleyin

pip install pyftpdlib

3. Proje Klasörü

Bu Python dosyasının bulunduğu dizinde otomatik olarak ftp_hedef adında bir klasör oluşturulacaktır.
Tüm FTP dosya işlemleri bu klasör içerisinde yapılacaktır.

4. Kodun Çalıştırılması

python ftp_server.py

📂 FTP Komut Satırı Kullanımı Örneği

cd ftp_client
ftp
ftp> open localhost 9000
Connected to DESKTOP-AG40JJ9.
220 pyftpdlib 2.0.1 ready.
530 Log in with USER and PASS first.
User (DESKTOP-AG40JJ9:(none)): ertan
331 Username ok, send password.
Password:
230 Login successful.

Sonrasında yapabileceğiniz işlemler:

İşlem

Komut

Örnek

Dosya listeleme

ls veya dir

ls

Dizinleri listeleme

ls veya dir

dir

Dosya indirme (okuma)

get <dosya_adı>

get ornek.txt

Dosya adını değiştirme

rename <eski_ad> <yeni_ad>

rename dosya.txt yenidosya.txt

Dosya silme

delete <dosya_adı>

delete silinecek.txt

Dizin değiştirme

cd <klasör_adı>

cd belgeler

Klasör oluşturma

mkdir <klasör_adı>

mkdir yeni_klasor

Dosya yükleme (yazma)

put <dosya_adı>

put deneme.txt

📡 FTP Bilgileri

Sunucu Adresi: 127.0.0.1 (veya ağ üzerindeki IP)

Port: 9000

Kullanıcı Adı: ertan

Şifre: 12345

FTP Klasörü: ftp_hedef

⚠️ Kullanım Notları

ftp_hedef dizini içerisinde dosya yükleyebilir, indirebilir, klasör oluşturabilir ve silebilirsiniz.

📜 Lisans

Bu proje eğitim ve kişisel kullanım amaçlı olarak paylaşılmıştır. Dilediğiniz gibi kullanabilir, geliştirebilir ve referans gösterebilirsiniz.

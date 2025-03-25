Bu proje, Python ve `pyftpdlib` kütüphanesi kullanılarak basit bir FTP sunucusu oluşturur. Kullanıcı, tanımlanan port üzerinden FTP bağlantısı kurarak dosya yükleyebilir, indirebilir ve yönetim işlemleri gerçekleştirebilir.

Belirlenen bir klasöre FTP erişimi sağlar.
Kullanıcı oluşturma ve yetkilendirme.
Dosya yükleme , indirme , silme, yeniden adlandırma işlemleri.

Kurulum Adımları

1.Gereksinimler
   - Python 3.x
   - pyftpdlib

2.Gerekli Paketleri Yükleyin
pip install pyftpdlib

3.Proje Klasörü
Bu Python dosyasının bulunduğu dizinde otomatik olarak ftp_hedef adında bir klasör oluşturulacaktır.
Tüm FTP dosya işlemleri bu klasör içerisinde yapılacaktır.

4.Kodun Çalıştırılması
python ftp_server.py


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

#sonrasında istediğiniz işlemleri komut satırı ile yapabilirsiniz

e

Dosya listeleyebilme (list)

ls veya dir

ls

l

Dizinleri listeleyebilme

ls veya dir

dir

r

Dosya okuma (read)

get <dosya_adı>

get ornek.txt

a

Dosya adını değiştirme

rename <eski_ad> <yeni_ad>

rename dosya.txt yenidosya.txt

d

Dosya silme (delete)

delete <dosya_adı>

delete silinecek.txt

f

Dizin değiştirme (change dir)

cd <klasör_adı>

cd belgeler

m

Klasör oluşturma (mkdir)

mkdir <klasör_adı>

mkdir yeni_klasor

w

Dosya yazma (write)

put <dosya_adı>

put deneme.txt





FTP Bilgileri
Sunucu Adresi: 127.0.0.1 (veya ağ üzerindeki IP)
Port:9000
Kullanıcı Adı:ertan
Şifre:12345
FTP Klasörü:ftp_hedef

Kullanım Notları
`ftp_hedef` dizini içerisinde dosya yükleyebilir, indirebilir, klasör oluşturabilir ve silebilirsiniz.




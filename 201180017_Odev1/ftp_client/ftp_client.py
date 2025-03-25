import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def ftp_calis():
    base_dir = os.path.dirname(os.path.abspath(__file__)) #python dosyası
    ftp_root = os.path.join(base_dir, "ftp_hedef")  #hedef_klasör oluşturulur
    os.makedirs(ftp_root, exist_ok=True)  
    # var mı

    authorizer = DummyAuthorizer()
    authorizer.add_user("ertan", "12345", ftp_root, perm="elradfmw") #kullanıcı izinleri
    #kullanıcı tanımlama
    #authorizer.add_anonymous(ftp_root)

    handler = FTPHandler #işlemci sınıf
    handler.authorizer = authorizer #kullanıcı yetkilendirmesini handlera aktarır

    server = FTPServer(("0.0.0.0", 9000), handler) #ftp başlat 9000 port
    server.serve_forever()


if __name__ == "__main__":
    ftp_calis()

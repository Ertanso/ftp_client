import os
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import tkinter as tk
from tkinter import messagebox, filedialog, Listbox, END, ttk, simpledialog
import shutil

class FTPServerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FTP Sunucusu Kontrol ve Dosya Yönetim Paneli")
        self.root.geometry("600x600")

        frame = ttk.Frame(root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Kullanıcı Adı:").pack(anchor="w")
        self.username_entry = ttk.Entry(frame)
        self.username_entry.pack(fill=tk.X, pady=2)

        ttk.Label(frame, text="Şifre:").pack(anchor="w")
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.pack(fill=tk.X, pady=2)

        ttk.Label(frame, text="Port:").pack(anchor="w")
        self.port_entry = ttk.Entry(frame)
        self.port_entry.insert(0, "9000")
        self.port_entry.pack(fill=tk.X, pady=2)

        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=5, fill=tk.X)

        self.start_btn = ttk.Button(button_frame, text="Sunucuyu Başlat", command=self.start_server)
        self.start_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.stop_btn = ttk.Button(button_frame, text="Sunucuyu Durdur", command=self.stop_server, state="disabled")
        self.stop_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        ttk.Label(frame, text="FTP Dizin ve Dosya Listesi:").pack(anchor="w", pady=5)
        self.file_listbox = Listbox(frame, width=60, height=18)
        self.file_listbox.pack(fill=tk.BOTH, expand=True, pady=2)

        action_frame = ttk.Frame(frame)
        action_frame.pack(pady=5, fill=tk.X)

        self.refresh_btn = ttk.Button(action_frame, text="Listeyi Yenile", command=self.refresh_file_list, state="disabled")
        self.refresh_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.upload_btn = ttk.Button(action_frame, text="Dosya Yükle", command=self.upload_file, state="disabled")
        self.upload_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.download_btn = ttk.Button(action_frame, text="Dosya İndir", command=self.download_file, state="disabled")
        self.download_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.rename_btn = ttk.Button(action_frame, text="Yeniden Adlandır", command=self.rename_file, state="disabled")
        self.rename_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        dir_action_frame = ttk.Frame(frame)
        dir_action_frame.pack(pady=5, fill=tk.X)

        self.mkdir_btn = ttk.Button(dir_action_frame, text="Dizin Oluştur", command=self.make_directory, state="disabled")
        self.mkdir_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.rmdir_btn = ttk.Button(dir_action_frame, text="Dizin/Sil", command=self.delete_selected, state="disabled")
        self.rmdir_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.server_thread = None
        self.ftp_server = None

    def run_server(self, username, password, port):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ftp_root = os.path.join(base_dir, "ftp_hedef")
        os.makedirs(self.ftp_root, exist_ok=True)

        authorizer = DummyAuthorizer()
        authorizer.add_user(username, password, self.ftp_root, perm="elradfmw")

        handler = FTPHandler
        handler.authorizer = authorizer

        self.ftp_server = FTPServer(("0.0.0.0", port), handler)
        try:
            self.ftp_server.serve_forever()
        except:
            pass

    def start_server(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            port = int(self.port_entry.get())
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir port girin!")
            return

        if not username or not password:
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş olamaz!")
            return

        self.server_thread = threading.Thread(target=self.run_server, args=(username, password, port))
        self.server_thread.daemon = True
        self.server_thread.start()

        for btn in [self.stop_btn, self.refresh_btn, self.upload_btn, self.download_btn, self.rename_btn, self.mkdir_btn, self.rmdir_btn]:
            btn.config(state="normal")
        self.start_btn.config(state="disabled")
        messagebox.showinfo("Bilgi", "FTP Sunucusu Başlatıldı.")

    def stop_server(self):
        if self.ftp_server:
            self.ftp_server.close_all()
            self.ftp_server = None
            messagebox.showinfo("Bilgi", "FTP Sunucusu Durduruldu.")

        for btn in [self.stop_btn, self.refresh_btn, self.upload_btn, self.download_btn, self.rename_btn, self.mkdir_btn, self.rmdir_btn]:
            btn.config(state="disabled")
        self.start_btn.config(state="normal")

    def refresh_file_list(self):
        self.file_listbox.delete(0, END)
        if hasattr(self, 'ftp_root') and os.path.exists(self.ftp_root):
            for item in os.listdir(self.ftp_root):
                self.file_listbox.insert(END, item)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                file_name = os.path.basename(file_path)
                target_path = os.path.join(self.ftp_root, file_name)
                shutil.copy(file_path, target_path)
                messagebox.showinfo("Başarılı", f"{file_name} başarıyla yüklendi.")
                self.refresh_file_list()
            except Exception as e:
                messagebox.showerror("Hata", f"Yükleme sırasında hata oluştu: {str(e)}")

    def download_file(self):
        selection = self.file_listbox.curselection()
        if selection:
            file_name = self.file_listbox.get(selection[0])
            src_path = os.path.join(self.ftp_root, file_name)
            target_path = filedialog.asksaveasfilename(initialfile=file_name)
            if target_path:
                shutil.copy(src_path, target_path)
                messagebox.showinfo("Bilgi", f"{file_name} başarıyla indirildi.")

    def rename_file(self):
        selection = self.file_listbox.curselection()
        if selection:
            old_name = self.file_listbox.get(selection[0])
            new_name = simpledialog.askstring("Yeniden Adlandır", f"{old_name} için yeni isim:")
            if new_name:
                os.rename(os.path.join(self.ftp_root, old_name), os.path.join(self.ftp_root, new_name))
                self.refresh_file_list()

    def make_directory(self):
        dir_name = simpledialog.askstring("Dizin Oluştur", "Yeni dizin adı:")
        if dir_name:
            os.makedirs(os.path.join(self.ftp_root, dir_name), exist_ok=True)
            self.refresh_file_list()

    def delete_selected(self):
        selection = self.file_listbox.curselection()
        if selection:
            item_name = self.file_listbox.get(selection[0])
            full_path = os.path.join(self.ftp_root, item_name)
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
            self.refresh_file_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = FTPServerUI(root)
    root.mainloop()
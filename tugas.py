import tkinter as tk
from tkinter import messagebox

# DATA KERUSAKAN & GEJALA
database_kerusakan = {
    "RAM Bermasalah": ["laptop_mati_total", "bunyi_beep", "restart_sendiri", "layar_nyala_tidak_booting"],
    "Harddisk Rusak": ["laptop_lambat", "suara_klik", "sering_blue_screen", "file_hilang"],
    "Overheating": ["laptop_mati_sendiri", "kipas_berisik", "laptop_panas", "laptop_lemot"],
    "VGA Rusak": ["layar_berkedip", "warna_luar_biasa", "layar_putih", "mati_tapi_suara_ada", "garis_vertikal"],
    "Motherboard Rusak": ["tidak_nyala_langsung", "tidak_ada_respon", "lampu_indikator_mati"]
}

# DAFTAR GEJALA (kode, pertanyaan)
semua_gejala = [
    ("laptop_mati_total", "Apakah laptop mati total dan tidak bisa menyala?"),
    ("bunyi_beep", "Apakah terdengar bunyi beep berulang?"),
    ("restart_sendiri", "Apakah laptop sering restart sendiri?"),
    ("layar_nyala_tidak_booting", "Apakah layar nyala tapi tidak masuk ke OS?"),
    ("laptop_lambat", "Apakah laptop berjalan sangat lambat?"),
    ("suara_klik", "Apakah terdengar suara klik dari dalam laptop?"),
    ("sering_blue_screen", "Apakah sering muncul Blue Screen?"),
    ("file_hilang", "Apakah file sering hilang atau corrupt?"),
    ("laptop_mati_sendiri", "Apakah laptop mati sendiri setelah digunakan?"),
    ("kipas_berisik", "Apakah kipas laptop berbunyi berisik?"),
    ("laptop_panas", "Apakah laptop terasa sangat panas?"),
    ("laptop_lemot", "Apakah laptop terasa lemot?"),
    ("layar_berkedip", "Apakah layar laptop berkedip-kedip?"),
    ("warna_luar_biasa", "Apakah warna layar terlihat aneh?"),
    ("layar_putih", "Apakah layar laptop berwarna putih?"),
    ("mati_tapi_suara_ada", "Apakah laptop mati tapi suara masih terdengar?"),
    ("garis_vertikal", "Apakah muncul garis vertikal pada layar?"),
    ("tidak_nyala_langsung", "Apakah laptop tidak langsung menyala?"),
    ("tidak_ada_respon", "Apakah laptop tidak ada respon sama sekali?"),
    ("lampu_indikator_mati", "Apakah lampu indikator laptop mati?"),
]

# SOLUSI (dipisah biar rapi)
solusi_kerusakan = {
    "RAM Bermasalah": "Bersihkan pin RAM dengan penghapus, pasang ulang RAM, atau ganti RAM baru.",
    "Harddisk Rusak": "Backup data, scan harddisk dengan CHKDSK, atau ganti dengan SSD baru.",
    "Overheating": "Bersihkan debu, ganti thermal paste, atau gunakan cooling pad.",
    "VGA Rusak": "Update driver VGA, coba monitor eksternal, atau bawa ke teknisi.",
    "Motherboard Rusak": "Cek adaptor dan baterai, atau ganti motherboard baru."
}

class AplikasiPakarSederhana:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Laptop")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        
        # Label Pertanyaan
        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar\nDiagnosa Kerusakan Laptop", 
                                    font=("Arial", 12), justify="center")
        self.label_tanya.pack(pady=30)
        
        # Tombol Mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya,
                                   bg="#4CAF50", fg="white", font=("Arial", 11), padx=20, pady=5)
        self.btn_mulai.pack(pady=10)
        
        # Frame Tombol Jawaban (disembunyikan awal)
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, 
                                command=lambda: self.jawab('y'), bg="#2196F3", fg="white")
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10,
                                   command=lambda: self.jawab('t'), bg="#f44336", fg="white")
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)
        
    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()
        
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            _, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()
            
    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()
        
    def proses_hasil(self):
        hasil = []
        for kerusakan, gejala_list in database_kerusakan.items():
            # Cek apakah semua gejala kerusakan ada di gejala_terpilih
            if all(g in self.gejala_terpilih for g in gejala_list):
                hasil.append(kerusakan)
        
        # Format hasil diagnosa
        if hasil:
            teks_hasil = ""
            for h in hasil:
                teks_hasil += f"Kerusakan: {h}\nSolusi: {solusi_kerusakan[h]}\n\n"
            messagebox.showinfo("Hasil Diagnosa", teks_hasil)
        else:
            messagebox.showinfo("Hasil Diagnosa", 
                                "Tidak terdeteksi kerusakan spesifik.\n\nSaran: Bawa ke service center untuk pengecekan lebih lanjut.")
        
        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai.\nKlik 'Mulai Diagnosa' untuk mencoba lagi.")

# Jalankan
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakarSederhana(root)
    root.mainloop()
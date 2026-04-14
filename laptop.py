import tkinter as tk
from tkinter import messagebox

# DATA KERUSAKAN & GEJALA
# Struktur: "Nama Kerusakan": ["Gejala1", "Gejala2", ...]
database_kerusakan = {
    "RAM Bermasalah": ["laptop_mati_total", "bunyi_beep_berulang", "laptop_restart_sendiri"],
    "Harddisk Rusak": ["laptop_lambat", "suara_klik_dari_laptop", "sering_blue_screen", "file_hilang_sendiri"],
    "Overheating (Panas Berlebih)": ["laptop_mati_sendiri", "kipas_berisik", "laptop_panas", "laptop_lemot"],
    "VGA Rusak": ["layar_berkedip", "warna_layar_aneh", "layar_putih", "laptop_mati_tapi_suara_ada"],
    "Motherboard Rusak": ["laptop_tidak_nyala_langsung", "tidak_ada_respon_sama_sekali", "lampu_indikator_mati"]
}

# DAFTAR SEMUA GEJALA UNTUK PERTANYAAN
semua_gejala = [
    ("laptop_mati_total", "Apakah laptop mati total dan tidak bisa menyala?"),
    ("bunyi_beep_berulang", "Apakah terdengar bunyi 'beep' berulang saat dinyalakan?"),
    ("laptop_restart_sendiri", "Apakah laptop sering restart sendiri?"),
    ("laptop_lambat", "Apakah laptop berjalan sangat lambat?"),
    ("suara_klik_dari_laptop", "Apakah terdengar suara 'klik' dari dalam laptop?"),
    ("sering_blue_screen", "Apakah sering muncul Blue Screen of Death (BSOD)?"),
    ("file_hilang_sendiri", "Apakah file-file sering hilang atau corrupt?"),
    ("laptop_mati_sendiri", "Apakah laptop mati sendiri setelah digunakan beberapa saat?"),
    ("kipas_berisik", "Apakah kipas laptop berbunyi sangat berisik?"),
    ("laptop_panas", "Apakah laptop terasa sangat panas?"),
    ("laptop_lemot", "Apakah laptop terasa lemot atau ngelag?"),
    ("layar_berkedip", "Apakah layar laptop berkedip-kedip?"),
    ("warna_layar_aneh", "Apakah warna pada layar terlihat aneh/tidak normal?"),
    ("layar_putih", "Apakah layar laptop berwarna putih?"),
    ("laptop_mati_tapi_suara_ada", "Apakah laptop mati tapi suara masih terdengar?"),
    ("laptop_tidak_nyala_langsung", "Apakah laptop tidak langsung menyala setelah ditekan tombol power?"),
    ("tidak_ada_respon_sama_sekali", "Apakah laptop tidak ada respon sama sekali saat ditekan power?"),
    ("lampu_indikator_mati", "Apakah lampu indikator laptop mati/tidak menyala?"),
]

class AplikasiPakarLaptop:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Laptop")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label Pertanyaan
        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar Diagnosa Kerusakan Laptop", font=("Arial", 12))
        self.label_tanya.pack(pady=20)

        # Tombol Mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        # Frame Tombol Jawaban (Disembunyikan di awal)
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()  # Sembunyikan tombol mulai
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == "y":
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for kerusakan, syarat in database_kerusakan.items():
            # Cek apakah gejala_terpilih mengandung semua syarat kerusakan
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(kerusakan)

        # Membuat pesan hasil diagnosa
        if hasil:
            kesimpulan = " atau ".join(hasil)
            pesan = f"Berdasarkan gejala yang Anda alami:\n\n{kesimpulan}\n\nSaran: Segera bawa laptop ke teknisi untuk diperiksa lebih lanjut."
        else:
            pesan = "Berdasarkan gejala yang Anda alami:\n\nTidak terdeteksi kerusakan spesifik.\n\nSaran: Bawa laptop ke service center untuk pengecekan lebih mendetail."
        
        messagebox.showinfo("Hasil Diagnosa", pesan)

        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")


# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("550x300")
    app = AplikasiPakarLaptop(root)
    root.mainloop()
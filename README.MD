# Sistem Pakar Diagnosa Kerusakan Laptop

**Mata Kuliah:** Praktikum Sistem Pakar  
**Pertemuan:** 4  
**NIM:** H1D024002  
**Nama:** Dera Amalia  

---

## 📋 Deskripsi Program

Program ini adalah sistem pakar berbasis **Python GUI (Tkinter)** yang dapat mendiagnosa kerusakan pada laptop berdasarkan gejala yang dipilih oleh pengguna.

Program menggunakan metode **forward chaining** dengan basis aturan yang disimpan dalam struktur data **Dictionary** (bukan if-else panjang).

---

## 🎯 Kriteria Tugas (Semua Terpenuhi)

| Kriteria | Status | Keterangan |
|----------|--------|-------------|
| Knowledge Base minimal 5 kerusakan | ✅ | RAM, Harddisk, Overheating, VGA, Motherboard |
| Mesin inferensi pakai Dictionary | ✅ | `database_kerusakan` dictionary |
| Bukan if-else panjang | ✅ | Menggunakan loop dan dictionary |
| Menangani gejala tidak cocok | ✅ | Output "Tidak terdeteksi" jika tidak ada yang cocok |
| Output nama kerusakan | ✅ | Ditampilkan di hasil diagnosa |
| Output solusi singkat | ✅ | Solusi perbaikan untuk setiap kerusakan |

---

## 🖥️ Daftar Kerusakan & Solusi

| No | Kerusakan | Solusi |
|----|-----------|--------|
| 1 | RAM Bermasalah | Bersihkan pin RAM dengan penghapus, pasang ulang, atau ganti RAM baru |
| 2 | Harddisk Rusak | Backup data, scan CHKDSK, atau ganti SSD baru |
| 3 | Overheating | Bersihkan debu, ganti thermal paste, atau pakai cooling pad |
| 4 | VGA Rusak | Update driver, coba monitor eksternal, atau bawa ke teknisi |
| 5 | Motherboard Rusak | Cek adaptor & baterai, atau ganti motherboard baru |

---

## 🚀 Cara Menjalankan Program

### Prasyarat
- Python 3.6 atau lebih baru
- Tkinter (biasanya sudah termasuk bawaan Python)

### Langkah-langkah

1. **Clone atau download repositori ini**
   ```bash
   git clone https://github.com/deraaml25/H1D024002-PraktikumKB-Pertemuan4.git
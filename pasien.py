# Percobaan 3

# Working Memory
gejala_pasien = []

def tanya_gejala(kode_gejala, teks_pertanyaan):
    # Menampilkan pertanyaan (Simulasi predikat pertanyaan/1 di Prolog)
    jawaban = input(f"{teks_pertanyaan} (y/t): ").lower()

    # Jika jawaban 'y', masukkan ke dalam list gejala (Simulasi assertz)
    if jawaban == 'y':
        gejala_pasien.append(kode_gejala)

def jalankan_diagnosa():
    print("\n--- Hasil Analisis Sistem ---")

    # Logika pencocokan (Sama seperti predikat penyakit/1 di Prolog)
    terdeteksi = False

    # Check Malaria Tertiana
    if "nyeri_otot" in gejala_pasien and "muntah" in gejala_pasien and "kejang" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Tertiana")
        terdeteksi = True

    # Check Malaria Quartana
    if "nyeri_otot" in gejala_pasien and "menggigil" in gejala_pasien and "tidak_enak_badan" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Quartana")
        terdeteksi = True

    # Check Malaria Tropika
    if "keringat_dingin" in gejala_pasien and "sakit_kepala" in gejala_pasien and "mimisan" in gejala_pasien and "mual" in gejala_pasien:
        print(">> Anda terdeteksi: Malaria Tropika")
        terdeteksi = True

    if not terdeteksi:
        print(">> Tidak terdeteksi penyakit malaria berdasarkan gejala yang Anda masukkan.")

def main():
    print("=== SISTEM PAKAR DIAGNOSA MALARIA ===")
    print("Jawablah pertanyaan berikut dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

    # Daftar pertanyaan yang akan diajukan (Simulasi predikat pertanyaan/1)
    tanya_gejala("nyeri_otot", "Apakah Anda merasa nyeri otot?")
    tanya_gejala("muntah", "Apakah Anda muntah-muntah?")
    tanya_gejala("kejang", "Apakah Anda mengalami kejang-kejang?")
    tanya_gejala("menggigil", "Apakah Anda sering menggigil?")
    tanya_gejala("tidak_enak_badan", "Apakah Anda merasa tidak enak badan?")
    tanya_gejala("demam", "Apakah Anda mengalami demam?")

    # Jalankan diagnosa setelah semua pertanyaan dijawab
    jalankan_diagnosa()

# Menjalankan program
if __name__ == "__main__":
    main()
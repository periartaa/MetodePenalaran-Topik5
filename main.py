basis_kasus = {
    "Pullorum (Feses Kapur )": {
        "gejala": ["Encer putih seperti kapur", "Sesak nafas", "Nafsu makan menurun", "Lesu"],
        "penanganan": "Menjaga kebersihan sanitasi kandang dan meningkatkan biosecurity."
    },
    "Chronic Respiratory Disease (Ngorok)": {
        "gejala": ["Ngorok, Sesak nafas", "Nafsu makan normal", "Cairan dari hidung"],
        "penanganan": "Isolasi ayam sakit, pemberian antibiotik, dan peningkatan ventilasi kandang."
    },
    "Kolibasilosis": {
        "gejala": ["Kusam", "Diare", "Nafsu makan normal", "Lemas", "Cairan lengket sekitas anus"],
        "penanganan": "Pemberian probiotik dan antibiotik, sanitasi kandang."
    },
    "Infectious Coryza": {
        "gejala": ["Diare", "Bersin", "Nafsu makan normal", "Air mata", "Cairan dari hidung", "Pembengkakan anus"],
        "penanganan": "Pemberian antibiotik dan vitamin, isolasi ayam sakit."
    },
    "Newcastle Disease (Tetelo)": {
        "gejala": ["Encer putih seperti kapur", "Batuk", "Sesak nafas", "Nafsu makan menurun", "Lemas", "Leher Bengkok"],
        "penanganan": "Vaksinasi, isolasi ayam sakit, dan peningkatan sanitasi."
    },
    "Infectious Bursal Disease (Gumboro)": {
        "gejala": ["Diare putih", "Nafsu makan menurun", "Stress", "Kematian mendedak"],
        "penanganan": "Vaksinasi, pemberian elektrolit, dan sanitasi kandang."
    },
    "Avian Influenza (Flu Burung )": {
        "gejala": ["Diare", "Ngorok", "Nafsu makan menuurun", "Cairan dari hidung dan mata", "Kulit ungun", "Kematian mendadak"],
        "penanganan": "Pelaporan ke otoritas kesehatan hewan, isolasi ketat, dan pemusnahan ayam terinfeksi."
    },
    "Dehidrasi": {
        "gejala": ["Nafsu makan normal", "Kaki merah, Kering", "Dehidrasi"],
        "penanganan": "Pemberian air bersih dan elektrolit."
    },
    "Omphalitis": {
        "gejala": ["Feses berbau busuk", "Nafsu makan menurun", "Kematian mendadak", "Kotoran basah"],
        "penanganan": "Sanitasi kandang, pemberian antibiotik, dan perawatan pusar."
    },
    "Coccidiosis(Diare berdarah)": {
        "gejala": ["Diare bedarah", "Nafsu makan Normal", "Kematian mendadak"],
        "penanganan": "Pemberian obat anticoccidial, sanitasi kandang, dan pencegahan kelembaban tinggi."
    }
}

# Fungsi Koefisien Dice
def koefisien_dice(kasus_baru, kasus_lama):
    # Hitung intersection (gejala yang sama)
    intersection = len(set(kasus_baru) & set(kasus_lama))
    # Hitung total gejala unik
    total = len(set(kasus_baru)) + len(set(kasus_lama))
    # Rumus Dice: (2 * intersection) / total
    similarity = (2 * intersection) / total if total != 0 else 0
    return similarity

# Input gejala kasus baru dari pengguna
print("=== Masukkan Gejala Kasus Baru ===")
print("Daftar gejala yang dikenal sistem:")
semua_gejala = set()
for penyakit in basis_kasus.values():
    semua_gejala.update(gejala for gejala in penyakit["gejala"])
print(", ".join(semua_gejala) + "\n")

kasus_baru = input("Masukkan gejala (pisahkan dengan koma): ").strip().split(",")
kasus_baru = [gejala.strip() for gejala in kasus_baru if gejala.strip()]


# Perhitungan Similarity dengan Semua Kasus
hasil_similarity = {}
for nama_penyakit, data in basis_kasus.items():
    similarity = koefisien_dice(kasus_baru, data["gejala"])
    hasil_similarity[nama_penyakit] = similarity

# Urutkan dari similarity tertinggi
hasil_terurut = sorted(hasil_similarity.items(), key=lambda x: x[1], reverse=True)

print("=== Hasil Perhitungan Similarity (Koefisien Dice) ===")
for penyakit, nilai in hasil_terurut:
    print(f"{penyakit}: {nilai:.2f}")

# Ambil rekomendasi tertinggi
penyakit_tertinggi, similarity_tertinggi = hasil_terurut[0]
print("\n=== HASIL ===")
print(f"Rekomendasi: {penyakit_tertinggi} (Similarity: {similarity_tertinggi:.2f})")
print(f"Penanganan: {basis_kasus[penyakit_tertinggi]['penanganan']}")
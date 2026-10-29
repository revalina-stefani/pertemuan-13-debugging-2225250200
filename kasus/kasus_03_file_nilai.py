
def baca_nilai(nama_file):
    nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue

                try:
                    angka = float(baris)
                except ValueError:
                    print("Data tidak valid:", baris)
                    continue

                if 0 <= angka <= 100:
                    nilai.append(angka)
                else:
                    print("Nilai di luar batas:", angka)

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []

    return nilai


data = baca_nilai("nilai.txt")
print("Data nilai:", data)

if data:
    print("Rata-rata:", sum(data) / len(data))
else:
    print("Tidak ada nilai valid.")

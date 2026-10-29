
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return None
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


def jalankan_test():
    tests = [
        ("T1", hitung_rata_rata([80, 60, 90, 70]), 75.0),
        ("T2", hitung_rata_rata([100, 80]), 90.0),
        ("T3", status(60), "Lulus"),
        ("T4", status(59), "Tidak lulus"),
        ("T5", nilai_tertinggi([80, 60, 90, 70]), 90),
    ]

    for test_id, actual, expected in tests:
        hasil = "PASS" if actual == expected else "FAIL"
        print(
            f"{test_id}: Expected={expected}, "
            f"Actual={actual}, Status={hasil}"
        )


if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))
    print("\nHasil pengujian:")
    jalankan_test()


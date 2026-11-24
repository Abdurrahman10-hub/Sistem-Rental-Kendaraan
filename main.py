"""Aplikasi konsol sederhana untuk menyewakan kendaraan."""


class Kendaraan:
    """Mewakili kendaraan yang dapat disewakan."""

    def __init__(self, nama, jenis, tarif_per_hari):
        self.__nama = nama
        self.__jenis = jenis
        self.tarif_per_hari = tarif_per_hari
        self.__tersedia = True

    @property
    def nama(self):
        return self.__nama

    @property
    def jenis(self):
        return self.__jenis

    @property
    def tarif_per_hari(self):
        return self.__tarif_per_hari

    @tarif_per_hari.setter
    def tarif_per_hari(self, nilai):
        if not isinstance(nilai, (int, float)) or isinstance(nilai, bool) or nilai <= 0:
            raise ValueError("Tarif per hari harus berupa angka lebih dari 0.")
        self.__tarif_per_hari = nilai

    @property
    def tersedia(self):
        return self.__tersedia

    def sewakan(self):
        if not self.__tersedia:
            raise ValueError("Kendaraan sedang disewa.")
        self.__tersedia = False

    def kembalikan(self):
        if self.__tersedia:
            raise ValueError("Kendaraan ini tidak sedang disewa.")
        self.__tersedia = True

    @staticmethod
    def validasi_durasi(hari):
        """Memastikan durasi sewa berupa bilangan bulat positif."""
        if not isinstance(hari, int) or isinstance(hari, bool) or hari <= 0:
            raise ValueError("Durasi sewa harus berupa bilangan bulat lebih dari 0.")


class SistemRental:
    """Mengelola daftar kendaraan dan transaksi rental."""

    def __init__(self, kendaraan=None):
        self.__kendaraan = list(kendaraan) if kendaraan is not None else []
        self.__kendaraan_disewa = {}

    @classmethod
    def dengan_data_contoh(cls):
        """Membuat sistem rental yang sudah berisi kendaraan contoh."""
        kendaraan = [
            Kendaraan("Toyota Avanza", "Mobil", 350000),
            Kendaraan("Honda Vario", "Motor", 100000),
            Kendaraan("Mitsubishi Xpander", "Mobil", 450000),
        ]
        return cls(kendaraan)

    @staticmethod
    def hitung_total(tarif_per_hari, hari):
        Kendaraan.validasi_durasi(hari)
        if not isinstance(tarif_per_hari, (int, float)) or tarif_per_hari <= 0:
            raise ValueError("Tarif per hari harus lebih dari 0.")
        return tarif_per_hari * hari

    def tampilkan_kendaraan(self):
        print("\nDaftar Kendaraan:")
        for nomor, kendaraan in enumerate(self.__kendaraan, start=1):
            status = "Tersedia" if kendaraan.tersedia else "Sedang disewa"
            print(
                f"{nomor}. {kendaraan.nama} ({kendaraan.jenis})"
                f" - Rp{kendaraan.tarif_per_hari:,.0f}/hari - {status}"
            )

    def sewa_kendaraan(self, nomor, hari):
        Kendaraan.validasi_durasi(hari)
        if nomor < 1 or nomor > len(self.__kendaraan):
            raise ValueError("Nomor kendaraan tidak ditemukan.")

        kendaraan = self.__kendaraan[nomor - 1]
        kendaraan.sewakan()
        total = self.hitung_total(kendaraan.tarif_per_hari, hari)
        self.__kendaraan_disewa[nomor - 1] = kendaraan
        return kendaraan, total

    def kembalikan_kendaraan(self, nomor):
        if nomor < 1 or nomor > len(self.__kendaraan):
            raise ValueError("Nomor kendaraan tidak ditemukan.")
        if nomor - 1 not in self.__kendaraan_disewa:
            raise ValueError("Kendaraan tersebut tidak sedang disewa.")

        kendaraan = self.__kendaraan_disewa.pop(nomor - 1)
        kendaraan.kembalikan()
        return kendaraan


def main():
    sistem = SistemRental.dengan_data_contoh()
    print("=== Sistem Rental Kendaraan ===")

    while True:
        print("\n1. Lihat kendaraan")
        print("2. Sewa kendaraan")
        print("3. Kembalikan kendaraan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                sistem.tampilkan_kendaraan()
            elif pilihan == "2":
                sistem.tampilkan_kendaraan()
                nomor = int(input("Masukkan nomor kendaraan: "))
                hari = int(input("Lama sewa (hari): "))
                kendaraan, total = sistem.sewa_kendaraan(nomor, hari)
                print(f"{kendaraan.nama} berhasil disewa.")
                print(f"Total biaya: Rp{total:,.0f}")
            elif pilihan == "3":
                nomor = int(input("Nomor kendaraan yang dikembalikan: "))
                kendaraan = sistem.kembalikan_kendaraan(nomor)
                print(f"{kendaraan.nama} berhasil dikembalikan.")
            elif pilihan == "4":
                print("Terima kasih telah menggunakan Sistem Rental.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu 1 sampai 4.")
        except ValueError as error:
            print(f"Transaksi tidak dapat diproses: {error}")


if __name__ == "__main__":
    main()

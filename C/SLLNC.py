class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_mahasiswa(self, nim, nama):
        new_mahasiswa = Node(nim, nama)
        if self.head is None:
            self.head = new_mahasiswa
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_mahasiswa

    def tampilkan_mahasiswa(self):
        if self.head is None:
            print("Linked List Kosong.")
        else:
            temp = self.head
            while temp is not None:
                print(f"NIM: {temp.nim}, Nama: {temp.nama}")
                temp = temp.next

    def hapus_mahasiswa(self, nim):
        if self.head is None:
            print("Linked List Kosong.")
            return

        if self.head.nim == nim:
            self.head = self.head.next
            print(f"Mahasiswa dengan NIM {nim} berhasil dihapus.")
            return

        temp = self.head
        while temp.next is not None and temp.next.nim != nim:
            temp = temp.next

        if temp.next is None:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        else:
            temp.next = temp.next.next
            print(f"Mahasiswa dengan NIM {nim} berhasil dihapus.")

    def ubah_data_mahasiswa(self, nim):
        if self.head is None:
            print("Linked List Kosong.")
            return

        temp = self.head
        while temp is not None and temp.nim != nim:
            temp = temp.next

        if temp is None:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        else:
            print(f"Nama saat ini: {temp.nama}")
            new_nama = input("Masukkan nama baru: ")
            temp.nama = new_nama
            print("Data mahasiswa berhasil diubah.")


def main():
    daftar_mahasiswa = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("0. Keluar")

        pilihan = input("Pilihan Anda: ")

        if pilihan == '1':
            nim = input("Masukkan NIM mahasiswa: ")
            nama = input("Masukkan nama mahasiswa: ")
            daftar_mahasiswa.tambah_mahasiswa(nim, nama)
        elif pilihan == '2':
            print("\nDaftar Mahasiswa:")
            daftar_mahasiswa.tampilkan_mahasiswa()
        elif pilihan == '3':
            nim_hapus = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            daftar_mahasiswa.hapus_mahasiswa(nim_hapus)
        elif pilihan == '4':
            nim_ubah = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            daftar_mahasiswa.ubah_data_mahasiswa(nim_ubah)
        elif pilihan == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struktur untuk merepresentasikan Mahasiswa
struct Mahasiswa {
    char nim[20];
    char nama[50];
    struct Mahasiswa* next;
};

// Struktur untuk merepresentasikan Linked List
struct LinkedList {
    struct Mahasiswa* head;
};

// Fungsi untuk membuat Mahasiswa baru
struct Mahasiswa* createMahasiswa(const char* nim, const char* nama) {
    struct Mahasiswa* newMahasiswa = (struct Mahasiswa*)malloc(sizeof(struct Mahasiswa));
    snprintf(newMahasiswa->nim, sizeof(newMahasiswa->nim), "%s", nim);
    snprintf(newMahasiswa->nama, sizeof(newMahasiswa->nama), "%s", nama);
    newMahasiswa->next = NULL;
    return newMahasiswa;
}

// Fungsi untuk menambahkan Mahasiswa ke Linked List Non-Circular
void tambahMahasiswa(struct LinkedList* list, const char* nim, const char* nama) {
    struct Mahasiswa* newMahasiswa = createMahasiswa(nim, nama);

    if (list->head == NULL) {
        list->head = newMahasiswa;
    } else {
        struct Mahasiswa* temp = list->head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newMahasiswa;
    }
}

// Fungsi untuk menampilkan semua Mahasiswa dalam Linked List
void tampilkanMahasiswa(struct LinkedList* list) {
    if (list->head == NULL) {
        printf("Linked List Kosong.\n");
        return;
    }

    struct Mahasiswa* temp = list->head;
    while (temp != NULL) {
        printf("NIM: %s, Nama: %s\n", temp->nim, temp->nama);
        temp = temp->next;
    }
}

// Fungsi untuk menghapus Mahasiswa dari Linked List berdasarkan NIM
void hapusMahasiswa(struct LinkedList* list, const char* nim) {
    if (list->head == NULL) {
        printf("Linked List Kosong. Tidak dapat menghapus.\n");
        return;
    }

    struct Mahasiswa* temp = list->head;
    struct Mahasiswa* prev = NULL;

    while (temp != NULL && strcmp(temp->nim, nim) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
        return;
    }

    if (prev == NULL) {
        // Mahasiswa yang dihapus adalah elemen pertama
        list->head = temp->next;
    } else {
        // Mahasiswa yang dihapus berada di tengah atau akhir
        prev->next = temp->next;
    }

    free(temp);
    printf("Mahasiswa dengan NIM %s berhasil dihapus.\n", nim);
}

// Fungsi untuk merubah data mahasiswa secara manual
void ubahData(struct LinkedList* list, const char* nim) {
    struct Mahasiswa* temp = list->head;

    while (temp != NULL && strcmp(temp->nim, nim) != 0) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
        return;
    }

    // Mahasiswa ditemukan, izinkan pengguna untuk merubah nama
    printf("Nama saat ini: %s\n", temp->nama);
    printf("Masukkan nama baru: ");
    scanf(" %[^\n]s", temp->nama);
    printf("Data mahasiswa berhasil diubah.\n");
}

// Fungsi utama
int main() {
    struct LinkedList daftarMahasiswa = {NULL};
    int pilihan;
    char nim[20], nama[50];

    do {
        printf("\nMenu:\n");
        printf("1. Tambah Mahasiswa\n");
        printf("2. Tampilkan Mahasiswa\n");
        printf("3. Hapus Mahasiswa\n");
        printf("4. Ubah Data Mahasiswa\n");
        printf("0. Keluar\n");
        printf("Pilihan Anda: ");
        scanf("%d", &pilihan);

        switch (pilihan) {
            case 1:
                printf("Masukkan NIM mahasiswa: ");
                scanf("%s", nim);

                printf("Masukkan Nama mahasiswa: ");
                scanf(" %[^\n]s", nama);

                tambahMahasiswa(&daftarMahasiswa, nim, nama);
                break;

            case 2:
                printf("\nDaftar Mahasiswa:\n");
                tampilkanMahasiswa(&daftarMahasiswa);
                break;

            case 3:
                printf("Masukkan NIM mahasiswa yang ingin dihapus: ");
                scanf("%s", nim);
                hapusMahasiswa(&daftarMahasiswa, nim);
                break;

            case 4:
                printf("Masukkan NIM mahasiswa yang ingin diubah: ");
                scanf("%s", nim);
                ubahData(&daftarMahasiswa, nim);
                break;

            case 0:
                printf("Program selesai.\n");
                break;

            default:
                printf("Pilihan tidak valid. Silakan coba lagi.\n");
        }
    } while (pilihan != 0);

    // Membersihkan memori sebelum keluar dari program
    struct Mahasiswa* temp = daftarMahasiswa.head;
    while (temp != NULL) {
        struct Mahasiswa* next = temp->next;
        free(temp);
        temp = next;
    }

    return 0;
}

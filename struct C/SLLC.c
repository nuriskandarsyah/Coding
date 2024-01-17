#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struktur untuk mendeklarasikan Mahasiswa
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
void tambahMahasiswa(struct LinkedList* list, char nim[], char nama[]) {
    struct Mahasiswa* newMahasiswa = (struct Mahasiswa*)malloc(sizeof(struct Mahasiswa));
    snprintf(newMahasiswa->nim, sizeof(newMahasiswa->nim), "%s", nim);
    snprintf(newMahasiswa->nama, sizeof(newMahasiswa->nama), "%s", nama);

    if (list->head == NULL) {
        list->head = newMahasiswa;
        newMahasiswa->next = list->head;
    } else {
        struct Mahasiswa* temp = list->head;
        while (temp->next != list->head) {
            temp = temp->next;
        }
        temp->next = newMahasiswa;
        newMahasiswa->next = list->head;
    }
}

// Fungsi untuk menampilkan data Mahasiswa
void tampilkanMahasiswa(struct LinkedList* list) {
    if (list->head == NULL) {
        printf("Linked List Kosong.\n");
        return;
    }

    struct Mahasiswa* temp = list->head;
    do {
        printf("NIM: %s, Nama: %s\n", temp->nim, temp->nama);
        temp = temp->next;
    } while (temp != list->head);
}

// Fungsi untuk menghapus data mahasiswa secara manual
void hapusMahasiswa(struct LinkedList* list, char nim[]) {
    if (list->head == NULL) {
        printf("Linked List Kosong.\n");
        return;
    }

    struct Mahasiswa* current = list->head;
    struct Mahasiswa* previous = NULL;

    do {
        if (strcmp(current->nim, nim) == 0) {
            if (current == list->head) {
                if (current->next == list->head) {
                    // Hapus satu-satunya elemen dalam linked list
                    free(current);
                    list->head = NULL;
                    printf("Mahasiswa dengan NIM %s berhasil dihapus.\n", nim);
                    return;
                } else {
                    // Hapus elemen pertama dalam linked list dengan lebih dari satu elemen
                    struct Mahasiswa* last = list->head;
                    while (last->next != list->head) {
                        last = last->next;
                    }
                    last->next = current->next;
                    list->head = current->next;
                    free(current);
                    printf("Mahasiswa dengan NIM %s berhasil dihapus.\n", nim);
                    return;
                }
            } else {
                previous->next = current->next;
                free(current);
                printf("Mahasiswa dengan NIM %s berhasil dihapus.\n", nim);
                return;
            }
        }
        previous = current;
        current = current->next;
    } while (current != list->head);

    printf("Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
}

// Fungsi untuk merubah data mahasiswa secara manual
void ubahData(struct LinkedList* list, char nim[]) {
    if (list->head == NULL) {
        printf("Linked List Kosong.\n");
        return;
    }

    // Mahasiswa ditemukan, izinkan pengguna untuk merubah nama
    struct Mahasiswa* temp = list->head;
    do {
        if (strcmp(temp->nim, nim) == 0) {
            printf("Nama saat ini: %s\n", temp->nama);
            printf("Masukkan nama baru: ");
            scanf(" %[^\n]s", temp->nama);
            printf("Data mahasiswa berhasil diubah.\n");
            return;
        }
        temp = temp->next;
    } while (temp != list->head);

    printf("Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
}

// Tampilan utama program
int main() {
    struct LinkedList daftarMahasiswa = {NULL};
    int pilihan, jumlahMahasiswa;
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
                printf("\nMasukkan jumlah mahasiswa: ");
                scanf("%d", &jumlahMahasiswa);

                for (int i = 0; i < jumlahMahasiswa; ++i) {
                    printf("Masukkan NIM mahasiswa %d: ", i + 1);
                    scanf("%s", nim);

                    printf("Masukkan Nama mahasiswa %d: ", i + 1);
                    scanf(" %[^\n]s", nama);

                    tambahMahasiswa(&daftarMahasiswa, nim, nama);
                }
                break;

            case 2:
                printf("\nDaftar Mahasiswa:\n");
                tampilkanMahasiswa(&daftarMahasiswa);
                break;

            case 3:
                printf("\nMasukkan NIM mahasiswa yang ingin dihapus: ");
                scanf("%s", nim);
                hapusMahasiswa(&daftarMahasiswa, nim);
                break;

            case 4:
                printf("\nMasukkan NIM mahasiswa yang ingin diubah: ");
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

    return 0;
}
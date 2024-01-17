#include <stdio.h>

int main() {
    char nama[100];
    printf("Masukkan nama Anda: ");
    fgets(nama, sizeof(nama), stdin);

    printf("Hello %s", nama);

    int pilihan[5];
    int harga[] = {500000, 1000000, 1500000, 2000000, 2500000};
    char kursus[][30] = {"Algoritma dan Pemrograman", "Database System", "Computer Network", "OOP", "Android"};
    int totalBiaya = 0;

    printf("\nList program pembelajaran yang tersedia [1 untuk ambil / 0 untuk tidak]:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d. %s (Rp. %d) : ", i + 1, kursus[i], harga[i]);
        scanf("%d", &pilihan[i]);
        if (pilihan[i] == 1) {
            totalBiaya += harga[i];
        }
    }

    printf("\nTotal biaya kursus: Rp. %d\n", totalBiaya);

    return 0;
}

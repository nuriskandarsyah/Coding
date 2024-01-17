#include <stdio.h>
#include <stdbool.h>

// Fungsi untuk memeriksa apakah suatu bilangan adalah bilangan prima atau bukan
bool isPrime(int number) {
    if (number <= 1) {
        return false;
    }

    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false;
        }
    }

    return true;
}

// Fungsi untuk menampilkan semua bilangan prima dalam suatu range
void displayPrimesInRange(int start, int end) {
    printf("Bilangan prima antara %d dan %d adalah:\n", start, end);

    for (int i = start; i <= end; i++) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }

    printf("\n");
}

int main() {
    int bilangan;

    // Menggunakan fungsi pemeriksa bilangan prima
    printf("Masukkan suatu bilangan untuk diperiksa apakah bilangan prima atau bukan: ");
    scanf("%d", &bilangan);

    if (isPrime(bilangan)) {
        printf("%d adalah bilangan prima.\n", bilangan);
    } else {
        printf("%d bukan bilangan prima.\n", bilangan);
    }

    // Menggunakan fungsi penampil bilangan prima dalam suatu range
    int rangeStart, rangeEnd;
    printf("Masukkan batas awal range: ");
    scanf("%d", &rangeStart);
    printf("Masukkan batas akhir range: ");
    scanf("%d", &rangeEnd);

    displayPrimesInRange(rangeStart, rangeEnd);

    return 0;
}

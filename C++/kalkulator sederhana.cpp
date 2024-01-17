#include <stdio.h>
#include <string.h>

int main() {
    int angka1, angka2;
    char op;
    int hasil;
    char loop[5];

    printf("Masukkan angka pertama: ");
    scanf("%d", &angka1);

    printf("Masukkan operator (+, -, *, /): ");
    scanf(" %c", &op);

    printf("Masukkan angka kedua: ");
    scanf("%d", &angka2);

    do {
            switch (op) {
        case '+':
            hasil = angka1 + angka2;
            printf("Hasil penjumlahan: %d\n", hasil);
            break;
        case '-':
            hasil = angka1 - angka2;
            printf("Hasil pengurangan: %d\n", hasil);
            break;
        case '*':
            hasil = angka1 * angka2;
            printf("Hasil perkalian: %d\n", hasil);
            break;1
        case '/':
            if (angka2 != 0) {
                hasil = angka1 / angka2;
                printf("Hasil pembagian: %d\n", hasil);
            } else {
                printf("Pembagian dengan nol tidak valid.\n");
            }
            break;
        default:
            printf("Operator tidak valid.\n");
            break;
    }

        printf("Apakah Anda ingin melakukan perhitungan lagi? (ya/tidak): ");
        scanf("%s", loop);
    } while (strcmp(loop, "ya") == 0);
    

    return 0;
}

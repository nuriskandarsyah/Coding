#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100
#define MAX_DATA 100

typedef struct {
    int no;
    char nomhs[MAX_LENGTH];
    char nama[MAX_LENGTH];
    int nilai;
    char huruf;
} Mahasiswa;

void bubbleSort(Mahasiswa data[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (data[j].no > data[j + 1].no) {
                Mahasiswa temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            }
        }
    }
}

void printData(Mahasiswa data[], int n) {
    printf("=======================================\n");
    printf("No\tNomhs\t\tN a m a\t\tNilai\tHURUF\n");
    printf("---------------------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%s\t\t%s\t\t%d\t%c\n", data[i].no, data[i].nomhs, data[i].nama, data[i].nilai, data[i].huruf);
    }
    printf("=======================================\n");
}

int main() {
    FILE *file;
    char filename[MAX_LENGTH];
    char line[MAX_LENGTH];
    int count = 0;
    Mahasiswa data[MAX_DATA];

    printf("Masukkan nama file: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Gagal membuka file.\n");
        return 1;
    }

    // Membaca data dari file
    while (fgets(line, sizeof(line), file)) {
        sscanf(line, "%d %s %s %d %c", &data[count].no, data[count].nomhs, data[count].nama, &data[count].nilai, &data[count].huruf);
        count++;
    }
    fclose(file);

    // Mengurutkan data menggunakan bubble sort
    bubbleSort(data, count);

    // Menampilkan data sebelum disortir
    printf("Data sebelum disortir:\n");
    printData(data, count);

    // Menampilkan data setelah disortir
    printf("Data setelah disortir:\n");
    printData(data, count);

    return 0;
}
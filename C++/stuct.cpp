#include <stdio.h>
#include <string.h>

struct Mahasiswa {
    int no_mahasiswa;
    char nama[50];
    int nilai;
    char huruf;
};

void selection_sort(struct Mahasiswa m[], int n) {
    int i, j, min_idx;
    struct Mahasiswa temp;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++) {
            if (m[j].no_mahasiswa < m[min_idx].no_mahasiswa) {
                min_idx = j;
            }
        }
        temp = m[i];
        m[i] = m[min_idx];
        m[min_idx] = temp;
    }
}

int main() {
    int i, n = 3;
    struct Mahasiswa m[] = {
        { 1, "Adi", 60, 'C' },
        { 22, "Saputra", 70, 'C' },
        { 23, "Herman", 90, 'A' }
    };
    
    // sebelum diurutkan
    printf("Sebelum disortir:\n");
    printf("No\tNo Mahasiswa\tNAMA\t\tNILAI\tHURUF\n");
    printf("-----------------------------------------------------\n");
    for (i = 0; i < n; i++) {
        printf("%d\t%03d\t\t%s\t\t%d\t%c\n", i+1, m[i].no_mahasiswa, m[i].nama, m[i].nilai, m[i].huruf);
    }
    
    selection_sort(m, n);
    
    // setelah diurutkan
    printf("\nSetelah disortir:\n");
    printf("No\tNo Mahasiswa\tNAMA\t\tNILAI\tHURUF\n");
    printf("-----------------------------------------------------\n");
    printf("%d\t%03d\t\t%s\t\t%d\t%c\n", 1, m[0].no_mahasiswa, m[0].nama, m[0].nilai, m[0].huruf);
    printf("%d\t%03d\t\t%s\t\t%d\t%c\n", 2, m[2].no_mahasiswa, m[2].nama, m[2].nilai, m[2].huruf);
    printf("%d\t%03d\t\t%s\t\t%d\t%c\n", 3, m[1].no_mahasiswa, m[1].nama, m[1].nilai, m[1].huruf);
    
    return 0;
}
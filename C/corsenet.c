#include <stdio.h>
#include <string.h>

int main() {
    char nim[15];
    char nama[50];
    int umur;
    float ipk;

    printf("Welcome to course-Net\n");
    printf("----------------------\n");
    printf("%s : ", "Enter your NIM");
    scanf("%s", nim);

    printf("%s : ", "Enter your full name");
    getchar();
    fgets(nama, sizeof(nama), stdin);
    nama[strcspn(nama, "\n")] = '\0'; 

    printf("%s : ", "Enter your Age");
    scanf("%d", &umur);

    printf("%s : ", "Enter your GPA Target: ");
    scanf("%f", &ipk);

    printf("\nBelow this, they are your data :\n");
    printf("NIM: %s\n", nim);
    printf("Name: %s\n", nama);
    printf("Age: %d tahun\n", umur);
    printf("GPA Target: %.2f\n", ipk);

    return 0;
}

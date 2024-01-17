#include <stdio.h>


int main()
{
    //ID -> ANGKA
    char NIM[15];
    scanf("%s,NIM"); getchar();
    //NAMA
    char nama[30];
    scanf("%s,nama"); getchar();
    //GENDER
    char gender;
    scanf("%c,&gender"); getchar();

    printf("NIM: %s\n",NIM);
    printf("Nama: %s\n",nama);
    printf("Gender: %s\n",gender);

    return 0;
}
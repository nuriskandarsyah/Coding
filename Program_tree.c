#include <stdio.h>
#include <stdlib.h>

// Kelompok 7
// Mata Kuliah : Struktur Data dan Algoritma
// Nur Iskandar S 220511009
// Adi Bachtiar 220511173
// Misnen 220510002
// Agung Putra Laksono 220510009
// Muhamad Rizki 220510008

//Struct Untuk Mendeklarasikan Node
struct TreeNode {
    char data[100];
    struct TreeNode* children[100];
    int child_count;
};

//Struct Untuk Menambahkan Node
struct TreeNode* create_node(char data[]) {
    struct TreeNode* new_node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    if (new_node != NULL) {
        strcpy(new_node->data, data);
        new_node->child_count = 0;
    }
    return new_node;
}

//Fungsi Untuk Menambahkan Node
void add_node(struct TreeNode* parent, char data[]) {
    struct TreeNode* new_node = create_node(data);
    if (new_node != NULL) {
        parent->children[parent->child_count++] = new_node;
    }
}

//Fungsi Untuk Melihat Node
void display_tree(struct TreeNode* node, int level) {
    if (node != NULL) {
        for (int i = 0; i < level; i++) {
            printf("  ");
        }
        printf("%s\n", node->data);
        for (int i = 0; i < node->child_count; i++) {
            display_tree(node->children[i], level + 1);
        }
    }
}

//Fungsi Untuk Menghapus Node
int delete_node(struct TreeNode* parent, char target_data[]) {
    for (int i = 0; i < parent->child_count; i++) {
        if (strcmp(parent->children[i]->data, target_data) == 0) {
            free(parent->children[i]);
            for (int j = i; j < parent->child_count - 1; j++) {
                parent->children[j] = parent->children[j + 1];
            }
            parent->child_count--;
            return 1;
        }
        if (delete_node(parent->children[i], target_data)) {
            return 1;
        }
    }
    return 0;
}

struct TreeNode* find_node(struct TreeNode* node, char target_data[]) {
    if (strcmp(node->data, target_data) == 0) {
        return node;
    }

    for (int i = 0; i < node->child_count; i++) {
        struct TreeNode* result = find_node(node->children[i], target_data);
        if (result != NULL) {
            return result;
        }
    }

    return NULL;
}

//Fungsi Untuk Menambahkan Tree
struct TreeNode* add_parent(struct TreeNode* root, char data[]) {
    struct TreeNode* new_parent = create_node(data);
    if (new_parent != NULL) {
        new_parent->children[0] = root;
        new_parent->child_count = 1;
    }
    return new_parent;
}

//Menu Utama
int main() {
    struct TreeNode* root = create_node("Root");

    while (1) {
        printf("\nMenu:\n");
        printf("1. Tambah Node\n");
        printf("2. Lihat Node\n");
        printf("3. Hapus Node\n");
        printf("4. Tambah Tree\n");
        printf("0. Keluar\n");

        int choice;
        char data[100];

        printf("Pilih menu (1/2/3/4/0): ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Masukkan data untuk node baru: ");
            scanf("%s", data);
            char parent_data[100];
            printf("Masukkan data node induk: ");
            scanf("%s", parent_data);
            struct TreeNode* parent = root;
            if (strcmp(parent_data, "Root") != 0) {
                parent = find_node(root, parent_data);
                if (parent == NULL) {
                    printf("Node induk dengan data '%s' tidak ditemukan.\n", parent_data);
                    continue;
                }
            }
            add_node(parent, data);
        } else if (choice == 2) {
            printf("\nTree:\n");
            display_tree(root, 0);
        } else if (choice == 3) {
            printf("Masukkan data node yang akan dihapus: ");
            scanf("%s", data);
            if (strcmp(data, "Root") == 0) {
                printf("Tidak dapat menghapus root node.\n");
            } else {
                if (!delete_node(root, data)) {
                    printf("Node dengan data '%s' tidak ditemukan.\n", data);
                } else {
                    printf("Node dengan data '%s' berhasil dihapus.\n", data);
                }
            }
        } else if (choice == 4) {
            printf("Masukkan data untuk Tree baru: ");
            scanf("%s", data);
            root = add_parent(root, data);
            printf("Tree baru dengan data '%s' berhasil ditambahkan.\n", data);
        } else if (choice == 0) {
            printf("Program selesai.\n");
            break;
        } else {
            printf("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 0.\n");
        }
    }

    // Free allocated memory
    free(root);

    return 0;
}

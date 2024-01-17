using System;
using System.Collections.Generic;

class TreeNode
{
    public string Data { get; set; }
    public List<TreeNode> Children { get; } = new List<TreeNode>();
}

class Program
{
    static TreeNode AddNode(TreeNode parent, string data)
    {
        TreeNode newNode = new TreeNode { Data = data };
        parent.Children.Add(newNode);
        return newNode;
    }

    static void DisplayTree(TreeNode node, int level = 0)
    {
        if (node != null)
        {
            Console.WriteLine(new string(' ', level * 2) + node.Data);
            foreach (var child in node.Children)
            {
                DisplayTree(child, level + 1);
            }
        }
    }

    static bool DeleteNode(TreeNode parent, string targetData)
    {
        for (int i = 0; i < parent.Children.Count; i++)
        {
            if (parent.Children[i].Data == targetData)
            {
                parent.Children.RemoveAt(i);
                return true;
            }
            if (DeleteNode(parent.Children[i], targetData))
            {
                return true;
            }
        }
        return false;
    }

    static TreeNode FindNode(TreeNode node, string targetData)
    {
        if (node.Data == targetData)
        {
            return node;
        }

        foreach (var child in node.Children)
        {
            TreeNode result = FindNode(child, targetData);
            if (result != null)
            {
                return result;
            }
        }

        return null;
    }

    static TreeNode AddParent(TreeNode root, string data)
    {
        TreeNode newParent = new TreeNode { Data = data };
        newParent.Children.Add(root);
        return newParent;
    }

    static void Main()
    {
        TreeNode root = new TreeNode { Data = "Root" };

        while (true)
        {
            Console.WriteLine("\nMenu:");
            Console.WriteLine("1. Tambah Node");
            Console.WriteLine("2. Lihat Node");
            Console.WriteLine("3. Hapus Node");
            Console.WriteLine("4. Tambah Node Induk");
            Console.WriteLine("5. Keluar");

            Console.Write("Pilih menu (1/2/3/4/5): ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Masukkan data untuk node baru: ");
                    string data = Console.ReadLine();
                    Console.Write("Masukkan data node induk: ");
                    string parentData = Console.ReadLine();
                    TreeNode parent = root;
                    if (parentData != "Root")
                    {
                        parent = FindNode(root, parentData);
                        if (parent == null)
                        {
                            Console.WriteLine("Node induk dengan data '{0}' tidak ditemukan.", parentData);
                            continue;
                        }
                    }
                    AddNode(parent, data);
                    break;

                case "2":
                    Console.WriteLine("\nTree:");
                    DisplayTree(root);
                    break;

                case "3":
                    Console.Write("Masukkan data node yang akan dihapus: ");
                    string dataToDelete = Console.ReadLine();
                    if (dataToDelete == "Root")
                    {
                        Console.WriteLine("Tidak dapat menghapus root node.");
                    }
                    else
                    {
                        if (!DeleteNode(root, dataToDelete))
                        {
                            Console.WriteLine("Node dengan data '{0}' tidak ditemukan.", dataToDelete);
                        }
                        else
                        {
                            Console.WriteLine("Node dengan data '{0}' berhasil dihapus.", dataToDelete);
                        }
                    }
                    break;

                case "4":
                    Console.Write("Masukkan data untuk node induk baru: ");
                    string newData = Console.ReadLine();
                    root = AddParent(root, newData);
                    Console.WriteLine("Node induk baru dengan data '{0}' berhasil ditambahkan.", newData);
                    break;

                case "5":
                    Console.WriteLine("Program selesai.");
                    return;

                default:
                    Console.WriteLine("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.");
                    break;
            }
        }
    }
}

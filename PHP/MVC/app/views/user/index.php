<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Daftar Pengguna</title>
</head>
<body>
    <h2>Daftar Pengguna</h2>
    <a href="?action=create">Tambah Pengguna</a>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nama</th>
            <th>Jabatan</th>
            <th>Contact Person</th>
            <th>Email</th>
            <th>Aksi</th>
        </tr>
        <?php foreach ($users as $user): ?>
            <tr>
                <td><?= $user['id_user'] ?></td>
                <td><?= $user['name'] ?></td>
                <td><?= $user['position'] ?></td>
                <td><?= $user['contact_person'] ?></td>
                <td><?= $user['email'] ?></td>
                <td>
                    <a href="?action=edit&id=<?= $user['id_user'] ?>">Edit</a>
                    <a href="?action=delete&id=<?= $user['id_user'] ?>" onclick="return confirm('Anda yakin ingin menghapus pengguna ini?');">Hapus</a>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>

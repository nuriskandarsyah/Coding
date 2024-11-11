<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tambah Pengguna</title>
</head>
<body>
    <h2>Tambah Pengguna</h2>
    <form action="?action=store" method="POST">
        <label>Nama:</label>
        <input type="text" name="name" required><br>

        <label>Jabatan:</label>
        <input type="text" name="position" required><br>

        <label>Password:</label>
        <input type="password" name="password" required><br>

        <label>Contact Person:</label>
        <input type="text" name="contact_person"><br>

        <label>Email:</label>
        <input type="email" name="email"><br>

        <input type="submit" value="Tambah">
    </form>
    <a href="?action=index">Kembali</a>
</body>
</html>

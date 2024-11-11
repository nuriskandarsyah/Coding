<?php
session_start();

// Cek apakah pengguna sudah login
if (!isset($_SESSION["name"])) {
    header("Location: login.php");
    exit;
}

// Proses logout
if (isset($_POST["logout"])) {
    session_unset();
    session_destroy();
    header('Location: index.php');
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>
    <h1>Selamat datang, <?= $_SESSION["name"] ?></h1>
    
    <!-- Form Logout -->
    <form action="dashboard.php" method="POST">
        <input type="submit" value="Log Out" class="submit-button" name="logout">
    </form>
</body>
</html>

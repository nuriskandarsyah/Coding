<?php
include "../app/service/database.php";
session_start();

$message = "";

if(isset($_SESSION["is_login"])){
    header("Location: dashboard.php");
}

// Jika login form di-submit
if (isset($_POST['login'])) {
    $username = $_POST['name'];
    $password = $_POST['password'];
    
    // Menggunakan prepared statements untuk menghindari SQL injection
    $sql = "SELECT * FROM users WHERE name=? AND password=?";
    $stmt = $db->prepare($sql);
    $stmt->bind_param("ss", $username, $password); // "ss" berarti dua string
    $stmt->execute();
    $result = $stmt->get_result();

    // Cek apakah ada data yang ditemukan
    if ($result->num_rows > 0) {
        $data = $result->fetch_assoc();
        header("Location: dashboard.php"); 
        $_SESSION["name"] = $data["name"];
        $_SESSION["is_login"] = true;
        exit; 
    } else {
        // Menyimpan pesan ke sesi untuk ditampilkan di halaman login
        $_SESSION['message'] = "Akun tidak ditemukan";

        header("Location: login.php");
        exit;
    }
}

// Retrieve message from session if available
if (isset($_SESSION['message'])) {
    $message = $_SESSION['message'];
    unset($_SESSION['message']); // Menghapus pesan setelah ditampilkan
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/auth.css">
    <title>Login</title>
</head>
<body>
    <div class="banner">
        <form action="login.php" method="POST">
            <div class="login-form">
                <div class="logo">
                    <img src="static/logo.png" alt="Logo">
                </div>
                <div class="input-container">
                    <input type="text" placeholder="username" name="name" required><br>
                </div>
                <div class="input-container">
                    <input type="password" placeholder="password" name="password" required><br>
                </div>
                <input type="submit" value="Log in" class="submit-button" name="login">
                
        <!-- Menampilkan pesan jika ada, di bawah form -->
        <?php if ($message): ?>
            <div class="message">
                <p><?php echo $message; ?></p>
            </div>
        <?php endif; ?>

            </div>
        </form>
    </div>
</body>
</html>

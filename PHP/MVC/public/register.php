<?php
session_start();
require_once "../app/service/database.php";

// Initialize message
$message = "";

if(isset($_SESSION["is_login"])){
    header("Location: dashboard.php");
}

if (isset($_POST['register'])) {
    // Get data from the form
    $name = $_POST['name'];
    $password = $_POST['password'];

    // Check if the username already exists in the database
    $checkQuery = "SELECT COUNT(*) AS count FROM users WHERE name = ?";
    $checkStmt = $db->prepare($checkQuery);
    $checkStmt->bind_param("s", $name);
    $checkStmt->execute();
    $result = $checkStmt->get_result();
    $userExists = $result->fetch_assoc()['count'];

    if ($userExists > 0) {
        // Save message in session
        $_SESSION['message'] = "Username sudah ada. Silakan gunakan username lain.";
    } else {
        // Query to insert new user data
        $insertQuery = "INSERT INTO users (name, password) VALUES (?, ?)";
        $stmt = $db->prepare($insertQuery);
        $stmt->bind_param("ss", $name, $password);

        // Execute query
        if ($stmt->execute()) {
            $_SESSION['message'] = "Registrasi berhasil!";
        } else {
            $_SESSION['message'] = "Registrasi gagal: " . $stmt->error; // Show error if failed
        }
    }

}

// Retrieve message from session if available
if (isset($_SESSION['message'])) {
    $message = $_SESSION['message'];
    unset($_SESSION['message']);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Akun</title>
    <link rel="stylesheet" href="static/auth.css">
</head>
<body>
<div class="banner">
    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="POST">
        <div class="login-form">
            <div class="logo">
                <img src="static/logo.png" alt="Logo">
            </div>
            <div class="input-container">
                <input type="text" placeholder="Username" id="name" name="name" required>
            </div>
            <div class="input-container">
                <input type="password" placeholder="Password" id="password" name="password" required>
            </div>
            <br>
            <input type="submit" name="register" value="Register" class="submit-button">
            
    <?php if ($message): ?>
        <p><?php echo $message; ?></p>
    <?php endif; ?>

        </div>
    </form>
</div>
</body>
</html>

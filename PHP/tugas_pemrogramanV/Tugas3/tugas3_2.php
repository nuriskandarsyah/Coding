<?php
// Inisialisasi variabel hasil untuk menampung data
$hasil = null;

function hitungKerucut($jari2, $tinggi) {
    $pi = pi(); // Menggunakan fungsi pi()
    $luas_alas = $pi * pow($jari2, 2); // Rumus luas alas
    $s = sqrt(pow($jari2, 2) + pow($tinggi, 2)); // Menghitung sisi/garis pelukis
    $luas_selimut = $pi * $jari2 * $s; // Rumus luas selimut
    $luas_permukaan = $luas_alas + $luas_selimut; // Luas permukaan kerucut

    // Mengembalikan hasil
    return [
        'luas_alas' => $luas_alas,
        'luas_selimut' => $luas_selimut,
        'luas_permukaan' => $luas_permukaan
    ];
}

// Mengecek apakah inputan telah disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Mengambil input dari user
    $jari2 = $_POST['jari2'];
    $tinggi = $_POST['tinggi'];

    // Validasi input
    if (is_numeric($jari2) && is_numeric($tinggi) && $jari2 > 0 && $tinggi > 0) {
        $hasil = hitungKerucut($jari2, $tinggi);
    } else {
        $hasil = "Inputan tidak valid!!!";
    }
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/auth.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <title>Perhitungan Luas Kerucut</title>
</head>
<body>
<div class="banner">
<form method="POST">
    <div class="back-button">
        <box-icon><a href="Tugas3_dashboard.php"><i class='bx bx-log-out'></i>&nbsp;&nbsp;</a></box-icon>
    </div>
    <div class="login-form">
        <h2>Perhitungan Luas Kerucut</h2>

        <!-- Form input -->
        
            <div class="input-container">
                <input type="number" placeholder="Jari-Jari Kerucut(cm)" name="jari2" id="jari2" required><br><br>
            </div>
            <div class="input-container">
                <input type="number" placeholder="Tinggi Kerucut(cm)" name="tinggi" id="tinggi" required><br><br>
            </div>
            <input type="submit" value="Hitung!!" class="submit-button">
        
        <div class='result-container'>
        <!-- Menampilkan hasil di bawah form -->
        <?php if ($hasil !== null): ?>
            <?php if (is_array($hasil)): ?>
                <p>Luas Alas Kerucut: <strong><?= number_format($hasil['luas_alas'], 2, ',', '.') ?> cm²</strong></p>
                <p>Luas Selimut Kerucut: <strong><?= number_format($hasil['luas_selimut'], 2, ',', '.') ?> cm²</strong></p>
                <p>Luas Permukaan Kerucut: <strong><?= number_format($hasil['luas_permukaan'], 2, ',', '.') ?> cm²</strong></p>
            <?php else: ?>
                <p><strong><?= $hasil ?></strong></p>
            <?php endif; ?>
        <?php endif; ?>
        </div>
    </div>
</form>
</div>
</body>
</html>

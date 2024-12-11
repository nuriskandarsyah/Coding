<?php
function hitungBunga($SaldoAwal, $bunga, $bulan) {
    $SaldoAkhir = $SaldoAwal * pow((1 + $bunga / 100), $bulan);

    return [
        'SaldoAkhir' => $SaldoAkhir
    ];
}

$hasil = null;


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $SaldoAwal = $_POST['SaldoAwal'];
    $bunga = $_POST['bunga'];
    $bulan = $_POST['bulan'];
   
    if (is_numeric($SaldoAwal) && is_numeric($bunga) && is_numeric($bulan) && $SaldoAwal > 0 && $bunga >= 0 && $bulan > 0) {
        $hasil = hitungBunga($SaldoAwal, $bunga, $bulan);
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
    <title>Perhitungan Bunga Majemuk</title>
</head>
<body>
<div class="banner">
<form method="POST">
    <div class="back-button">
        <box-icon><a href="Tugas3_dashboard.php"><i class='bx bx-log-out'></i>&nbsp;&nbsp;</a></box-icon>
    </div>
    <div class="login-form">
    <h2>Perhitungan Bunga Majemuk</h2>

    <!-- Form Inputan -->
        <div class="input-container">
            <input type="number" placeholder="Masukkan Saldo Awal (Rp):" name="SaldoAwal" id="SaldoAwal" required>
        </div>
        <div class="input-container">
            <input type="number" placeholder="Masukkan Bunga per Bulan (%): " name="bunga" id="bunga" step="0.01" required>
        </div>
        <div class="input-container">
            <input type="number" placeholder="Masukkan Jumlah Bulan: " name="bulan" id="bulan" required>
        </div>
        <input type="submit" value="Hitung!!" class="submit-button">
    <div class='result-container'>
    <!-- Menampilkan hasil -->
    <?php if ($hasil !== null): ?>
        <h3>Hasil Perhitungan:</h3>
        <?php if (is_array($hasil)): ?>
            <p>Saldo Akhir setelah <?= htmlspecialchars($bulan) ?> bulan adalah: <strong>Rp. <?= number_format($hasil['SaldoAkhir'], 2, ',', '.') ?></strong></p>
        <?php else: ?>
            <p><strong><?= htmlspecialchars($hasil) ?></strong></p>
        <?php endif; ?>
    <?php endif; ?>
    </div>
    </div>
</form>
</body>
</html>

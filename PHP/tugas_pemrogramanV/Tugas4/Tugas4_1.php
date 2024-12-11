<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perhitungan Biaya Fotocopy</title>
    <link rel="stylesheet" href="../static/auth.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="banner">
    <form method="POST">
    <div class="back-button">
        <box-icon><a href="Tugas4_dashboard.php"><i class='bx bx-log-out'></i>&nbsp;&nbsp;</a></box-icon>
    </div>
        <div class="login-form">
            <h2>Perhitungan Biaya Fotocopy</h2>
            <!-- Form Input -->
                <div class="input-container">
                    <input type="number" name="jumlahLembar" placeholder="Masukkan jumlah lembar" required>
                </div>
                <input type="submit" value="Hitung!!" class="submit-button">

            <!-- Menampilkan Hasil -->
            <?php
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                $jumlahLembar = (int) $_POST['jumlahLembar'];

                $hargaPerLembar = 0;
                
                if ($jumlahLembar < 100) {
                    $hargaPerLembar = 150;
                } elseif ($jumlahLembar >= 100 && $jumlahLembar <= 200) {
                    $hargaPerLembar = 100;
                } else {
                    $hargaPerLembar = 80;
                }

                $totalBiaya = $jumlahLembar * $hargaPerLembar;

                echo "<div class='result-container'>";
                echo "<p><strong>Jumlah fotocopy:</strong> $jumlahLembar lembar</p>";
                echo "<p><strong>Harga per lembar:</strong> Rp. $hargaPerLembar</p>";
                echo "<p><strong>Total biaya yang harus dibayar:</strong> Rp. $totalBiaya</p>";
                echo "</div>";
            }
            ?>
        </div>
    </form>
    </div>
</body>
</html>

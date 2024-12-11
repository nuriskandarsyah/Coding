<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/auth.css">
    <title>Tugas 3</title>
</head>
<body>
    <form method="POST">
        <div class="menu-container">
            <div class="menu-grid">
                <!-- Suku Bunga Majemuk -->
                <div class="menu-item">
                    <?php
                        // Deklarasi variabel
                        $saldo_awal = 2000000;
                        $bunga_per_bulan = 0.03;
                        $jumlah_bulan = 11;

                        // Perhitungan saldo akhir
                        $saldo_akhir = $saldo_awal * pow((1 + $bunga_per_bulan), $jumlah_bulan);

                        echo '<div class="result-container">';
                        echo "<p><b>1. Perhitungan Suku Bunga Majemuk</b></p>";
                        echo "<p>Saldo awal: Rp." . number_format($saldo_awal, 2, ',', '.') . "</p>";
                        echo "<p>Bunga per bulan: " . ($bunga_per_bulan * 100) . "%</p>";
                        echo "<p>Total yang harus dibayarkan setelah $jumlah_bulan bulan adalah: Rp." . number_format($saldo_akhir, 2, ',', '.') . "</p>";
                        echo '</div>';
                    ?>
                </div>

                <!-- Volume Bangun Ruang -->
                <div class="menu-item">
                    <?php
                        // Fungsi untuk menghitung luas alas kerucut
                        function luasAlas($r) {
                            return pi() * pow($r, 2);
                        }

                        // Fungsi untuk menghitung luas permukaan kerucut
                        function luasPermukaan($r, $s) {
                            return pi() * $r * ($r + $s);
                        }

                        // Deklarasi jari-jari dan tinggi
                        $r = 5; // Jari-jari
                        $s = 10; // Garis pelukis

                        // Perhitungan luas alas dan luas permukaan
                        $luas_alas = luasAlas($r);
                        $luas_permukaan = luasPermukaan($r, $s);

                        echo '<div class="result-container">';
                        echo "<p><b>2. Perhitungan Volume Kerucut</b></p>";
                        echo "<p>Luas Alas Kerucut: " . number_format($luas_alas, 2, ',', '.') . " m²</p>";
                        echo "<p>Luas Permukaan Kerucut: " . number_format($luas_permukaan, 2, ',', '.') . " m²</p>";
                        echo '</div>';
                    ?>
                </div>
            </div>
        </div>
    </form>
</body>
</html>

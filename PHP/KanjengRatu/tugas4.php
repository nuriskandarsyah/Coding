<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/auth.css">
    <title>Tugas 4</title>
</head>
<body>
    <form method="POST">
        <div class="menu-container">
            <div class="menu-grid">
                <!-- Perhitungan Biaya Fotocopy -->
                <div class="menu-item">
                    <?php            
                            $jumlahLembar = 158;

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
                            echo "<p><b>1. Perhitungan Biaya Fotocopy</b></p>";
                            echo "<p><strong>Jumlah fotocopy:</strong> $jumlahLembar lembar</p>";
                            echo "<p><strong>Harga per lembar:</strong> Rp. $hargaPerLembar</p>";
                            echo "<p><strong>Total biaya yang harus dibayar:</strong> Rp. $totalBiaya</p>";
                            echo "</div>";
                    ?>
                </div>


                <!-- Perhitungan jumlah hari dalam bulan ini -->
                <div class="menu-item">
                    <?php
                    $nilai = $grade = $keterangan = '';  // Initialize variables

                    if (isset($_POST['submit'])) {
                        $nilai = $_POST['nilai'];

                        if (is_numeric($nilai)) {  // Validate input as a number
                            switch (true) {
                                case ($nilai >= 90):
                                    $grade = "A";
                                    $keterangan = "Baik Sekali";
                                    break;
                                case ($nilai >= 76):
                                    $grade = "B";
                                    $keterangan = "Baik";
                                    break;
                                case ($nilai >= 60):
                                    $grade = "C";
                                    $keterangan = "Cukup";
                                    break;
                                case ($nilai >= 50):
                                    $grade = "D";
                                    $keterangan = "Kurang";
                                    break;
                                default:
                                    $grade = "E";
                                    $keterangan = "Nilai Kurang";
                                    break;
                            }
                        } else {
                            $grade = "Error";
                            $keterangan = "Masukkan nilai yang valid!";
                        }
                    }
                    ?>
                
                    <div class="input-container">
                        <input type="number" placeholder="Masukkan Nilai" name="nilai" id="nilai" step="0.01" required value="<?= htmlspecialchars($nilai) ?>">
                    </div>
                    <input type="submit" name="submit" value="submit" class="submit-button">        
                    <div class="result-container">
                        <?php if ($nilai !== ''): ?>
                            <p>Nilai: <?= htmlspecialchars($nilai) ?></p>
                            <p>Grade: <?= htmlspecialchars($grade) ?></p>
                            <p>Keterangan: <?= htmlspecialchars($keterangan) ?></p>
                        <?php endif; ?>
                    </div>
                </div>

                <!-- Perhitungan jumlah hari dalam bulan ini -->
                <div class="menu-item">
                <?php
                
                $bulan = date('n');

                switch ($bulan) {
                    case 2:
                        $hari = 28;
                        break;
                    case 4:
                    case 6:
                    case 9:
                    case 11:
                        $hari = 30;
                        break;
                    default:
                        $hari = 31;
                }
                echo '<div class="result-container">';
                echo "<p><b>3. Perhitungan Jumlah Hari Dalam Bulan Ini</b></p>";
                echo "<p>Bulan ini mempunyai " . $hari . " hari.</p>";
                echo '</div>';
                ?>
                </div>
            </div>
        </div>
    </form>
</body>
</html>

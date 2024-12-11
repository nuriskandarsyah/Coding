<?php
// Perhitungan biaya fotocopy
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

echo "<br>";
echo "<br>";
echo "2.Perhitungan nilai grade";
$nilai = $grade = $keterangan = '';

if (isset($_POST['submit'])) { // Periksa jika form dikirim
    $nilai = $_POST['nilai'];

    if (is_numeric($nilai)) { // Validasi input sebagai angka
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

echo "<div class='form-container'>";
echo "<form method='POST' action=''>";
echo    "<div class='input-container'>";
echo        "<label for='nilai'>Masukkan Nilai:</label>";
echo        "<input type='number' placeholder='Masukkan Nilai' name='nilai' id='nilai' step='0.01' required value='" . htmlspecialchars($nilai) . "'>";
echo    "</div>";
echo    "<input type='submit' name='submit' value='Submit' class='submit-button'>";
echo "</form>";
echo "</div>";

if ($nilai !== '') {
    echo "<div class='result-container'>";
    echo    "<p><strong>Nilai:</strong> $nilai</p>";
    echo    "<p><strong>Grade:</strong> $grade</p>";
    echo    "<p><strong>Keterangan:</strong> $keterangan</p>";
    echo "</div>";
}

echo "<br>";
echo "<br>";
// Perhitungan jumlah hari dalam bulan ini
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

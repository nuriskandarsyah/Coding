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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keterangan Grade Nilai</title>
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
            <div class="input-container">
                <input type="number" placeholder="Masukkan Nilai" name="nilai" id="nilai" step="0.01" required value="<?= htmlspecialchars($nilai) ?>">
            </div>
            <input type="submit" name="submit" value="Ookeeee" class="submit-button">
            <div class="result-container">
                <?php if ($nilai !== ''): ?>
                    <p>Nilai: <?= htmlspecialchars($nilai) ?></p>
                    <p>Grade: <?= htmlspecialchars($grade) ?></p>
                    <p>Keterangan: <?= htmlspecialchars($keterangan) ?></p>
                <?php endif; ?>
            </div>
        </div>
    </form>
</div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jumlah Hari dalam Bulan</title>
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
                echo '<div class="submit-button">';
                echo "<p>Bulan ini mempunyai " . $hari . " hari.</p>";
                echo '</div>';
                ?>
        </div>
    </form>
</div>
</body>
</html>

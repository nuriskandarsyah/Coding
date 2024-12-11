<?php
$kelipatan10 = 0;
for ($b = 5; $b <= 100; $b++) {
    if ($b % 10 == 0){
        $kelipatan10++;
    }
}

$jumlah = 0;
for ($i = 2; $i <= 50; $i++) {
    $jumlah += $i;
}

$kelipatan6 = 0;
for ($i = 3; $i <= 127; $i++) {
    if ($i % 6 == 0) {
        $kelipatan6++;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tugas 5</title>
    <link rel="stylesheet" href="static/auth.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
<form method="POST">
        <div class="menu-container">
            <div class="menu-grid">
            <div class="menu-item">
                <div class="result-container">
                    <p>1. Jumlah Bilangan 5 s/d 100 yang Berkelipatan 10:</p>
                    <p><b><?php echo $kelipatan10; ?></b></p>

                    <p>2. Jumlah Bilangan dari 2 s/d 50:</p>
                    <p><b><?php echo $jumlah; ?></b></p>

                    <p>3. Banyaknya Bilangan Bulat dari 3 s/d 127 yang Merupakan Kelipatan 6:</p>
                    <p><b><?php echo $kelipatan6; ?></b></p>    
                </div>
            </div>
        </div>
        </div>
    </form>
</body>
</html>
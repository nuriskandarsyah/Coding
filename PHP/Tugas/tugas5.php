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
echo "<p>1. Jumlah Bilangan 5 s/d 100 yang Berkelipatan 10:</p>";
echo "<p><b><?php echo $kelipatan10; ?></b></p>";

echo "<p>2. Jumlah Bilangan dari 2 s/d 50:</p>";
echo "<p><b><?php echo $jumlah; ?></b></p>";

echo "<p>3. Banyaknya Bilangan Bulat dari 3 s/d 127 yang Merupakan Kelipatan 6:</p>";
echo "<p><b><?php echo $kelipatan6; ?></b></p>";
?>

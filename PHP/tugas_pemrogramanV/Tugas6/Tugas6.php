<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tugas 6</title>
    <link rel="stylesheet" href="../static/auth.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
<div class="banner">
    <form method="POST">
        <div class="back-button">
            <box-icon><a href="Tugas6_dashboard.php"><i class='bx bx-log-out'></i>&nbsp;&nbsp;</a></box-icon>
        </div>
        <div class="next-button">
            <a href="tugas6_MdArray.php">Multidimensional<br>Array</a>
        </div>
        <div class="login-form">
            <h2>1. Array Associative</h2>
            <div class="result-container">
                <?php
                $pegawai = array("lina", "arni", "jona", "punjabi", "marcus", "marlin");

                $pegawai_associative = array(
                    "p1" => $pegawai[0],
                    "p2" => $pegawai[1],
                    "p3" => $pegawai[2],
                    "p4" => $pegawai[3],
                    "p5" => $pegawai[4],
                    "p6" => $pegawai[5],
                );

                echo "<strong>Data Pegawai (Associative Array) Sebelum Diurutkan </srong><br />";
                foreach ($pegawai_associative as $key => $value) {
                    echo "$key: $value<br />";
                }
                echo "<br />";

                asort($pegawai_associative);

                echo "<strong>Data Pegawai (Associative Array) Setelah Diurutkan</strong><br />";
                foreach ($pegawai_associative as $key => $value) {
                    echo "$key: $value<br />";
                }
                ?>
            </div>
        </div>
        <div class="login-form">
            <h2>2. 5 fungsi array</h2>
            <div class="result-container">
                <?php
                    $pegawai = array("lina", "arni", "jona", "punjabi", "marcus", "marlin");

                    //array_reverse — Membalik urutan elemen array
                    $reversedPegawai = array_reverse($pegawai);
                    echo "1. Array setelah dibalik urutannya:\n";
                    print_r($reversedPegawai);
                    echo "<br><br>";

                    //array_slice — Mengambil potongan array
                    $slicedPegawai = array_slice($pegawai, 1, 3); // Ambil elemen mulai dari indeks ke-1 sebanyak 3 elemen
                    echo "2. Potongan array (3 elemen dari indeks ke-1):\n";
                    print_r($slicedPegawai);
                    echo "<br><br>";

                    //in_array — Memeriksa apakah elemen ada di dalam array
                    $namaDicari = "marcus";
                    $exists = in_array($namaDicari, $pegawai) ? "ada" : "tidak ada";
                    echo "3. Apakah '$namaDicari' ada dalam array? $exists\n";
                    echo "<br><br>";

                    //array_unique — Menghapus elemen duplikat dalam array
                    $pegawai[] = "lina";
                    $uniquePegawai = array_unique($pegawai);
                    echo "4. Array setelah menghapus elemen duplikat:\n";
                    print_r($uniquePegawai);
                    echo "<br><br>";
                    ?>
            </div>
        </div>
    </form>
</div>
</body>
</html>

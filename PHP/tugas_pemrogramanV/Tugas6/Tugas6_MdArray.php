<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
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
        <div class="login-form">
            <h2>Multidimensional Array</h2>
            <div class="card-container">
                <?php
                    $angka = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ];

                    $pegawaiDetail = [
                        ["nama" => "Lina", "jabatan" => "Manager", "gaji" => 10000000],
                        ["nama" => "Arni", "jabatan" => "Supervisor", "gaji" => 7000000],
                        ["nama" => "Jona", "jabatan" => "Staff", "gaji" => 5000000],
                        ["nama" => "Punjabi", "jabatan" => "Staff", "gaji" => 5000000],
                        ["nama" => "Marcus", "jabatan" => "Supervisor", "gaji" => 7000000],
                        ["nama" => "Marlin", "jabatan" => "Manager", "gaji" => 10000000],
                        ["nama" => "Suriya", "jabatan" => "HR", "gaji" => 12000000],
                        ["nama" => "karsono", "jabatan" => "Umum", "gaji" => 1000000],
                        ["nama" => "Wumbo", "jabatan" => "Direktur", "gaji" => 99999999],

                    ];

                    $pegawaiIndex = 0;

                    foreach ($angka as $row) {
                        foreach ($row as $num) {
                            echo '  <div class="card">';
                            echo '      <div class="card-inner">';
                            echo '          <div class="card-front">' . $num . '</div>';
                            echo '              <div class="card-back">';
                            if (isset($pegawaiDetail[$pegawaiIndex])) {
                                $pegawai = $pegawaiDetail[$pegawaiIndex];
                                echo 'Nama: ' . $pegawai["nama"] . '<br>';
                                echo 'Jabatan: ' . $pegawai["jabatan"] . '<br>';
                                echo 'Gaji: Rp' . number_format($pegawai["gaji"], 0, ',', '.') . '<br>';
                            } else {
                                echo 'No Data';
                            }
                            echo '              </div>';
                            echo '      </div>';
                            echo '  </div>';
                            $pegawaiIndex++;
                        }
                    }
                ?>
            </div>
        </div>
        </form>
    </div>
</body>
</html>

<?php
$pegawai = array("lina", "arni", "jona", "punjabi", "marcus", "marlin");
echo "<strong>Sebelum diurutkan</strong><br />";
    foreach($pegawai as $data => $nama){
        echo "$data: $nama"."<br />";
    }
    echo "<br/>";

sort($pegawai);
echo "<strong>Setelah diurutkan</strong><br />";
    foreach($pegawai as $data => $nama){
        echo "$data: $nama"."<br />";
    }

?>
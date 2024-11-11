<?php

$hostname = "localhost";
$username = "root";
$password = "";
$database_name = "erp";

// Establish the database connection
$db = mysqli_connect($hostname, $username, $password, $database_name);

/*
// Check connection
if (!$db) {
    echo "Koneksi gagal!";
    die("Error: " . mysqli_connect_error());
} else {
    echo "Database terhubung.\n";
}//
*/

return $db; // This allows other files to retrieve $db when including this file

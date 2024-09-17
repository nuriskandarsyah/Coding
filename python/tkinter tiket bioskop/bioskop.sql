-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 07:25 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kasir`
--

-- --------------------------------------------------------


-- Table structure for table `bioskop`
CREATE TABLE `bioskop` (
    `id` int(11) NOT NULL,
    `Nomer_Transaksi` VARCHAR(10) NULL,
    `Nama` VARCHAR(50) NULL,
    `Nomer_Kursi` VARCHAR(10) NULL,
    `Tgl` DATE NULL DEFAULT NULL,
    `Harga` DECIMAL(10) NULL DEFAULT NULL, 
    `Jumlah_Tiket` INT NULL,
    `Total_Bayar` DECIMAL(10) NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Indexes for table `bioskop`
ALTER TABLE `bioskop`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Nomer_Transaksi` (`Nomer_Transaksi`);

-- AUTO_INCREMENT for table `bioskop`
ALTER TABLE `bioskop`
  MODIFY `id` INT NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

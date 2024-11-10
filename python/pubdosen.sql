-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 19, 2024 at 06:47 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `anjungan`
--

-- --------------------------------------------------------

--
-- Table structure for table `pubdosen`
--

CREATE TABLE `pubdosen` (
  `pub_id` int(11) NOT NULL,
  `dosen_id` int(11) NOT NULL,
  `judul` varchar(255) DEFAULT NULL,
  `jurnal` varchar(255) DEFAULT NULL,
  `tgl_terbit` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pubdosen`
--

INSERT INTO `pubdosen` (`pub_id`, `dosen_id`, `judul`, `jurnal`, `tgl_terbit`) VALUES
(12, 4, 'wumboing', 'CompletionCertificateNur Iskandar S-98375.pdf', '2024-07-03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pubdosen`
--
ALTER TABLE `pubdosen`
  ADD PRIMARY KEY (`pub_id`),
  ADD KEY `pub_dosen_ibfk_1` (`dosen_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pubdosen`
--
ALTER TABLE `pubdosen`
  MODIFY `pub_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pubdosen`
--
ALTER TABLE `pubdosen`
  ADD CONSTRAINT `pubdosen_ibfk_1` FOREIGN KEY (`dosen_id`) REFERENCES `dosen` (`dosen_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

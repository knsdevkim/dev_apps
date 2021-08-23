-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 17, 2020 at 03:40 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parkinglotsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth`
--

CREATE TABLE `auth` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `level` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth`
--

INSERT INTO `auth` (`id`, `username`, `password`, `level`) VALUES
(1, 'admin', 'admin', '1');

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `time` text NOT NULL,
  `user` int(11) NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`id`, `date`, `time`, `user`, `status`) VALUES
(1, 'Nov 07, 2020', '04:11 am', 1, 'PARKED'),
(2, 'Nov 07, 2020', '04:11 am', 1, 'PARK OUT'),
(3, 'Nov 11, 2020', '06:11 am', 1, 'PARKED'),
(4, 'Nov 11, 2020', '06:11 am', 1, 'PARK OUT'),
(5, 'Nov 11, 2020', '06:11 am', 1, 'PARKED'),
(6, 'Nov 11, 2020', '06:11 am', 1, 'PARK OUT'),
(7, 'Nov 11, 2020', '11:11 am', 7, 'PARKED'),
(8, 'Nov 11, 2020', '11:11 am', 7, 'PARK OUT'),
(9, 'Nov 11, 2020', '11:11 am', 7, 'PARKED'),
(10, 'Nov 11, 2020', '12:11 pm', 8, 'PARK OUT'),
(11, 'Nov 11, 2020', '12:11 pm', 8, 'PARKED'),
(12, 'Nov 11, 2020', '12:11 pm', 8, 'PARKED'),
(13, 'Nov 11, 2020', '12:11 pm', 8, 'PARKED'),
(14, 'Nov 11, 2020', '12:11 pm', 8, 'PARKED'),
(15, 'Nov 11, 2020', '12:11 pm', 8, 'PARK OUT');

-- --------------------------------------------------------

--
-- Table structure for table `parkinglot`
--

CREATE TABLE `parkinglot` (
  `id` int(11) NOT NULL,
  `location` text NOT NULL,
  `label` text NOT NULL,
  `status` text NOT NULL DEFAULT 'AVAILABLE',
  `reserve` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `parkinglot`
--

INSERT INTO `parkinglot` (`id`, `location`, `label`, `status`, `reserve`) VALUES
(1, 'GATE 1', 'PARKING LOT 1', 'AVAILABLE', ''),
(2, 'GATE 1', 'PARKING LOT 2', 'AVAILABLE', ''),
(3, 'GATE 1', 'PARKING LOT 3', 'AVAILABLE', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `idnumber` text NOT NULL,
  `password` text DEFAULT NULL,
  `fullname` text NOT NULL,
  `address` text NOT NULL,
  `plateno` text DEFAULT NULL,
  `carmodel` text DEFAULT NULL,
  `contactnumber` text DEFAULT NULL,
  `type` text NOT NULL,
  `level` text NOT NULL DEFAULT 'normal'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `idnumber`, `password`, `fullname`, `address`, `plateno`, `carmodel`, `contactnumber`, `type`, `level`) VALUES
(1, '00001', NULL, 'kim nicole sabordo', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'employee', 'normal'),
(2, '00002', NULL, 'georgia lorenz fernin', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'student', 'normal'),
(3, '00003', NULL, 'keyla ianelle sabordo', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'employee', 'normal'),
(4, '00004', NULL, 'stephanie chua', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'employee', 'normal'),
(5, 'admin', '$2y$12$dxZjKluEw.0F5VBbjzv.M.hI6QJMUeFSDp5A90rqrwjWHwXZax/yC', 'admin', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'admin', 'admin'),
(7, '00005', NULL, 'jdjddj', 'dndjdjdj', '00230101', 'Toyota - Fortuner', NULL, 'Employee', 'normal'),
(8, '00007', NULL, 'tesla', 'bacolod city', '00230101', 'Toyota - Fortuner', NULL, 'Student', 'normal');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth`
--
ALTER TABLE `auth`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `parkinglot`
--
ALTER TABLE `parkinglot`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth`
--
ALTER TABLE `auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `parkinglot`
--
ALTER TABLE `parkinglot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

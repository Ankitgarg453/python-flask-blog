-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 10, 2021 at 10:54 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `firstflaskdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `firstflaskdbtbl`
--

CREATE TABLE `firstflaskdbtbl` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `sub_title` varchar(25) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(50) NOT NULL,
  `img_file` varchar(15) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `firstflaskdbtbl`
--

INSERT INTO `firstflaskdbtbl` (`sno`, `title`, `sub_title`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'post title', 'first sub titlee', 'first-post', 'content of first post', 'post-bg.jpg', '2021-09-11 00:56:52'),
(4, 'new post title', 'new subtitle', 'new-post-slug', 'content', 'data.png', '2021-09-10 19:38:47'),
(5, 'third post title', 'thirt post sub title', 'third-slug', 'swsw', 'scdc', '2021-09-11 01:16:24'),
(6, 'new post title4', 'new post s title4', 'slug-post4', 'cont new post title4', 'img4', '2021-09-11 01:19:10'),
(7, 'new post title5', 'new post stitle5', 'slug-post5', 'cont new post title5', 'img5', '2021-09-11 01:19:42');

-- --------------------------------------------------------

--
-- Table structure for table `secflaskdbtbl_contacts`
--

CREATE TABLE `secflaskdbtbl_contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `phn_nmbr` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `secflaskdbtbl_contacts`
--

INSERT INTO `secflaskdbtbl_contacts` (`sno`, `name`, `phn_nmbr`, `msg`, `date`, `email`) VALUES
(1, 'arg', '0788873000', 'p msg', '2021-09-08 01:24:36', 'gar@gmail.com'),
(2, 'Testing1', '9009090902', 'testing msg', '2021-09-08 01:26:22', 'Testing1@test.com'),
(3, 'test', '07888730000', 'msg', '2021-09-08 01:52:43', 'Testing1@test.com'),
(4, 'name em tst', '7894561230', 'msg for email testing1', '2021-09-08 18:42:13', 'ankitgargit123@gmail.com'),
(5, 'email nm tst1', '7897897897', 'test msg 1', '2021-09-08 19:00:51', 'ankitgarg453@gmail.com'),
(6, 'email nm tst1', '7897897897', 'test msg 1', '2021-09-08 19:14:30', 'ankitgarg453@gmail.com'),
(7, 'email nm tst1', '7897897897', 'test msg 1', '2021-09-08 19:16:05', 'ankitgarg453@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `firstflaskdbtbl`
--
ALTER TABLE `firstflaskdbtbl`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `secflaskdbtbl_contacts`
--
ALTER TABLE `secflaskdbtbl_contacts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `firstflaskdbtbl`
--
ALTER TABLE `firstflaskdbtbl`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `secflaskdbtbl_contacts`
--
ALTER TABLE `secflaskdbtbl_contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

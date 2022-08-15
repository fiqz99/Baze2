- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 15, 2022 at 09:32 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `marketing_agencies`
--

-- --------------------------------------------------------

--
-- Table structure for table `buyer`
--

DROP TABLE IF EXISTS `buyer`;
CREATE TABLE IF NOT EXISTS `buyer` (
  `buyer_id` int(11) NOT NULL,
  `order_no` int(11) NOT NULL,
  `id_market` int(11) NOT NULL,
  PRIMARY KEY (`buyer_id`),
  KEY `id_market` (`id_market`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
CREATE TABLE IF NOT EXISTS `city` (
  `post_code` int(11) NOT NULL,
  `city_name` varchar(45) NOT NULL,
  PRIMARY KEY (`post_code`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
CREATE TABLE IF NOT EXISTS `clients` (
  `client_id` int(11) NOT NULL,
  `client_adress` varchar(100) NOT NULL,
  `client_name` varchar(50) NOT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `examine`
--

DROP TABLE IF EXISTS `examine`;
CREATE TABLE IF NOT EXISTS `examine` (
  `id_market` int(11) NOT NULL,
  `id_worker` int(11) NOT NULL,
  KEY `id_market` (`id_market`),
  KEY `id_worker` (`id_worker`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `has`
--

DROP TABLE IF EXISTS `has`;
CREATE TABLE IF NOT EXISTS `has` (
  `id_client` int(11) NOT NULL,
  `id_agency` int(11) NOT NULL,
  `contract_date` datetime NOT NULL,
  KEY `id_client` (`id_client`),
  KEY `id_agency` (`id_agency`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `market`
--

DROP TABLE IF EXISTS `market`;
CREATE TABLE IF NOT EXISTS `market` (
  `market_id` int(11) NOT NULL,
  `market_adress` varchar(50) NOT NULL,
  `market_name` varchar(50) NOT NULL,
  `market_size` int(11) NOT NULL,
  PRIMARY KEY (`market_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `marketing_agency`
--

DROP TABLE IF EXISTS `marketing_agency`;
CREATE TABLE IF NOT EXISTS `marketing_agency` (
  `agency_id` int(11) NOT NULL,
  `agency_name` varchar(100) DEFAULT NULL,
  `no_employees` int(11) NOT NULL,
  `city_postCode` int(11) NOT NULL,
  PRIMARY KEY (`agency_id`),
  KEY `city_postCode` (`city_postCode`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marketing_agency`
--

INSERT INTO `marketing_agency` (`agency_id`, `agency_name`, `no_employees`, `city_postCode`) VALUES
(1, 'Black M&M', 53, 34000),
(2, 'Blue Marketing', 32, 18000),
(3, 'BigMarket', 123, 11000);

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
CREATE TABLE IF NOT EXISTS `seller` (
  `seller_id` int(11) NOT NULL,
  `shipments_no` int(11) NOT NULL,
  `id_market` int(11) NOT NULL,
  PRIMARY KEY (`seller_id`),
  KEY `id_market` (`id_market`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `surname` varchar(20) NOT NULL,
  `userType` int(11) NOT NULL,
  `password` varchar(64) NOT NULL,
  `salt` varchar(8) NOT NULL,
  `username` varchar(20) NOT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userId`, `name`, `surname`, `userType`, `password`, `salt`, `username`) VALUES
(1, 'Filip', 'Stefanovic', 3, '59ce3e6419e5825044ca24f18f69e311a2e97e29b3f7d1c23cb33befeb045706', 'X5IUHJQG', 'admin'),
(2, 'Marko', 'Markovic', 1, 'bc7ff8a6a4e2786775f0880e7766ee6aefc5f1e5d4c7edf438701796110ff707', 'IFK3VXB6', 'marko123'),
(3, 'Jovan', 'Jovanovic', 2, '887d1be412619ec15eb053195c04dc29adcb7e8a92e898d5d1ff804063630085', 'ZDJ6ECWW', 'zmaj123');

-- --------------------------------------------------------

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
CREATE TABLE IF NOT EXISTS `worker` (
  `worker_id` int(13) NOT NULL,
  `worker_name` varchar(25) NOT NULL,
  `worker_surname` varchar(25) NOT NULL,
  `worker_gender` char(1) NOT NULL,
  `worker_adress` varchar(50) NOT NULL,
  `agency_id` int(11) NOT NULL,
  PRIMARY KEY (`worker_id`),
  KEY `agency_id` (`agency_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `worker`
--

INSERT INTO `worker` (`worker_id`, `worker_name`, `worker_surname`, `worker_gender`, `worker_adress`, `agency_id`) VALUES
(15, 'Marko', 'Markovic', 'M', 'Bulevar Oslobodjenja 15', 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

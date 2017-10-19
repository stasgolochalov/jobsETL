-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: jobs
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `Job_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Location_Id` int(11) NOT NULL,
  `Status_Id` int(11) NOT NULL,
  `Category_Id` int(11) NOT NULL,
  `Job_Title_Id` int(11) NOT NULL,
  PRIMARY KEY (`Job_Id`),
  KEY `Location_Id` (`Location_Id`),
  KEY `Status_Id` (`Status_Id`),
  KEY `Job_Title_Id` (`Job_Title_Id`),
  KEY `Category_Id` (`Category_Id`),
  CONSTRAINT `Category_Id` FOREIGN KEY (`Category_Id`) REFERENCES `categories` (`Category_Id`),
  CONSTRAINT `Job_Title_Id` FOREIGN KEY (`Job_Title_Id`) REFERENCES `job_titles` (`Job_Title_Id`),
  CONSTRAINT `Location_Id` FOREIGN KEY (`Location_Id`) REFERENCES `locations` (`Location_Id`),
  CONSTRAINT `Status_Id` FOREIGN KEY (`Status_Id`) REFERENCES `statuses` (`Status_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=165 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-19 20:09:46

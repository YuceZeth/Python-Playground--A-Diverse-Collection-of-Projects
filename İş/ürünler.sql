# Host: localhost  (Version 5.5.5-10.4.14-MariaDB)
# Date: 2020-10-20 23:33:26
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "ürünler"
#

DROP TABLE IF EXISTS `ürünler`;
CREATE TABLE `ürünler` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `urun_adi` varchar(255) DEFAULT NULL,
  `giris_miktari` int(11) DEFAULT NULL,
  `depo_miktari` int(11) DEFAULT NULL,
  `kalan_miktar` int(11) DEFAULT NULL,
  `satis_miktari` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

#
# Data for table "ürünler"
#

INSERT INTO `ürünler` VALUES (1,'mercimek',100,50,50,50),(2,'fındık',100,100,100,50),(3,'pirinç',200,190,190,10),(4,'nohut',250,100,100,150),(6,'krema',400,400,400,0);

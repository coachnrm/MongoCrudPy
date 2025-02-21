/*
 Navicat Premium Data Transfer

 Source Server         : localmariadb
 Source Server Type    : MariaDB
 Source Server Version : 101110
 Source Host           : localhost:3307
 Source Schema         : DemoDB

 Target Server Type    : MariaDB
 Target Server Version : 101110
 File Encoding         : 65001

 Date: 21/02/2025 09:23:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Customer
-- ----------------------------
CREATE TABLE `Customer`  (
  `CustomerId` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`CustomerId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

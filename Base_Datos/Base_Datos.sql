-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: Proyecto
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bitacora_sesiones`
--

DROP TABLE IF EXISTS `Bitacora_sesiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bitacora_sesiones` (
  `id_usuario` varchar(20) DEFAULT NULL,
  `fecha_entrada` datetime DEFAULT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  KEY `usuario_idx` (`id_usuario`),
  CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `Usuarios` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Cargos`
--

DROP TABLE IF EXISTS `Cargos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cargos` (
  `codigo` varchar(40) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `salario` float DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Cargos_Funciones_Asignadas`
--

DROP TABLE IF EXISTS `Cargos_Funciones_Asignadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cargos_Funciones_Asignadas` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `id_cargo` varchar(45) DEFAULT NULL,
  `id_funcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  KEY `fk_Cargos_Funciones_Asignadas_1_idx` (`id_cargo`),
  KEY `fk_Cargos_Funciones_Asignadas_2_idx` (`id_funcion`),
  CONSTRAINT `fk_Cargos_Funciones_Asignadas_1` FOREIGN KEY (`id_cargo`) REFERENCES `Cargos` (`codigo`),
  CONSTRAINT `fk_Cargos_Funciones_Asignadas_2` FOREIGN KEY (`id_funcion`) REFERENCES `Funciones_Asignadas` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Contratos`
--

DROP TABLE IF EXISTS `Contratos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contratos` (
  `codigo` varchar(20) NOT NULL,
  `id_empleado` varchar(20) NOT NULL,
  `id_cargo` varchar(20) NOT NULL,
  `id_sucursal` varchar(20) NOT NULL,
  `fecha_inicio` datetime NOT NULL,
  `fecha_terminacion` datetime NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `empleado_idx` (`id_empleado`),
  KEY `cargo_idx` (`id_cargo`),
  KEY `sucursal_idx` (`id_sucursal`),
  CONSTRAINT `c_cargo` FOREIGN KEY (`id_cargo`) REFERENCES `Cargos` (`codigo`),
  CONSTRAINT `c_empleado` FOREIGN KEY (`id_empleado`) REFERENCES `Empleados` (`codigo`),
  CONSTRAINT `c_sucursal` FOREIGN KEY (`id_sucursal`) REFERENCES `Sucursales` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Departamentos`
--

DROP TABLE IF EXISTS `Departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Departamentos` (
  `codigo` varchar(40) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `poblacion` int NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Empleados`
--

DROP TABLE IF EXISTS `Empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Empleados` (
  `codigo` varchar(20) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono_contacto` varchar(45) NOT NULL,
  `id_cargo` varchar(20) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `cargo_idx` (`id_cargo`),
  CONSTRAINT `cargo` FOREIGN KEY (`id_cargo`) REFERENCES `Cargos` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Funciones_Asignadas`
--

DROP TABLE IF EXISTS `Funciones_Asignadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Funciones_Asignadas` (
  `codigo` varchar(20) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Municipios`
--

DROP TABLE IF EXISTS `Municipios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Municipios` (
  `codigo` varchar(40) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `poblacion` varchar(45) NOT NULL,
  `tipo_municipio` varchar(45) NOT NULL,
  `departamento` varchar(40) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `departamento_idx` (`departamento`),
  KEY `fk_Municipios_1_idx` (`tipo_municipio`),
  CONSTRAINT `departamento` FOREIGN KEY (`departamento`) REFERENCES `Departamentos` (`codigo`),
  CONSTRAINT `fk_Municipios_1` FOREIGN KEY (`tipo_municipio`) REFERENCES `Tipo_Municipio` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Permisos`
--

DROP TABLE IF EXISTS `Permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Permisos` (
  `codigo` varchar(45) NOT NULL,
  `permiso` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Profesion_Empleado`
--

DROP TABLE IF EXISTS `Profesion_Empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Profesion_Empleado` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `id_empleado` varchar(45) DEFAULT NULL,
  `id_profesion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  KEY `idProfesion_idx` (`id_profesion`),
  KEY `idEmpleado` (`id_empleado`),
  CONSTRAINT `idEmpleado` FOREIGN KEY (`id_empleado`) REFERENCES `Empleados` (`codigo`),
  CONSTRAINT `idProfesion` FOREIGN KEY (`id_profesion`) REFERENCES `Profesiones` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Profesiones`
--

DROP TABLE IF EXISTS `Profesiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Profesiones` (
  `codigo` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Sucursales`
--

DROP TABLE IF EXISTS `Sucursales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sucursales` (
  `codigo` varchar(45) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `id_departamento` varchar(40) DEFAULT NULL,
  `id_municipio` varchar(40) DEFAULT NULL,
  `id_director` varchar(40) DEFAULT NULL,
  `presupuesto_anual` float DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  KEY `departamento_idx` (`id_departamento`),
  KEY `municipio_idx` (`id_municipio`),
  KEY `director_idx` (`id_director`),
  CONSTRAINT `departamento_sucursal` FOREIGN KEY (`id_departamento`) REFERENCES `Departamentos` (`codigo`),
  CONSTRAINT `director` FOREIGN KEY (`id_director`) REFERENCES `Empleados` (`codigo`),
  CONSTRAINT `municipio` FOREIGN KEY (`id_municipio`) REFERENCES `Municipios` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Tipo_Municipio`
--

DROP TABLE IF EXISTS `Tipo_Municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Municipio` (
  `codigo` varchar(20) NOT NULL,
  `tipo_municipio` varchar(45) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuarios` (
  `codigo` varchar(20) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `contrasenia` varchar(45) NOT NULL,
  `id_permiso` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  KEY `fk_Usuarios_1_idx` (`id_permiso`),
  CONSTRAINT `fk_Usuarios_1` FOREIGN KEY (`id_permiso`) REFERENCES `Permisos` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-28 12:58:28

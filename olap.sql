
CREATE TABLE dim_libros (
  idlibro int NOT NULL,
  nom_libro varchar(30) DEFAULT NULL,
  idautor int DEFAULT NULL,
  nom_autor varchar(30) DEFAULT NULL,
  ideditorial int DEFAULT NULL,
  nom_editorial varchar(30) DEFAULT NULL,
  PRIMARY KEY (idlibro)
);

-- 
CREATE TABLE dim_salidas (
  idsalida int NOT NULL,
  total_cant int DEFAULT NULL,
  PRIMARY KEY (idsalida)
);

--
CREATE TABLE dim_tiempos (
  idtiempo date NOT NULL,
  year_sal int DEFAULT NULL,
  month_sal int DEFAULT NULL,
  day_sal int DEFAULT NULL,
  PRIMARY KEY (idtiempo)
);

--
CREATE TABLE ft_salidas (
  idsalida int NOT NULL,
  idlibro int NOT NULL,
  idtiempo date NOT NULL,
  cantidad int DEFAULT NULL,
  PRIMARY KEY (idsalida,idlibro,idtiempo),
  CONSTRAINT FK_idlibro FOREIGN KEY (idlibro) REFERENCES dim_libros (idlibro),
  CONSTRAINT FK_idsalida FOREIGN KEY (idsalida) REFERENCES dim_salidas (idsalida),
  CONSTRAINT FK_idtiempo FOREIGN KEY (idtiempo) REFERENCES dim_tiempos (idtiempo)
);




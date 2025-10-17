
--

CREATE TABLE autor (
  idautor int NOT NULL,
  nom_autor varchar(60) DEFAULT NULL,
  PRIMARY KEY (idautor)
);

INSERT INTO autor VALUES (1,'Edgar Allan Poe'),(2,'Michael Hutchensen'),(3,'Louis Pasteur'),(4,'Miguel de Cervantes '),(5,'Ernest Hemingway'),(6,'Lord Byron'),(7,'William Shakespeare'),(8,'Isaac Newton'),(9,'Albert Einstein'),(10,'Alan Turing');


CREATE TABLE editorial (
  idedit int NOT NULL,
  nom_edit varchar(30) DEFAULT NULL,
  PRIMARY KEY (idedit)
);


INSERT INTO editorial VALUES (1,'Pearson'),(2,'McGraw-Hill'),(3,'Planeta'),(4,'Packt Publishing'),(5,'OReilly');


CREATE TABLE libros (
  idlibro int NOT NULL,
  nom_libro varchar(30) DEFAULT NULL,
  idautor int NOT NULL,
  ideditorial int NOT NULL,
  PRIMARY KEY (idlibro)
) ;

INSERT INTO libros VALUES (1,'Lo que el viento no se llevo',1,1),(2,'Mazinger Z',2,2),(3,'El ABC de las Matemáticas',3,3),(4,'Principia Naturalis',8,4),(5,'Mathematicus Tractadus',10,5),(6,'Computability Proof',10,5),(7,'Chaos Theory',9,1),(8,'El Quijote de la Mancha Gris',4,2),(9,'El viejo y el Mar',5,4),(10,'Buho Gris',6,3);


CREATE TABLE salida (
  idsalida int NOT NULL,
  fecha_sal date NOT NULL,
  total_cant int DEFAULT '0',
  PRIMARY KEY (idsalida)
);


INSERT INTO salida VALUES (1,'2019-03-01',10),(2,'2019-02-05',10),(3,'2019-04-28',5),(4,'2019-03-05',18),(5,'2019-05-05',13),(6,'2019-06-03',8),(7,'2019-06-10',10);



CREATE TABLE salidas_det (
  idsalida int NOT NULL,
  idlibro int NOT NULL,
  cantidad int DEFAULT '1',
  PRIMARY KEY (idsalida,idlibro)
);

INSERT INTO salidas_det VALUES (1,1,2),(1,2,1),(2,1,2),(2,3,5),(2,4,5),(3,5,3),(3,6,2),(3,7,2),(3,8,1),(4,9,3),(4,10,2),(5,1,2),(5,2,2),(5,3,2),(6,4,2),(6,5,3),(6,6,2),(7,7,3),(7,8,2),(7,9,2),(7,10,2);





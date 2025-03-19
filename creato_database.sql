DROP DATABASE IF EXISTS escuela_artes;
CREATE DATABASE IF NOT EXISTS escuela_artes;
USE escuela_artes;

CREATE TABLE IF NOT EXISTS puestos (
	idPuesto INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	salario DECIMAL(20,2) CHECK (salario >= 0),
    descripcion VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS empleados ( 
	idEmpleado INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    idPuesto INT,
	nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    mail VARCHAR(50) NOT NULL CHECK (mail LIKE '%_@_%.__%'), 
    telefono VARCHAR(20),
    direccion VARCHAR(100),
    FOREIGN KEY (idPuesto) REFERENCES puestos (idPuesto)
);

CREATE TABLE IF NOT EXISTS alumnos ( 
	idAlumno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT CHECK (edad >= 0),
    mail VARCHAR(50) NOT NULL CHECK (mail LIKE '%_@_%.__%'), 
    telefono VARCHAR(20),
    direccion VARCHAR(100),
    membresiaActiva BOOLEAN
);

CREATE TABLE IF NOT EXISTS cursos (
	idCurso INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    idEmpleado INT,
    nivel ENUM('Basico','Intermedio','Avanzado'),
    turno ENUM('Mañana', 'Tarde', 'Noche'),
	dia ENUM('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'),
	horario VARCHAR(20),
    costo DECIMAL(10,2),
    FOREIGN KEY (idEmpleado) REFERENCES empleados (idEmpleado)
);

CREATE TABLE IF NOT EXISTS inscripciones (
	idInscripcion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	idAlumno INT,
	idCurso INT,
	fechaInscripcion DATETIME,
    FOREIGN KEY (idAlumno) REFERENCES alumnos (idAlumno),
	FOREIGN KEY (idCurso) REFERENCES cursos (idCurso)
);

CREATE TABLE IF NOT EXISTS notas (
	idNota INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	idAlumno INT,
	idCurso INT,
	nota DECIMAL(10,2),
    CHECK (nota >= 0 AND nota <= 10),
    FOREIGN KEY (idAlumno) REFERENCES alumnos (idAlumno),
	FOREIGN KEY (idCurso) REFERENCES cursos (idCurso)
);

CREATE TABLE IF NOT EXISTS proveedores (
	idProveedor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
	mail VARCHAR(50) NOT NULL CHECK (mail LIKE '%_@_%.__%'),
	telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS inventario (
	idInventario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(100),
	idProveedor INT,
	cantidad INT,
	fechaIngreso DATE,
    FOREIGN KEY (idProveedor) REFERENCES proveedores (idProveedor)
);

CREATE TABLE IF NOT EXISTS redesSociales (
	idRedSocial  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    plataforma ENUM('TikTok', 'Instagram', 'Facebook'),
    idEmpleado INT,
	fecha DATETIME,
	descripcion VARCHAR(255),
	likes INT,
	seguidores INT,
	comentarios INT,
    visualizaciones INT,
    FOREIGN KEY (idEmpleado) REFERENCES empleados (idEmpleado)
);

-- INDEX para mejorar rendimiento
CREATE INDEX idx_alumnos_mail ON alumnos(mail);
CREATE INDEX idx_empleados_mail ON empleados(mail);
CREATE INDEX idx_notas_alumno ON notas(idAlumno);
CREATE INDEX idx_cursos_nombre ON cursos(nombre);


INSERT INTO puestos(idPuesto, salario, descripcion) VALUES
(1,2000000,'Director/a General'),(2,1500000,'Jefe/a de Cursos'),(3,1000000,'Secretario/a administrativo'),(4,800000,'Profesor/a'),(5,900000,'Vendedor/a'),(6,600000,'Fotógrafo'),(7,700000,'Vestuarista'),(8,1000000,'Directora de Artes'),(9,400000,'Artista'),(10,950000,'Mantenimiento'),(11,500000,'Community Manager');

INSERT INTO empleados(idEmpleado, idPuesto, nombre, apellido, mail, telefono, direccion) VALUES
(1, 1,'Maria','Lagos','marialagos@gmail.com','1130204565','Quesada 2530'),(2, 2,'Claudia','Campos','claudiacampos@gmail.com','1130204678','Mercedes 1250'),(3, 3,'Ramiro','Perez','ramiroperez@gmail.com','1130204768','Peron 600'),(4, 3,'Juana','Rodriguez','juanarodriguez@gmail.com','1130204987','Nogoya 1800'),(5, 4,'Marcelo','Gallardini','marcelogallardini@gmail.com','1130204565','Sarmiento 250'),(6, 4,'Jose','Ruiz','joseruiz@gmail.com','1130204001','Lavalle 1200'),(7, 4,'Matias','Castro','matiascastro@gmail.com','1130204002','Mitre 3200'),(8, 4,'Morena','Chavez','morenachavez@gmail.com','1130204003','Gorriti 1800'),(9, 4,'Camila','Vallejos','camilavallejos@gmail.com','1130204004','Corrientes 1500'),(10, 4,'Sabrina','Rojas','sabrinarojas@gmail.com','1130204005','Cerrito 200'),(11, 5,'Matias','Machio','matiasmachio@gmail.com','1130204006','Callao 2500'),(12, 5,'Miranda','Paredes','mirandaparedes@gmail.com','1130204007','Tucuman 800'),(13, 6,'Jose','Aquino','joseaquino@gmail.com','1130204008','Belgrano 3000'),(14, 7,'Vanesa','Straus','vanesastraus@gmail.com','1130204009','Rivadavia 900'),(15, 8,'Isabel','Pantoja','isabelpantoja@gmail.com','1130204010','La Rioja 1250'),(16, 9,'Gustavo','Fernandez','gustavofernandez@gmail.com','1130204011','Pueyrredon 1300'),(17, 9,'Lucia','Dominguez','luciadominguez@gmail.com','1130204012','Mendoza 1400'),(18, 9,'Santiago','Alvarez','santiagoalvarez@gmail.com','1130204013','Esmeralda 2100'),(19, 10,'Alfredo','Benitez','alfredobenitez@gmail.com','1130204014','Santa Fe 3000'),(20, 10,'Florencia','Martinez','florenciamartinez@gmail.com','1130204015','Entre Rios 2500'),(21, 11,'Carolina','Diaz','carolinadiaz@gmail.com','1130204016','San Juan 800'),(22, 11,'Claudia','Perez','claudiaperez@gmail.com','1145657898','Choques 1730'),(23, 4,'Romina','Clinton','romiclin@gmail.com','1132452310','Rivadavia 1245'),(24, 4,'Pablo','Ibañez','pabloibi@gmail.com','1133457789','Viedma 713');

INSERT INTO alumnos(idAlumno, nombre, apellido, edad, mail, telefono, direccion, membresiaActiva) VALUES
(1, 'Tomas','Sanchez','22','tomassanchez@gmail.com','1130204578','Torino 1780',true),(2, 'Pilar','Estevanez','25','pilarestevanez@gmail.com','1130204222','Saavedra 1560',true),(3, 'Marcos','Perez','19','marcosperez@gmail.com','1130204345','Segurola 810',true),(4, 'Lucia','Gomez','23','luciagomez@gmail.com','1130204987','Moreno 1230',true),(5, 'Federico','Gonzalez','28','federicogonzalez@gmail.com','1130204560','Laprida 2400',false),(6, 'Ana','Lopez','21','analopez@gmail.com','1130204890','Talcahuano 900',true),(7, 'Martin','Rodriguez','24','martinrodriguez@gmail.com','1130204767','Ayacucho 450',true),(8, 'Carla','Mendez','26','carlamendez@gmail.com','1130204321','Belgrano 2000',false),(9, 'Julian','Castro','20','juliancastro@gmail.com','1130204311','Independencia 1350',true),(10, 'Camila','Dominguez','23','camiladominguez@gmail.com','1130204876','San Martin 1700',true),(11, 'Matias','Silva','22','matiassilva@gmail.com','1130204778','Alem 1950',false),(12, 'Florencia','Vega','27','florenciavega@gmail.com','1130204899','Roca 1550',true),(13, 'Santiago','Mora','19','santiagomora@gmail.com','1130204650','Cuyo 980',true),(14, 'Lautaro','Ibanez','21','lautaroibanez@gmail.com','1130204661','Alberdi 820',false),(15, 'Valentina','Ramos','25','valentinaramos@gmail.com','1130204322','Lavalleja 2300',true),(16, 'Ignacio','Fernandez','24','ignaciofernandez@gmail.com','1130204779','Fitz Roy 1400',false),(17, 'Sofia','Rojas','22','sofiarojas@gmail.com','1130204891','Malabia 1300',true),(18, 'Joaquin','Aquino','28','joaquinaquino@gmail.com','1130204200','Armenia 250',true),(19, 'Nicolas','Benitez','23','nicolasbenitez@gmail.com','1130204981','Mendoza 1020',false),(20, 'Paula','Sosa','20','paulasosa@gmail.com','1130204770','San Juan 1500',true),(21, 'Agustina','Castro','22','agustinacastro@gmail.com','1130204444','Esmeralda 500',true),(22, 'Federica','Rossi','24','federicarossi@gmail.com','1130204010','Rivadavia 850',true),(23, 'Gonzalo','Perez','26','gonzaloperez@gmail.com','1130204100','Santa Fe 300',false),(24, 'Emilia','Suarez','21','emiliasuarez@gmail.com','1130204234','Santa Fe 950',false),(25, 'Nahuel','Martinez','23','nahuelmartinez@gmail.com','1130204765','Pueyrredon 3000',true),(26, 'Lucas','Villalba','22','lucasvillalba@gmail.com','1130204325','Arenales 1780',false),(27, 'Bianca','Ramirez','20','biancaramirez@gmail.com','1130204877','Urquiza 2450',true),(28, 'Santiago','Fernandez','24','santiagofernandez@gmail.com','1130204334','Moreno 200',false),(29, 'Micaela','Diaz','21','micaeladiaz@gmail.com','1130204550','Montevideo 1200',false),(30, 'Diego','Gutierrez','26','diegogutierrez@gmail.com','1130204652','French 850',true),(31, 'Julieta','Vazquez','25','julietavazquez@gmail.com','1130204330','Callao 1500',true),(32, 'Benjamin','Moreno','19','benjaminmoreno@gmail.com','1130204112','Serrano 1100',false),(33, 'Valeria','Garcia','27','valeriagarcia@gmail.com','1130204982','Las Heras 1700',false),(34, 'Leandro','Cabrera','22','leandrocabrera@gmail.com','1130204667','Viamonte 2300',true),(35, 'Franco','Molina','24','francomolina@gmail.com','1130204349','Alem 900',false),(36, 'Melina','Cruz','26','melinacruz@gmail.com','1130204002','Caseros 1800',false),(37, 'Gustavo','Pereyra','21','gustavopereyra@gmail.com','1130204894','Corrientes 3400',true),(38, 'Antonella','Luna','22','antonellaluna@gmail.com','1130204885','Armenia 600',false),(39, 'Sofia','Serrano','19','sofiaserrano@gmail.com','1130204995','Rodriguez Peña 400',true),(40, 'Juan','Lopez','25','juanlopez@gmail.com','1130204017','Maipu 1700',false),(41, 'Rocio','Sanchez','23','rociosanchez@gmail.com','1130204769','Posadas 500',true),(42, 'Felipe','Navarro','24','felipenavarro@gmail.com','1130204110','San Juan 2200',false),(43, 'Alma','Iglesias','20','almaiglesias@gmail.com','1130204220','Guemes 250',true),(44, 'Matias', 'Fernandez', '27', 'matiasfernandez@gmail.com', '1130204788', 'Avenida Rivadavia 3200', true),(45, 'Lucia', 'Gomez', '22', 'luciagomez@gmail.com', '1130204954', 'Av. Pueyrredon 1200', true),(46, 'Emilia', 'Martinez', '21', 'emiliamartinez@gmail.com', '1130204889', 'Uruguay 700', true),(47, 'Sebastian', 'Rios', '26', 'sebastianrios@gmail.com', '1130204501', 'Santa Fe 3400', true),(48, 'Bruno', 'Diaz', '23', 'brunodiaz@gmail.com', '1130204785', 'Rivadavia 4100', true),(49, 'Ana', 'Perez', '25', 'anaperez@gmail.com', '1130204113', 'Lavalle 900', true),(50, 'Julieta', 'Castro', '20', 'julietacastro@gmail.com', '1130204822', 'Alvear 1600', true),(51, 'Lucas', 'Torres', '24', 'lucastorres@gmail.com', '1130204799', 'Córdoba 2700', true),(52, 'Gabriel', 'Reyes', '22', 'gabrielreyes@gmail.com', '1130204703', 'French 300', true),(53, 'Clara', 'Vazquez', '19', 'claravazquez@gmail.com', '1130204944', 'Belgrano 2400', true),(54, 'Facundo', 'Suarez', '27', 'facundosuarez@gmail.com', '1130204219', 'Sarmiento 1800', true),(55, 'Camila', 'Romero', '22', 'camilaromero@gmail.com', '1130204522', 'Perón 3500', true),(56, 'Valentin', 'Garcia', '21', 'valentingarcia@gmail.com', '1130204467', 'Callao 1400', true),(57, 'Isabel', 'Arias', '24', 'isabelarias@gmail.com', '1130204755', 'Yrigoyen 2500', true),(58, 'Nahuel', 'Ruiz', '25', 'nahuelruiz@gmail.com', '1130204599', 'Fitz Roy 800', true),(59, 'Martina', 'Villalba', '23', 'martinavillalba@gmail.com', '1130204876', 'Malabia 900', true),(60, 'Daniel', 'Sosa', '26', 'danielsosa@gmail.com', '1130204984', 'Medrano 1700', true),(61, 'Santiago', 'Ortiz', '22', 'santiagoortiz@gmail.com', '1130204022', 'Castelli 1200', true),(62, 'Paula', 'Silva', '24', 'paulasilva@gmail.com', '1130204811', 'Billinghurst 700', true),(63, 'Federico', 'Mendoza', '21', 'federicomendoza@gmail.com', '1130204354', 'Dorrego 2100', true);

INSERT INTO cursos(idCurso, nombre, descripcion, idEmpleado, nivel, turno, dia, horario, costo) VALUES
(1,'Vestuarios','Diseño y confeccion',8,'Basico','Tarde','Viernes','17:30',40000),(2,'Vestuarios','Diseño y confeccion',8,'Intermedio','Mañana','Martes','11:30',45000),(3,'Vestuarios','Diseño y confeccion',8,'Avanzado','Noche','Viernes','20:00',60000),(4,'Pelucas y Peinados','Estilismo profesional',5,'Basico','Mañana','Lunes','13:30',40000),(5,'Pelucas y Peinados','Estilismo profesional',5,'Intermedio','Mañana','Lunes','11:00',45000),(6,'Pelucas y Peinados','Estilismo profesional',5,'Avanzado','Noche','Miercoles','20:30',60000),(7,'Taller de Fotografia','Produccion y captura de la imagen artistica',6,'Basico','Mañana','Jueves','10:30',40000),(8,'Taller de Fotografia','Produccion y captura de la imagen artistica',6,'Intermedio','Mañana','Jueves','11:40',45000),(9,'Taller de Fotografia','Produccion y captura de la imagen artistica',6,'Avanzado','Noche','Viernes','19:45',60000),(10,'Sombreros y accesorios','Confeccion de articulos escenicos',7,'Basico','Tarde','Lunes','15:30',40000),(11,'Sombreros y accesorios','Confeccion de articulos escenicos',7,'Intermedio','Tarde','Lunes','14:00',45000),(12,'Sombreros y accesorios','Confeccion de articulos escenicos',7,'Avanzado','Noche','Sabado','20:30',60000),(13,'Performance Artistica','Acting y puesta en escena del personaje',9,'Basico','Mañana','Jueves','9:30',40000),(14,'Performance Artistica','Acting y puesta en escena del personaje',9,'Intermedio','Mañana','Jueves','11:00',45000),(15,'Performance Artistica','Acting y puesta en escena del personaje',9,'Avanzado','Mañana','Lunes','11:00',60000),(16,'Maquillaje profesional','Desarrollo de makeup para personajes',23,'Basico','Mañana','Sabado','11:30',40000),(17,'Maquillaje profesional','Desarrollo de makeup para personajes',23,'Intermedio','Tarde','Martes','15:00',45000),(18,'Maquillaje profesional','Desarrollo de makeup para personajes',23,'Avanzado','Tarde','Martes','13:00',60000),(19,'Pintura japonesa','Arte visual antiguo y contemporaneo',24,'Basico','Mañana','Sabado','9:30',40000),(20,'Pintura japonesa','Arte visual antiguo y contemporaneo',24,'Intermedio','Noche','Lunes','21:00',45000),(21,'Pintura japonesa','Arte visual antiguo y contemporaneo',24,'Avanzado','Noche','Lunes','19:00',60000);

INSERT INTO inscripciones(idInscripcion, idAlumno, idCurso, fechaInscripcion) VALUES
(1 ,5, 7, '2023-02-25 11:10:05'),(2 ,28, 11, '2023-02-22 09:40:45'),(3 ,19, 12, '2023-02-15 10:45:40'),(4 ,8, 3, '2023-03-13 14:30:45'),(5 ,32, 15, '2023-03-27 13:25:10'),(6 ,39, 7, '2023-03-21 16:25:00'),(7 ,42, 14, '2023-03-19 15:20:30'),(8 ,29, 6, '2023-04-18 14:15:20'),(9 ,36, 5, '2023-04-14 10:55:40'),(10 ,11, 5, '2023-04-20 16:50:30'),(11 ,37, 9, '2023-05-17 10:50:15'),(12 ,14, 2, '2023-05-18 09:40:25'),(13 ,40, 10, '2023-05-26 09:35:45'),(14 ,24, 8, '2023-05-30 14:50:50'),(15 ,26, 4, '2023-06-08 12:30:30'),(16 ,38, 13, '2023-06-04 13:35:55'),(17 ,41, 2, '2023-06-10 11:40:20'),(18 ,16, 10, '2023-06-12 11:55:20'),(19 ,1, 10, '2024-02-15 10:20:35'),(20 ,13, 1, '2024-02-18 15:30:22'),(21 ,31, 6, '2024-02-20 10:55:10'),(22 ,7, 9, '2024-02-22 13:45:50'),(23 ,39, 14, '2024-02-27 11:50:35'),(24 ,15, 5, '2024-03-03 14:50:35'),(25 ,10, 4, '2024-03-10 14:25:38'),(26 ,30, 7, '2024-03-15 16:30:20'),(27 ,2, 8, '2024-03-20 09:45:50'),(28 ,43, 11, '2024-06-06 09:15:00'),(29 ,21, 5, '2024-04-22 14:20:15'),(30 ,22, 12, '2024-04-30 09:25:10'),(31 ,12, 1, '2024-04-25 13:55:55'),(32 ,9, 7, '2024-04-09 11:20:27'),(33 ,18, 3, '2024-05-12 11:40:35'),(34 ,14, 2, '2024-05-15 10:40:20'),(35 ,4, 15, '2024-05-18 11:55:10'),(36 ,37, 9, '2024-05-19 13:10:25'),(37 ,6, 5, '2024-06-05 16:40:45'),(38 ,11, 6, '2024-06-01 09:10:40'),(39 ,25, 8, '2024-06-10 12:00:50'),(40 ,34, 1, '2024-06-04 12:45:30'),(41 ,27, 3, '2024-05-26 12:45:30'),(42 ,3, 12, '2024-04-12 14:30:25'),(43 ,20, 10, '2024-06-12 11:55:20'),(44 ,44, 19, '2024-06-01 10:10:30'),(45 ,45, 19, '2024-06-02 11:25:15'),(46 ,46, 20, '2024-06-03 14:40:50'),(47 ,47, 20, '2024-06-04 09:50:20'),(48 ,48, 21, '2024-06-05 12:15:35'),(49 ,49, 21, '2024-06-06 13:30:45'),(50 ,50, 21, '2024-06-07 10:50:55'),(51 ,51, 20, '2024-06-08 15:20:05'),(52 ,52, 19, '2024-06-09 11:35:25'),(53 ,53, 19, '2024-06-10 14:45:30'),(54 ,54, 20, '2024-06-11 09:20:40'),(55 ,55, 20, '2024-06-12 12:50:55'),(56 ,56, 21, '2024-06-13 16:05:10'),(57 ,57, 21, '2024-06-14 13:15:25'),(58 ,58, 21, '2024-06-15 10:05:40'),(59 ,59, 21, '2024-06-16 11:40:50'),(60 ,60, 19, '2024-06-17 14:25:00'),(61 ,61, 7, '2024-06-18 15:35:10'),(62 ,62, 3, '2024-06-19 12:10:20'),(63 ,63, 4, '2024-06-20 09:55:30');

INSERT INTO notas (idNota, idAlumno, idCurso, nota) VALUES
(1 ,14, 2, 7),(2 ,41, 2, 9),(3 ,26, 4, 6),(4 ,8, 3, 8),(5 ,24, 8, 10),(6 ,5, 7, 7),(7 ,39, 7, 9),(8 ,28, 11, 6),(9 ,11, 5, 7),(10 ,36, 5, 9),(11 ,37, 9, 8),(12 ,40, 10, 9),(13 ,16, 10, 1),(14 ,19, 12, 10),(15 ,38, 13, 9),(16 ,42, 14, 10),(17 ,32, 15, 9),(18 ,29, 6, 1),(19, 1, 10, 9),(20, 13, 1, 10),(21, 31, 6, 6),(22, 7, 9, 7),(23, 39, 14, 8),(24, 15, 5, 6),(25, 10, 4, 5),(26, 30, 7, 8),(27, 2, 8, 6),(28, 43, 11, 9),(29, 21, 5, 7),(30, 22, 12, 8),(31, 12, 1, 10),(32, 9, 7, 6),(33, 18, 3, 7),(34, 14, 2, 6),(35, 4, 15, 9),(36, 37, 9, 8),(37, 6, 5, 6),(38, 11, 6, 7),(39, 25, 8, 6),(40, 34, 1, 10),(41, 27, 3, 5),(42, 3, 12, 9),(43, 20, 10, 9),(44, 44, 19, 10),(45, 45, 19, 9),(46, 46, 20, 7),(47, 47, 21, 6),(48, 48, 21, 10),(49, 49, 20, 7),(50, 50, 19, 10),(51, 51, 19, 8),(52, 52, 19, 6),(53, 53, 20, 7),(54, 54, 21, 10),(55, 55, 21, 9),(56, 56, 21, 6),(57, 57, 20, 8),(58, 58, 20, 5),(59, 59, 7, 6),(60, 60, 7, 10),(61, 61, 7, 9),(62, 62, 4, 7),(63, 63, 4, 8);

INSERT INTO proveedores(idProveedor,nombre,mail,telefono) VALUES
(1,'Libreria San Carlos','librecarlos@gmail.com','1141234680'),(2,'Maquillaje Loreal','loreal@gmail.com','1132445789'),(3,'Atelier Manos Libres','manoslibres@gmail.com','1109873134'),(4,'Vestuarios Teatrales','vestteatro@gmail.com','1133435678'),(5,'Cuaderno de Leo','loni13@gmail.com','1112345477'),(6,'Estilismos Adrian','adrianstyle@gmail.com','1114542343'),(7,'Papeleria Goma Eva','evarosas@gmail.com','1132549812'),(8,'Pintureria Rex','rexpintureria@gmail.com','1112546787'),(9,'Pelucas Inc.','peluinc@gmail.com','1144325670'),(10,'Marta Minujin','minujin@gmail.com','1143567690'),(11,'Libreria La Dorita','ladorita@gmail.com','1111325467'),(12,'Galeria State','stategalery@gmail.com','1127879900'),(13,'Vestidos Okinaga','okinaga@gmail.com','1115436731');

INSERT INTO inventario(idInventario, nombre, idProveedor, cantidad, fechaIngreso) VALUES
(1, 'Vestido fantasia', 13, 10, '2024-10-01'),(2, 'Peluca con brillos', 9, 15, '2024-10-02'),(3, 'Papel de diseño', 1, 50, '2024-10-03'),(4, 'Lapiz negro de diseño', 8, 30, '2024-10-04'),(5, 'Maquillaje', 2, 20, '2024-10-05'),(6, 'Cuadro de acuarelas', 3, 25, '2024-10-06'),(7, 'Marcadores de Colores', 1, 8, '2024-10-07'),(8, 'Lienzo 20x30', 3, 20, '2024-10-08'),(9, 'Obra de Arte Abstracta', 3, 5,  '2024-10-09'),(10, 'Cuaderno de Bocetos', 11, 40,  '2024-10-10'),(11, 'Papel para Dibujo', 11, 60,  '2024-10-11'),(12, 'Tijeras de Corte', 6, 25, '2024-10-12'),(13, 'Sombrero Pastel', 4, 15,  '2024-10-13'),(14, 'Espejos de Maquillaje', 2, 30,  '2024-10-14'),(15, 'Goma de Borrar Grande', 1, 50,  '2024-10-15'),(16, 'Pinturas varias', 12, 8,  '2024-10-16'),(17, 'Carboncillos', 8, 25,  '2024-10-17'),(18, 'Cuaderno de Colores con artes', 5, 35,  '2024-10-18'),(19, 'Vestido de Baile', 13, 12,  '2024-10-19'),(20, 'Papel Fotográfico', 7, 100,  '2024-10-20'),(21, 'Papel para Regalo', 7, 75, '2024-10-21'),(22, 'Obra de Arte Figurativa', 3, 4, '2024-10-22'),(23, 'Pegamento en Barra', 1, 90, '2024-10-23'),(24, 'Portapinceles con diseño', 11, 30, '2024-10-24'),(25, 'Papel de Embalaje', 7, 45, '2024-10-25'),(26, 'Cuaderno de Notas', 11, 60, '2024-10-26'),(27, 'Obra de Arte Modernista', 3, 3, '2024-10-27'),(28, 'Guantes de gala largos', 4, 7, '2024-10-28'),(29, 'Tijeras de costura', 6, 30, '2024-10-29'),(30, 'Rollo de Plástico Adhesivo', 8, 20, '2024-10-30'),(31, 'Peluca rubia corta', 6, 20, '2024-10-31'),(32, 'Set arreglo pelucas', 6, 15, '2024-10-31'),(33, 'Spray para pelo', 6, 30, '2024-10-31'),(34, 'Obra figurativa', 10, 1, '2024-10-31'),(35, 'Obra conceptual', 10, 3, '2024-10-31');

INSERT INTO redesSociales(idRedSocial, plataforma, idEmpleado, fecha, descripcion, likes, seguidores, comentarios, visualizaciones) VALUES
(1, 'Instagram', 21, '2023-05-26 09:35:45', 'posteo publicitando cursos', '14', '223', '4', '37'),(2, 'Facebook', 21, '2023-05-27 10:35:45', 'posteo publicitando cursos', '11', '229', '4', '137'),(3, 'Instagram', 21, '2023-05-29 16:35:45', 'posteo publicitando evento', '17', '350', '7', '98'),(4, 'Instagram', 21, '2023-05-26 09:35:45', 'foto de los cursos', '14', '523', '24', '265'),(5, 'Facebook', 22, '2023-05-27 10:35:45', 'posteo publicitando cursos', '11', '723', '14', '370'),(6, 'TikTok', 21, '2023-05-29 16:35:45', 'posteo concurso', '17', '750', '77', '450'),(7, 'Instagram', 21, '2023-05-26 09:35:45', 'video mostrando pelucas', '14', '1223', '34', '337'),(8, 'Facebook', 22, '2023-05-27 10:35:45', 'video mostrando la escuela', '11', '1223', '4', '637'),(9, 'TikTok', 22, '2023-05-29 16:35:45', 'posteo publicitando cursos', '17', '1350', '7', '545'),(10, 'Instagram', 21, '2023-05-26 09:35:45', 'posteo publicitando taller', '14', '1223', '4', '537'),(11, 'Instagram', 22, '2023-06-01 09:40:00', 'posteo sobre confección de cosplay', '16', '300', '5', '120'),(12, 'Facebook', 21, '2023-06-02 10:45:00', 'video de cosplays en exhibición', '12', '400', '8', '180'),(13, 'TikTok', 22, '2023-06-05 11:30:00', 'posteo publicitando taller de pelucas', '18', '500', '9', '260'),(14, 'Instagram', 21, '2023-06-06 09:20:00', 'foto de la confección de un disfraz', '15', '700', '15', '350'),(15, 'Facebook', 22, '2023-06-07 14:50:00', 'posteo sobre técnicas de pelucas', '11', '800', '5', '270'),(16, 'TikTok', 21, '2023-06-10 12:25:00', 'video de peinados con pelucas', '17', '920', '10', '390'),(17, 'Instagram', 22, '2023-06-12 09:15:00', 'posteo publicitando evento de cosplay', '19', '1100', '7', '420'),(18, 'Facebook', 21, '2023-06-15 11:50:00', 'publicando el evento de pelucas', '15', '1250', '14', '500'),(19, 'TikTok', 22, '2023-06-18 13:00:00', 'posteo de un disfraz espectacular', '20', '1350', '8', '450'),(20, 'Instagram', 21, '2023-06-20 10:15:00', 'video del taller de cosplay', '16', '1400', '10', '560');



-- VISTAS --
-- Vista 1: 'ver_alumnos_por_curso'

CREATE OR REPLACE VIEW ver_alumnos_por_curso AS
SELECT COUNT(I.idAlumno) AS cantidadAlumnos, C.nombre AS curso, C.nivel AS nivel
FROM cursos AS C JOIN inscripciones AS I ON C.idCurso = I.idCurso
JOIN alumnos AS A ON A.idAlumno = I.idAlumno
WHERE A.membresiaActiva = true
GROUP BY I.idCurso
ORDER BY cantidadAlumnos DESC;

-- Invocamos la vista 1
SELECT * FROM ver_alumnos_por_curso;

-- Vista 2: 'ver_notas_altas'

CREATE OR REPLACE VIEW ver_notas_altas AS
SELECT n.idNota, n.idAlumno, a.nombre AS nombreAlumno, a.apellido AS apellidoAlumno, c.nombre AS nombreCurso, n.nota
FROM notas AS n
JOIN alumnos AS a ON n.idAlumno = a.idAlumno
JOIN cursos AS c ON n.idCurso = c.idCurso
WHERE n.nota >= 9
ORDER BY n.nota DESC;


-- Invocamos la vista 2
SELECT * FROM ver_notas_altas;

-- Vista 3: 'ver_publicaciones_por_cm'

CREATE OR REPLACE VIEW ver_publicaciones_por_cm AS
SELECT COUNT(R.idRedSocial) AS cantidadPublicaciones, E.idEmpleado, E.nombre, E.apellido
FROM redesSociales AS R JOIN empleados AS E ON R.idEmpleado = E.idEmpleado
GROUP BY E.idEmpleado
ORDER BY cantidadPublicaciones DESC;

-- Invocamos la vista 3
SELECT * FROM ver_publicaciones_por_cm;




-- FUNCIONES --
-- Función 1: calcular_salario_anual(idEmpleado)

DROP FUNCTION IF EXISTS calcular_salario_anual;
DELIMITER //

CREATE FUNCTION calcular_salario_anual(idEmpleado INT) 
RETURNS DECIMAL(20,2)
DETERMINISTIC
BEGIN
    DECLARE salarioMensual DECIMAL(20,2);
    SET salarioMensual = (SELECT P.salario FROM empleados AS E JOIN puestos AS P ON E.idPuesto = P.idPuesto WHERE E.idEmpleado = idEmpleado);
    RETURN salarioMensual * 12;
END //

DELIMITER ;

-- Invocamos la función
SELECT idEmpleado, nombre, apellido, calcular_salario_anual(idEmpleado) AS salarioAnual
FROM empleados;

-- Función 2: obtener_curso(idcurs INT)

DROP FUNCTION IF EXISTS obtener_curso;
DELIMITER $$

CREATE FUNCTION obtener_curso(idcurs INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE resultado VARCHAR(255);
    SET resultado = (SELECT C.nombre FROM cursos C JOIN inscripciones I ON C.idCurso = I.idCurso WHERE I.idAlumno = idcurs LIMIT 1);
    RETURN resultado;
END;

$$

-- Invocamos la función
SELECT nombre, apellido, obtener_curso(2) AS curso
FROM alumnos;




-- STORED PROCEDURE --
-- Stored Procedure 1 -- insertar_nota_alumno

DROP PROCEDURE if exists insertar_nota_alumno;
DELIMITER //

CREATE PROCEDURE insertar_nota_alumno(
    IN idAlumno INT,
    IN idCurso INT,
    IN nuevaNota DECIMAL(5, 2)
)
BEGIN
    DECLARE notaExistente INT;

    SELECT COUNT(*) INTO notaExistente
    FROM inscripciones AS I
    WHERE I.idAlumno = idAlumno AND I.idCurso = idCurso;

    IF notaExistente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El alumno no está inscrito en el curso.';
    ELSE
        IF nuevaNota < 0 OR nuevaNota > 10 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'La nota debe estar entre 0 y 10.';
        ELSE
            INSERT INTO notas (idAlumno, idCurso, nota)
            VALUES (idAlumno, idCurso, nuevaNota)
            ON DUPLICATE KEY UPDATE nota = nuevaNota;

            SELECT CONCAT('Nota insertada o actualizada con valor ', nuevaNota, ' para el alumno con ID ', idAlumno, ' en el curso con ID ', idCurso) AS mensaje;
        END IF;
    END IF;
END //

DELIMITER ;

-- Invocamos el SP
 CALL insertar_nota_alumno(63,4,10);


-- Stored Procedures 2 -- ingresar_alumno_activar_membresia --

DROP PROCEDURE IF EXISTS ingresar_alumno_activar_membresia;
DELIMITER //

CREATE PROCEDURE ingresar_alumno_activar_membresia(
    IN nombre VARCHAR(100),
    IN apellido VARCHAR(100),
    IN edad INT,
    IN mail VARCHAR(50),
    IN telefono VARCHAR(20),
    IN direccion VARCHAR(100),
    IN membresiaActiva BOOLEAN,
    IN idCurso INT
)
BEGIN
    INSERT INTO alumnos(idAlumno, nombre, apellido, edad, mail, telefono, direccion, membresiaActiva)
    VALUES (idAlumno, nombre, apellido, edad, mail, telefono, direccion, membresiaActiva);

    INSERT INTO inscripciones(idAlumno, idCurso, fechaInscripcion)
    VALUES (idAlumno, idCurso, CURRENT_DATE);
END 
//

DELIMITER ;

-- Invocamos el SP
CALL ingresar_alumno_activar_membresia('Juan','Perez',26, 'alumnoprueba@gmail.com', 12346784,'Torres 1345', TRUE, 21);

SELECT *
FROM alumnos
WHERE mail = 'alumnoprueba@gmail.com';


-- TRIGGER -- Inventario Historico
-- Generamos primero una tabla de inventario historico

CREATE TABLE IF NOT EXISTS inventario_historico (
    idHistorico INT PRIMARY KEY AUTO_INCREMENT,
    idInventario INT,
    nombre VARCHAR(100),
    idProveedor INT,
    cantidad INT,
    fechaIngreso DATE,
    usuario VARCHAR(200),
    operacion VARCHAR(200)
);

-- Ingreso al inventario
DROP TRIGGER IF EXISTS tg_ingreso_inventario;

DELIMITER //
CREATE TRIGGER tg_ingreso_inventario
AFTER INSERT ON inventario
FOR EACH ROW
BEGIN
    INSERT INTO inventario_historico(idInventario, nombre, idProveedor, cantidad, fechaIngreso, usuario, operacion)
    VALUES(NEW.idInventario, NEW.nombre, NEW.idProveedor, NEW.cantidad, NEW.fechaIngreso, USER(), 'INGRESO');
END;
//
DELIMITER ;

-- Modificación del inventario
DROP TRIGGER IF EXISTS tg_modificacion_inventario;

DELIMITER //
CREATE TRIGGER tg_modificacion_inventario
AFTER UPDATE ON inventario
FOR EACH ROW
BEGIN
    INSERT INTO inventario_historico(idInventario, nombre, idProveedor, cantidad, fechaIngreso, usuario, operacion)
    VALUES(NEW.idInventario, NEW.nombre, NEW.idProveedor, NEW.cantidad, NEW.fechaIngreso, USER(), 'MODIFICADO');
END;
//
DELIMITER ;

-- Eliminación del inventario
DROP TRIGGER IF EXISTS tg_eliminacion_inventario;

DELIMITER //
CREATE TRIGGER tg_eliminacion_inventario
BEFORE DELETE ON inventario
FOR EACH ROW
BEGIN
    INSERT INTO inventario_historico(idInventario, nombre, idProveedor, cantidad, fechaIngreso, usuario, operacion)
    VALUES(OLD.idInventario, OLD.nombre, OLD.idProveedor, OLD.cantidad, OLD.fechaIngreso, USER(), 'ELIMINADO');
END;
//
DELIMITER ;
drop database if exists platelink;
create database platelink;
use platelink;

create table civiles(
	idCivil int primary key auto_increment,
    nombres varchar(50) not null,
    apellidoPaterno varchar(50) not null,
    apellidoMaterno varchar(50) not null,
    fechaNacimiento date not null,
    sexo ENUM('M', 'F'),
    domicilio varchar(250) not null,
    nacionalidad varchar(50) not null,
    curp varchar(20) not null unique
);

create table vehiculos(
	idVehiculo int primary key auto_increment,
    idCivil int not null, foreign key(idCivil) references civiles(idCivil),
	numeroSerie varchar(30) not null,
    marca varchar(30) not null,
    modelo varchar(30) not null,
    anio int not null,
    color varchar(20) not null
);

create table matriculas(
	idMatricula int primary key auto_increment,
	idCivil int not null, foreign key(idCivil) references civiles(idCivil),
    idVehiculo int not null, foreign key(idVehiculo) references vehiculos(idVehiculo),
    numero varchar(12) not null unique,
    anio int not null,
    importada boolean not null
);

create table robos(
	idRobo int primary key auto_increment,
    idVehiculo int, foreign key(idVehiculo) references vehiculos(idVehiculo),
    idMatricula int, foreign key(idMatricula) references matriculas(idMatricula),
    fechaReporte datetime not null,
    fechaCierre datetime,
    detalles varchar(500)
);

create table revistas(
	idRevista int primary key auto_increment,
    idVehiculo int not null, foreign key(idVehiculo) references vehiculos(idVehiculo),
    fecha datetime not null
);

create table infracciones(
	idInfraccion int primary key auto_increment,
    descripcion varchar(100) not null
);

create table multas(
	idMulta int primary key auto_increment,
    idCivil int not null, foreign key(idCivil) references civiles(idCivil),
    idInfraccion int not null, foreign key(idInfraccion) references infracciones(idInfraccion),
    fechaMulta datetime not null,
    fechaPago datetime,
    costo float not null
);





insert into infracciones(descripcion) values ("Transitar sin placas");
insert into infracciones(descripcion) values ("Manejar sin licencia");
insert into infracciones(descripcion) values ("Obstruir paso a peaton");
insert into infracciones(descripcion) values ("Manejar en estado de ebriedad");
insert into infracciones(descripcion) values ("Exceso de entre 1 a 20kmh sobre limite de velocidad");
insert into infracciones(descripcion) values ("Exceso de entre 21 a 30kmh sobre limite de velocidad");
insert into infracciones(descripcion) values ("Exceso de entre 31 a 40kmh sobre limite de velocidad");
insert into infracciones(descripcion) values ("Exceso de mas de 41kmh sobre limite de velocidad");
insert into infracciones(descripcion) values ("Estacionarse en doble fila");
insert into infracciones(descripcion) values ("Pasarse alto(rojo) del semaforo");

insert into civiles(nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, domicilio, nacionalidad, curp)
		values("Jesus Enrique", "Dominguez", "Maruko", "2001-04-05", 'M', "Manaca 113", "Mexicana", "DOMJ010405HBSMRSA6");
insert into civiles(nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, domicilio, nacionalidad, curp)
		values("Aldo Efrain", "Castro", "Barajas", "2001-08-07", 'M', "Lopez Mateo 22", "Mexicana", "CABA010807HBSSRLA7");
insert into civiles(nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, domicilio, nacionalidad, curp)
		values("Alan", "Gonzalez de la Llave", "Achoy", "2001-07-27", 'M', "Huichol 59", "Mexicana", "GOAA010727HBSNCLA1");
insert into civiles(nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, domicilio, nacionalidad, curp)
		values("Diego Alejandro", "Ochoa", "Duarte", "2001-10-05", 'M', "Barandal 30", "Mexicana", "OODD011005HBSCRGA5");
insert into civiles(nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, sexo, domicilio, nacionalidad, curp)
		values("Brandon Luis", "Barrera", "Monteverde", "2001-08-15", 'M', "Toronja 52", "Mexicana", "BAMB010815HBSMTSA2");

insert into vehiculos(idCivil, numeroSerie, marca, modelo, anio, color)
		values(1, "WDBRF52H76F783280", "Mercedes Benz", "C Class", 2006, "Rojo");
insert into vehiculos(idCivil, numeroSerie, marca, modelo, anio, color)
		values(2, "4T1BE30K12U058669", "Toyota", "Camry", 2002, "Negro");
insert into vehiculos(idCivil, numeroSerie, marca, modelo, anio, color)
		values(3, "JH4DA9440PS002537", "Honda", "Acura Integra", 2008, "Blanco");
insert into vehiculos(idCivil, numeroSerie, marca, modelo, anio, color)
		values(4, "1B4GP54R2VB378393", "Ford", "Mustang", 2003, "Amarillo");
insert into vehiculos(idCivil, numeroSerie, marca, modelo, anio, color)
		values(5, "WP1AB29P99LA40680", "Porsche", "Cayenne", 2009, "Gris");

insert into matriculas(idCivil, idVehiculo, numero, anio, importada)
		values(1, 1, "521-PNJ-8", 2023, true);
insert into matriculas(idCivil, idVehiculo, numero, anio, importada)
		values(2, 2, "217-PNE-9", 2023, true);
insert into matriculas(idCivil, idVehiculo, numero, anio, importada)
		values(3, 3, "388-PNK-7", 2023, false);
insert into matriculas(idCivil, idVehiculo, numero, anio, importada)
		values(4, 4, "653-PNK-1", 2023, false);
insert into matriculas(idCivil, idVehiculo, numero, anio, importada)
		values(5, 5, "877-PNL-1", 2023, true);

insert into robos(idVehiculo, idMatricula, fechaReporte, fechaCierre, detalles)
		values(2, null, "2023-06-10 12:35:15", null, "Robo a mano armada mientras trabajaba de uber");
insert into robos(idVehiculo, idMatricula, fechaReporte, fechaCierre, detalles)
		values(4, null, "2023-09-12 17:12:48", null, "Fui al cine de soriana forjadores a ver una pelicula y al salir ya no estaba mi vehiculo");

insert into revistas(idVehiculo, fecha)
		values(3, "2021-12-12 23:30:00");
insert into revistas(idVehiculo, fecha)
		values(1, "2023-02-04 12:00:00");
insert into revistas(idVehiculo, fecha)
		values(2, "2023-02-15 14:30:00");
insert into revistas(idVehiculo, fecha)
		values(4, "2023-02-24 11:00:00");
insert into revistas(idVehiculo, fecha)
		values(5, "2023-02-26 13:45:00");

insert into multas(idCivil, idInfraccion, fechaMulta, fechaPago, costo)
		values(4, 1, "2023-04-12 22:00:00", "2023-04-15 14:30:00", 500);
insert into multas(idCivil, idInfraccion, fechaMulta, fechaPago, costo)
		values(4, 2, "2023-04-12 22:00:00", "2023-04-15 14:30:00", 300);
insert into multas(idCivil, idInfraccion, fechaMulta, fechaPago, costo)
		values(4, 9, "2023-05-17 15:30:00", "2023-05-22 17:00:00", 1000);
insert into multas(idCivil, idInfraccion, fechaMulta, fechaPago, costo)
		values(3, 3, "2023-07-27 23:20:00", null, 550);
insert into multas(idCivil, idInfraccion, fechaMulta, fechaPago, costo)
		values(2, 10, "2023-08-07 14:00:00", "23-08-10 16:00:00", 7000);



delimiter $$
drop procedure if exists datosMatricula$$
create procedure datosMatricula( in numeroMatricula varchar(12))
begin

	declare xidMatricula int;
    declare xidCivil int;
    declare xidVehiculo int;
    
    set xidMatricula = (select idMatricula from matriculas where numero = numeroMatricula);
    set xidCivil = (select idCivil from matriculas where idMatricula = xidMatricula);
    set xidVehiculo = (select idVehiculo from matriculas where idMatricula = xidMatricula);
    
	drop temporary table if exists infoMatricula;
	create temporary table infoMatricula (
		numeroM varchar(12),
        anioM int,
        importadaM boolean,
        
        nombresC varchar(50),
        apellidoPaternoC varchar(50),
        apellidoMaternoC varchar(50), 
        curpC varchar(20),
        
        numeroSerieV varchar(30),
        marcaV varchar(30),
        modeloV varchar(30),
        anioV int, 
        colorV varchar(20),
        
        ultimaRevistaR datetime
	);
    
    insert into infoMatricula values(
		(select numero from matriculas where idMatricula = xidMatricula),
        (select anio from matriculas where idMatricula = xidMatricula),
        (select importada from matriculas where idMatricula = xidMatricula),
        
        (select nombres from civiles where idCivil = xidCivil),
        (select apellidoPaterno from civiles where idCivil = xidCivil),
        (select apellidoMaterno from civiles where idCivil = xidCivil),
        (select curp from civiles where idCivil = xidCivil),
        
        (select numeroSerie from vehiculos where idVehiculo = xidVehiculo),
        (select marca from vehiculos where idVehiculo = xidVehiculo),
        (select modelo from vehiculos where idVehiculo = xidVehiculo),
        (select anio from vehiculos where idVehiculo = xidVehiculo),
        (select color from vehiculos where idVehiculo = xidVehiculo),
        
        (select fecha from revistas where idVehiculo = xidVehiculo)
    );
    
    select * from infoMatricula;
end$$

/*call datosMatricula("653-PNK-1");

select * from matriculas where numero="653-PNK-1";*/
-- Kevin GIlberto Niño Vargas Y Santiago Tapia Bolaños 

SELECT Nombre, Telefono 
FROM profesores;

SELECT Nombre, Telefono 
FROM programas
WHERE Depto = 1 ;

SELECT idprofesor, idproyecto
FROM Participacion_proyectos
WHERE idprofesor = 3333;

SELECT idprofesor, idproyecto
FROM Participacion_proyectos
WHERE idproyecto = 2;

SELECT idprofesor, idproyecto, Horas
FROM Participacion_proyectos
WHERE Horas > 5;

SELECT idprofesor, idproyecto, Horas
FROM Participacion_proyectos
WHERE Horas >= 4 AND Horas <= 6;

SELECT idprofesor, idproyecto, Horas
FROM Participacion_proyectos
WHERE Horas BETWEEN 4 AND 6;

UPDATE departamentos 
SET jefe = 3333
WHERE idDepartamento = 1;

SELECT * 
FROM programas
WHERE Depto = 1 or Depto = 3 ;

SELECT * 
FROM programas
WHERE Depto in(1,3) ;

SELECT idProyecto, Presupuesto
FROM proyectos;

SELECT idProyecto, Presupuesto
FROM proyectos
ORDER BY presupuesto;

SELECT idProyecto, Presupuesto
FROM proyectos
ORDER BY presupuesto;

-- DOS TABLAS


SELECT profesores.Nombre AS PROFESOR, programas.Nombre AS PROGRAMA
FROM profesores INNER JOIN programas
ON programas.idPrograma = profesores.Programa;

SELECT profesores.nombre AS 'PROFESOR JEFE', departamentos.nombre AS DEPARTAMENTO
FROM profesores INNER JOIN departamentos
ON profesores.idProfesor = departamentos.Jefe;


SELECT proyectos.Nombre , profesores.Nombre AS 'PROFESOR LIDER', proyectos.Presupuesto
FROM proyectos INNER JOIN profesores
ON profesores.idProfesor = proyectos.Lider;

-- TRES TABLAS 

SELECT profesores.nombre AS Profe, proyectos.nombre as Proy, participacion_proyectos.horas as Horas
FROM(participacion_proyectos INNER JOIN profesores
ON participacion_proyectos.idProfesor = Profesores.idProfesor) 
INNER JOIN proyectos
ON participacion_proyectos.idProyecto = proyectos.idProyecto;



-- nombre fuente, nombre proyecto, monto

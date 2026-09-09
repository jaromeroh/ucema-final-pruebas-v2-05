# Proceso documentado

Construcción docente en una sesión; no se atribuyen despliegues ni revisiones humanas inexistentes.

## Decisión 1: cálculos reproducibles
Se suman importes con Decimal y se calcula la variación sobre los totales, no promediando porcentajes regionales. Los tests comprueban totales, pérdidas por región y una base previa nula.

## Decisión 2: evitar crecimiento inventado
Cuando no hay ventas previas, change_percent es null. El modelo debe explicar la ausencia de base comparable y no informar un porcentaje infinito o arbitrario.

## Decisión 3: alcance comercial acotado
La salida propone una revisión; no sustituye una validación contable ni decide precios o gastos. No se conserva una iteración previa desplegada del sistema.

## Evidencia y limitaciones de la historia
Las pruebas guardadas muestran verificaciones realizadas sobre los archivos incluidos. El historial Git permite ubicar implementación y documentación. No se conserva una conversación completa con la IA ni una validación de campo empresarial. Las corridas preservan las instrucciones efectivamente enviadas al modelo; esas sí pueden auditarse literalmente.

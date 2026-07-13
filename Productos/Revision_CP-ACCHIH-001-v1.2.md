# Revisión técnica de la Política de Certificación CP-ACCHIH-001 v1.2

Este documento registra los ajustes que deberán incorporarse a la Política de Certificación antes de su aprobación definitiva. Se mantiene separado temporalmente para facilitar la revisión del cambio normativo frente al documento vigente.

## 1. Conservación documental

Sustituir cualquier referencia que condicione la conservación a la capacidad de almacenamiento por la siguiente regla:

> La plataforma institucional conservará copia íntegra de los documentos firmados hasta por diez años, conforme a los controles de seguridad, disponibilidad, integridad, acceso y conservación aplicables. Esta conservación no sustituye las obligaciones archivísticas de la dependencia responsable del documento o expediente.

## 2. Referencia de tiempo cierto

Establecer como referencia temporal la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya.

Los servicios de sincronización en nube podrán utilizarse como medios técnicos auxiliares, siempre que mantengan trazabilidad respecto de la referencia oficial y del Tiempo Universal Coordinado.

## 3. Neutralidad tecnológica

La CP deberá describir capacidades y controles, sin amarrarse a marcas, productos o proveedores específicos. Los detalles de implementación deberán documentarse en la CPS y en procedimientos internos.

## 4. Arquitectura PKI

La arquitectura vigente mediante una AC raíz emisora en línea deberá reconocerse como transitoria y sujeta a controles compensatorios.

La arquitectura objetivo será una AC raíz fuera de línea y una o más autoridades intermedias subordinadas emisoras.

## 5. Separación criptográfica

La clave de la AC raíz no deberá utilizarse para sellado de tiempo, cifrado de datos, firma de documentos de usuario final, autenticación de cliente o servidor ni firma de código.

Los servicios OCSP y TSA deberán contar con claves y certificados independientes y perfiles restringidos a sus funciones.

## 6. Historial y control documental

Mantener consistencia entre la versión indicada en portada, la tabla de control documental y el historial de versiones. La revisión deberá registrar los cambios de neutralidad tecnológica, conservación, sellado de tiempo y arquitectura PKI.

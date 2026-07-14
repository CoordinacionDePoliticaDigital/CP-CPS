# Revisión técnica de la Política de Certificación CP-ACCHIH-001 v1.2

**IANA PEN institucional:** `1.3.6.1.4.1.63888`

Este documento registra los ajustes que deberán incorporarse a la Política de Certificación antes de su aprobación definitiva. Se mantiene separado temporalmente para facilitar la revisión del cambio normativo frente al documento vigente.

## 1. Conservación documental

Sustituir cualquier referencia que condicione la conservación a la capacidad de almacenamiento por la siguiente regla:

> La plataforma institucional conservará copia íntegra de los documentos firmados hasta por diez años. Este plazo constituye el periodo máximo ordinario de conservación prestado por la plataforma, no un plazo mínimo aplicable a todos los expedientes. La conservación no sustituye las obligaciones archivísticas de la dependencia responsable. La eliminación al concluir el plazo solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que requiera conservar el documento o sus evidencias por más tiempo, y cuando se haya efectuado la transferencia documental que corresponda.

## 2. Referencia de tiempo cierto

Establecer como referencia temporal la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya.

Los servicios de sincronización podrán utilizarse como medios técnicos auxiliares, siempre que mantengan trazabilidad respecto de la referencia oficial y del Tiempo Universal Coordinado. La tolerancia máxima y el método de medición deberán definirse una sola vez en la CPS y ser referenciados por la política de sellado de tiempo.

## 3. Neutralidad tecnológica

La CP deberá describir capacidades y controles, sin amarrarse a marcas, productos o proveedores específicos. Los detalles de implementación deberán documentarse en la CPS y en procedimientos internos.

## 4. Arquitectura PKI

La arquitectura vigente mediante una AC raíz emisora en línea deberá reconocerse como transitoria y sujeta a controles compensatorios. El certificado vigente conserva la restricción de longitud de ruta con la que fue emitido hasta su expiración o revocación.

La arquitectura objetivo será AC raíz fuera de línea → AC intermedia emisora → certificado de entidad final. La raíz objetivo deberá utilizar `pathLenConstraint=1` y cada intermedia emisora `pathLenConstraint=0`; no se permitirá que las intermedias emitan otras autoridades subordinadas.

La transición requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, publicación de perfiles y cadenas, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de CP y CPS.

## 5. Separación criptográfica

La clave de la AC raíz no deberá utilizarse para sellado de tiempo, cifrado de datos, firma de documentos de usuario final, autenticación de cliente o servidor ni firma de código.

Los servicios OCSP y TSA deberán contar con claves y certificados independientes. El perfil autoritativo del certificado TSA será el apartado 4.2 del Anexo A; los demás documentos deberán referenciarlo sin duplicar sus reglas.

## 6. OID institucionales

Los OID de políticas, perfiles y servicios deberán asignarse y registrarse bajo el PEN institucional `1.3.6.1.4.1.63888`. Se mantienen como identificadores documentales aprobados:

- CP: `1.3.6.1.4.1.63888.1.1`;
- CPS: `1.3.6.1.4.1.63888.1.2`.

Cualquier OID adicional deberá incorporarse al catálogo institucional antes de su uso productivo.

## 7. Historial y control documental

Mantener consistencia entre la versión indicada en portada, la tabla de control documental y el historial de versiones. La revisión deberá registrar los cambios de neutralidad tecnológica, conservación, sellado de tiempo, arquitectura PKI y OID institucionales.

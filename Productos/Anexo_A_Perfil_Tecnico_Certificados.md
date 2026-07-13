# Anexo A. Perfil Técnico de Certificados

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.3  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

> Este documento distingue entre los perfiles actualmente desplegados y los perfiles objetivo aprobados para nuevas emisiones o para la siguiente generación de la infraestructura. Los certificados productivos existentes conservarán las extensiones con las que fueron emitidos hasta su expiración o revocación. La CPS deberá documentar expresamente esta coexistencia y el plan de transición.

## 1. Disposiciones generales

Los certificados deberán cumplir con X.509 versión 3, RFC 5280 y los perfiles técnicos aprobados por la Autoridad de Certificación.

Los números de serie deberán ser únicos dentro del ámbito de la autoridad emisora y generarse mediante un mecanismo que evite colisiones y secuencias predecibles.

Los algoritmos y longitudes de clave deberán revisarse periódicamente conforme al estado de la técnica, análisis de riesgo y compatibilidad de los sistemas institucionales.

Los identificadores de política, perfiles y servicios deberán asignarse bajo el arco institucional `1.3.6.1.4.1.63888` y registrarse en el catálogo de OID de la Autoridad de Certificación antes de su uso productivo.

Los perfiles objetivo definidos en este anexo no modificarán retroactivamente los certificados ya emitidos. Cuando un certificado vigente no cumpla el perfil objetivo, deberá identificarse como certificado de transición y no podrá utilizarse como referencia para nuevas emisiones una vez habilitado el perfil corregido.

## 2. Certificado de la AC raíz

### 2.1. Perfil vigente de transición

El certificado raíz actualmente desplegado conserva las extensiones con las que fue emitido. De acuerdo con el certificado productivo incorporado al repositorio, incluye usos de clave más amplios y una extensión de sellado de tiempo. Estas características se documentan como condición vigente de transición y no como perfil autorizado para una nueva raíz.

El certificado raíz vigente no deberá volver a emitirse con dicho conjunto de extensiones. Su operación deberá sujetarse a controles compensatorios, monitoreo reforzado, restricción de permisos y al plan de migración hacia la arquitectura objetivo.

### 2.2. Perfil objetivo de la AC raíz

| Campo | Valor o regla |
|---|---|
| Versión | X.509 v3 |
| Subject | Igual al Issuer por tratarse de un certificado autofirmado |
| Issuer | `CN=Autoridad de Certificación de Gobierno del Estado de Chihuahua, E=autoridad.certificadora@chihuahua.gob.mx, O=Gobierno del Estado de Chihuahua, OU=Coordinación de Política Digital, L=Chihuahua, S=Chihuahua, C=MX, PostalCode=31000` |
| Vigencia máxima | Quince años |
| Algoritmo de clave pública | RSA |
| Longitud de clave | 4096 bits |
| Algoritmo de firma | SHA-512 con RSA, conforme a la configuración productiva autorizada |
| Basic Constraints | Crítica: `CA=TRUE` |
| Path Length Constraint | `pathLenConstraint=1`, para permitir únicamente la cadena AC raíz → AC intermedia emisora → certificado de entidad final |
| Key Usage | Crítica: `keyCertSign`, `cRLSign` |
| Extended Key Usage | No deberá incluirse |
| Subject Key Identifier | No crítica |
| Authority Key Identifier | Conforme al perfil aplicable |

### 2.3. Restricciones de uso del perfil objetivo

El certificado de la AC raíz no deberá utilizarse para:

a) Firmar documentos de usuario final;  
b) Firmar sellos de tiempo;  
c) Cifrar datos;  
d) Autenticación de cliente o servidor;  
e) Firma de código;  
f) Cualquier finalidad distinta de la emisión de certificados de autoridades subordinadas y firma de listas de revocación conforme al perfil autorizado.

### 2.4. Jerarquía autorizada

La arquitectura objetivo permitirá una sola capa de autoridades intermedias subordinadas. Las autoridades intermedias podrán ser múltiples y operar como emisoras hermanas, pero no podrán emitir otras autoridades subordinadas.

Cada AC intermedia emisora deberá utilizar `pathLenConstraint=0`.

La transición desde la raíz emisora directa requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, perfiles aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de la CPS.

## 3. Certificados de usuario final

### 3.1. Perfil vigente de transición

Los certificados de usuario final actualmente emitidos conservan las extensiones con las que fueron generados. De acuerdo con los certificados productivos incorporados al repositorio, pueden incluir `clientAuth` y `emailProtection`, además de usos de clave no requeridos por el perfil objetivo de firma electrónica avanzada.

Estos certificados permanecerán reconocidos hasta su expiración o revocación, conforme a la CP y CPS vigentes. No deberán utilizarse como plantilla para nuevas emisiones una vez habilitado el perfil objetivo.

### 3.2. Perfil objetivo de usuario final

| Campo | Valor o regla |
|---|---|
| Versión | X.509 v3 |
| Issuer | Autoridad de Certificación de Gobierno del Estado de Chihuahua o AC intermedia emisora autorizada |
| Vigencia máxima | Cuatro años |
| Algoritmo de clave pública | RSA |
| Longitud mínima | 2048 bits |
| Algoritmo de firma | SHA-256 con RSA o superior |
| Basic Constraints | Crítica: `CA=FALSE` |
| Key Usage | Crítica: `digitalSignature`, `contentCommitment` cuando resulte compatible |
| Extended Key Usage | El perfil general de firma electrónica avanzada no incluirá EKU. No se permiten `clientAuth`, `serverAuth`, `emailProtection`, `codeSigning`, `timeStamping`, `OCSPSigning` ni otros usos extendidos en este perfil. Cualquier EKU deberá pertenecer a un perfil distinto, expresamente aprobado y asociado a su propio OID bajo `1.3.6.1.4.1.63888`. |
| Subject Key Identifier | No crítica |
| Authority Key Identifier | No crítica |
| CRL Distribution Points | Cuando corresponda |
| Authority Information Access | Deberá incluir acceso al servicio OCSP cuando corresponda |
| Certificate Policies | Deberá identificar la política aplicable mediante OID autorizado bajo el PEN institucional |

### 3.3. Atributos del Subject

Podrán utilizarse, conforme al tipo de titular:

| Atributo | Uso |
|---|---|
| `CN` | Nombre completo de la persona titular |
| `serialNumber` | Identificador autorizado de la persona titular |
| `2.5.4.45` | Identificador único autorizado conforme al perfil institucional |
| `E` o `emailAddress` | Correo electrónico |
| `O` | Dependencia, entidad u organización relacionada |
| `OU` | Unidad administrativa |
| `L` | Localidad |
| `S` | Entidad federativa |
| `C` | País |
| `postalCode` | Código postal, cuando resulte necesario |

La CPS deberá definir el mapeo exacto de CURP, RFC y otros identificadores, evitando duplicidades, ambigüedades y exposición innecesaria de datos personales.

## 4. Certificados de infraestructura

Los certificados de OCSP, TSA y demás servicios de infraestructura deberán utilizar claves independientes y perfiles separados.

### 4.1. Certificado OCSP

Deberá incluir exclusivamente los usos necesarios para firmar respuestas OCSP y la extensión `id-kp-OCSPSigning` (`1.3.6.1.5.5.7.3.9`), conforme al RFC 6960. La extensión EKU deberá ser crítica y no contener otros usos.

### 4.2. Certificado TSA

Deberá utilizarse exclusivamente para sellado de tiempo e incluir una extensión `Extended Key Usage` marcada como crítica, cuyo único valor permitido será `timeStamping` (`1.3.6.1.5.5.7.3.8`). No deberá contener usos extendidos adicionales.

La clave de la TSA deberá ser independiente de la clave de la AC raíz y de las claves utilizadas para otros servicios.

Los certificados TSA productivos existentes deberán verificarse contra este perfil. Cualquier diferencia deberá documentarse en la CPS como condición de transición, junto con su fecha de expiración, controles compensatorios y plan de sustitución.

## 5. Revisión criptográfica

La Autoridad de Certificación deberá revisar periódicamente:

a) Algoritmos de firma;  
b) Longitudes de clave;  
c) Funciones hash;  
d) Compatibilidad con clientes y validadores;  
e) Recomendaciones de organismos técnicos reconocidos;  
f) Riesgos de obsolescencia criptográfica.

Cualquier cambio que afecte la confianza, compatibilidad o validez de los certificados deberá someterse al procedimiento de gestión de cambios autorizado.

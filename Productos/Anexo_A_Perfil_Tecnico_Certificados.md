# Anexo A. Perfil Técnico de Certificados

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

> Este documento define los perfiles técnicos mínimos de los certificados emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua. Los valores definitivos deberán corresponder con los certificados publicados en el repositorio oficial y con la configuración vigente documentada en la Declaración de Prácticas de Certificación.

## 1. Disposiciones generales

Los certificados deberán cumplir con X.509 versión 3, RFC 5280 y los perfiles técnicos aprobados por la Autoridad de Certificación.

Los números de serie deberán ser únicos dentro del ámbito de la autoridad emisora y generarse mediante un mecanismo que evite colisiones y secuencias predecibles.

Los algoritmos y longitudes de clave deberán revisarse periódicamente conforme al estado de la técnica, análisis de riesgo y compatibilidad de los sistemas institucionales.

Los identificadores de política, perfiles y servicios deberán asignarse bajo el arco institucional `1.3.6.1.4.1.63888` y registrarse en el catálogo de OID de la Autoridad de Certificación antes de su uso productivo.

## 2. Perfil del certificado de la AC raíz

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
| Path Length Constraint | Arquitectura vigente: ausente o `None`, por tratarse de la raíz emisora directa desplegada. Arquitectura objetivo: `pathLenConstraint=1` para permitir únicamente la cadena AC raíz → AC intermedia emisora → certificado de entidad final. Cada AC intermedia emisora deberá utilizar `pathLenConstraint=0`. |
| Key Usage | Crítica: `keyCertSign`, `cRLSign` |
| Subject Key Identifier | No crítica |
| Authority Key Identifier | Conforme al perfil aplicable |

### 2.1. Restricciones de uso

El certificado de la AC raíz no deberá utilizarse para:

a) Firmar documentos de usuario final;  
b) Firmar sellos de tiempo;  
c) Cifrar datos;  
d) Autenticación de cliente o servidor;  
e) Firma de código;  
f) Cualquier finalidad distinta de la emisión de certificados y firma de listas de revocación conforme al perfil autorizado.

El certificado raíz no deberá incluir `Extended Key Usage`.

### 2.2. Jerarquía autorizada

La arquitectura objetivo permitirá una sola capa de autoridades intermedias subordinadas. Las autoridades intermedias podrán ser múltiples y operar como emisoras hermanas, pero no podrán emitir otras autoridades subordinadas.

La transición desde la raíz emisora directa requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, perfiles aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de la CPS.

## 3. Perfil de certificados de usuario final

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

### 3.1. Atributos del Subject

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

## 5. Revisión criptográfica

La Autoridad de Certificación deberá revisar periódicamente:

a) Algoritmos de firma;  
b) Longitudes de clave;  
c) Funciones hash;  
d) Compatibilidad con clientes y validadores;  
e) Recomendaciones de organismos técnicos reconocidos;  
f) Riesgos de obsolescencia criptográfica.

Cualquier cambio que afecte la confianza, compatibilidad o validez de los certificados deberá someterse al procedimiento de gestión de cambios autorizado.

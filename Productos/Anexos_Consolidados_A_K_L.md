# Anexos consolidados A, K y L

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión del consolidado:** 1.2  
**Estado:** Documento derivado  
**Fuente de verdad:** archivos individuales indicados en el manifiesto  

> Este archivo es generado automáticamente. No deberá editarse de forma manual. Cualquier modificación normativa deberá realizarse en el anexo individual correspondiente y después regenerar este consolidado.

## Manifiesto de fuentes

| Fuente autoritativa | SHA-256 |
|---|---|
| `Productos/Anexo_A_Perfil_Tecnico_Certificados.md` | `22857718c84c9193375b5cb97d8f0e92b2ea3192da3294fdc15a29aba73e84ad` |
| `Productos/Anexo_K_Perfil_PAdES.md` | `23502d39e815b481b53ab3c236ccf0f993af391a71afc1c3731e4a2b16d54d2a` |
| `Productos/Anexo_L_Politica_Sellado_Tiempo.md` | `f23550e494093101f7140f7b46cfeb46d51907355dcfa02b561fd593ecddbb2f` |

---

## Anexo A. Perfil Técnico de Certificados

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

> Este documento distingue entre los perfiles desplegados actualmente y los perfiles objetivo para nuevas emisiones. Los certificados vigentes conservan las extensiones con las que fueron emitidos hasta su expiración o revocación; no deberán utilizarse como plantilla para nuevas emisiones cuando contradigan el perfil objetivo. La Declaración de Prácticas de Certificación deberá documentar la coexistencia, los controles compensatorios y el plan de transición.

### 1. Disposiciones generales

Los certificados deberán cumplir con X.509 versión 3, RFC 5280 y los perfiles técnicos aprobados por la Autoridad de Certificación.

Los números de serie deberán ser únicos dentro del ámbito de la autoridad emisora y generarse mediante un mecanismo que evite colisiones y secuencias predecibles.

Los algoritmos y longitudes de clave deberán revisarse periódicamente conforme al estado de la técnica, análisis de riesgo y compatibilidad de los sistemas institucionales.

Los identificadores de política, perfiles y servicios deberán asignarse bajo el arco institucional `1.3.6.1.4.1.63888` y registrarse en el catálogo de OID de la Autoridad de Certificación antes de su uso productivo.

### 2. Perfil del certificado de la AC raíz

#### 2.1. Perfil vigente de transición

El certificado raíz actualmente desplegado conserva los valores con los que fue emitido, incluyendo usos de clave y EKU más amplios que el perfil objetivo. Su reconocimiento no autoriza nuevos certificados raíz con esas extensiones ni habilita su utilización material para fines ajenos a la emisión y administración de certificados.

Mientras permanezca vigente deberán aplicarse controles compensatorios que impidan su uso para firma de documentos, cifrado, autenticación o sellado de tiempo.

#### 2.2. Perfil objetivo

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
| Path Length Constraint | Arquitectura objetivo: `pathLenConstraint=1` para permitir únicamente la cadena AC raíz → AC intermedia emisora → certificado de entidad final. Cada AC intermedia emisora deberá utilizar `pathLenConstraint=0`. |
| Key Usage | Crítica: `keyCertSign`, `cRLSign` |
| Subject Key Identifier | No crítica |
| Authority Key Identifier | Conforme al perfil aplicable |

El certificado raíz objetivo no deberá incluir `Extended Key Usage`.

#### 2.3. Restricciones de uso

El certificado de la AC raíz no deberá utilizarse para:

a) Firmar documentos de usuario final;  
b) Firmar sellos de tiempo;  
c) Cifrar datos;  
d) Autenticación de cliente o servidor;  
e) Firma de código;  
f) Cualquier finalidad distinta de la emisión de certificados y firma de listas de revocación conforme al perfil autorizado.

#### 2.4. Jerarquía autorizada

La arquitectura objetivo permitirá una sola capa de autoridades intermedias subordinadas. Las autoridades intermedias podrán ser múltiples y operar como emisoras hermanas, pero no podrán emitir otras autoridades subordinadas.

La transición desde la raíz emisora directa requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, perfiles aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de la CPS.

### 3. Perfil de certificados de usuario final

#### 3.1. Perfil vigente de transición

Los certificados de usuario final actualmente emitidos podrán conservar los EKU `clientAuth` y `emailProtection` cuando formen parte de su configuración original. Su permanencia no autoriza nuevas emisiones con esos EKU bajo el perfil general de firma electrónica avanzada.

#### 3.2. Perfil objetivo

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

#### 3.3. Atributos del Subject

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

### 4. Certificados de infraestructura

Los certificados de OCSP, TSA y demás servicios de infraestructura deberán utilizar claves independientes y perfiles separados.

#### 4.1. Certificado OCSP

Deberá incluir exclusivamente los usos necesarios para firmar respuestas OCSP y la extensión `id-kp-OCSPSigning` (`1.3.6.1.5.5.7.3.9`), conforme al RFC 6960. La extensión EKU deberá ser crítica y no contener otros usos.

Cada autoridad emisora deberá contar con un certificado de respondedor OCSP delegado emitido directamente por esa misma autoridad. El respondedor utilizado para certificados emitidos por la AC raíz deberá ser emitido por la AC raíz; el respondedor utilizado para certificados emitidos por una AC intermedia deberá ser emitido directamente por dicha intermedia. No deberá reutilizarse un certificado OCSP emitido por una autoridad distinta para responder por certificados fuera de su ámbito de emisión.

#### 4.2. Certificado TSA

Deberá utilizarse exclusivamente para sellado de tiempo e incluir una extensión `Extended Key Usage` marcada como crítica, cuyo único valor permitido será `timeStamping` (`1.3.6.1.5.5.7.3.8`). No deberá contener usos extendidos adicionales.

La clave de la TSA deberá ser independiente de la clave de la AC raíz y de las claves utilizadas para otros servicios.

### 5. Revisión criptográfica

La Autoridad de Certificación deberá revisar periódicamente:

a) Algoritmos de firma;  
b) Longitudes de clave;  
c) Funciones hash;  
d) Compatibilidad con clientes y validadores;  
e) Recomendaciones de organismos técnicos reconocidos;  
f) Riesgos de obsolescencia criptográfica.

Cualquier cambio que afecte la confianza, compatibilidad o validez de los certificados deberá someterse al procedimiento de gestión de cambios autorizado.

---

## Anexo K. Perfil PAdES Institucional

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

### 1. Objeto

El presente anexo define el perfil mínimo para las firmas electrónicas avanzadas aplicadas a documentos PDF mediante la plataforma institucional.

### 2. Estándar base

La plataforma institucional utilizará firmas PAdES conforme a la familia de estándares ETSI EN 319 142.

El nivel mínimo será **PAdES Baseline B-T**, que incorpora un sello de tiempo sobre la firma y permite acreditar una referencia temporal confiable asociada al acto de firma.

PAdES-B-T no deberá considerarse, por sí solo, un mecanismo completo de validación a largo plazo. Cuando el periodo de conservación, el valor probatorio o el riesgo del documento lo requieran, deberán incorporarse los elementos necesarios para conformidad **PAdES Baseline B-LT** o **PAdES Baseline B-LTA**.

#### 2.1. Matriz de conformidad

| Nivel | Firma Baseline B | Sello de tiempo RFC 3161 sobre la firma | Certificados y cadena incorporados | Evidencias de revocación incorporadas | Sellos de archivo posteriores | Regla de conformidad |
|---|---:|---:|---:|---:|---:|---|
| PAdES B-T | Obligatorio | Obligatorio | Opcional dentro del PDF; deberán conservarse como evidencia asociada | Opcional dentro del PDF; deberán conservarse como evidencia asociada | No requerido | No podrá declararse B-T sin sello de tiempo válido sobre la firma. |
| PAdES B-LT | Obligatorio | Obligatorio | Obligatorio | Obligatorio | No requerido | El PDF deberá contener el material necesario para validar la firma y el estado de los certificados sin depender de la disponibilidad inmediata de servicios externos. |
| PAdES B-LTA | Obligatorio | Obligatorio | Obligatorio | Obligatorio | Obligatorio | Además de cumplir B-LT, el PDF deberá incorporar uno o más sellos de archivo que protejan la firma y su material de validación para conservación prolongada. |

La presencia de una representación visual, hoja de firmas, código QR o folio no determina el nivel de conformidad PAdES.

### 3. Algoritmos

| Elemento | Requisito mínimo |
|---|---|
| Función hash | SHA-256 o superior |
| Algoritmo de firma | RSA con clave de al menos 2048 bits, o algoritmo autorizado equivalente |
| Sello de tiempo | RFC 3161 |
| Certificado de firmante | Certificado vigente y no revocado al momento de la firma |
| Certificado TSA | Conforme al perfil autoritativo definido en el apartado 4.2 del Anexo A |

Los algoritmos deberán revisarse conforme al estado de la técnica y a la política criptográfica institucional.

### 4. Validación al momento de firma

La plataforma deberá verificar, al menos:

a) Integridad del documento;  
b) Correspondencia entre la firma y el certificado;  
c) Vigencia del certificado;  
d) Estado de revocación mediante OCSP y, cuando proceda, CRL;  
e) Cadena de confianza;  
f) Uso permitido del certificado;  
g) Validez del sello de tiempo;  
h) Correspondencia entre el sello de tiempo y la firma.

### 5. Evidencias de validación

La plataforma deberá conservar, asociadas al documento firmado, las evidencias necesarias para su validación posterior, incluyendo cuando corresponda:

a) Certificado del firmante;  
b) Cadena de certificación;  
c) Respuesta OCSP;  
d) CRL aplicable;  
e) Sello de tiempo;  
f) Hash del documento;  
g) Fecha y hora de firma;  
h) Resultado de validación;  
i) Bitácoras del proceso.

Para B-LT y B-LTA, los materiales exigidos por la matriz deberán incorporarse al documento conforme al estándar aplicable.

### 6. Representación visual

La representación visual de la firma podrá contener:

a) Nombre completo del firmante;  
b) Fecha y hora de firma asociada al sello de tiempo;  
c) Identificador o número de serie del certificado, cuando resulte necesario;  
d) Leyenda institucional de firma electrónica avanzada;  
e) Datos del cargo, dependencia o unidad administrativa cuando correspondan.

La representación visual será informativa. La validez de la firma dependerá de los elementos criptográficos contenidos en el documento y de su correcta validación.

### 7. Firmas múltiples

La plataforma deberá preservar la integridad de las firmas previamente incorporadas cuando se agreguen firmas adicionales.

Cada firma deberá contar con su propio certificado, sello de tiempo y evidencia de validación.

### 8. Conservación y mantenimiento de evidencias

La plataforma institucional, bajo responsabilidad operativa de la Autoridad de Certificación, conservará los documentos y sus evidencias asociadas hasta por diez años, sin sustituir las obligaciones archivísticas de la dependencia responsable del expediente.

La Autoridad de Certificación deberá evaluar la aptitud criptográfica y de validación de las evidencias de manera periódica y, en todo caso, antes del vencimiento de certificados o sellos de tiempo, o antes de que un algoritmo deje de ser aceptable. Cuando sea necesario, ejecutará el resellado, la incorporación de material de validación o la migración a B-LT o B-LTA.

Una vez concluido el plazo de conservación de la plataforma, la eliminación solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que exija conservar el documento o sus evidencias, y cuando se haya realizado la transferencia que corresponda a la dependencia responsable.

---

## Anexo L. Política de Sellado de Tiempo

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

### 1. Objeto y alcance

El presente documento establece las reglas generales bajo las cuales opera la Autoridad de Sellado de Tiempo vinculada a la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

La TSA emitirá sellos de tiempo para documentos, firmas electrónicas, hashes y evidencias electrónicas procesadas por los servicios institucionales autorizados.

### 2. Referencia temporal

La referencia de tiempo cierto será la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya.

Para mantener disponibilidad y continuidad, la TSA podrá utilizar servicios técnicos de sincronización de tiempo de alta disponibilidad, siempre que:

a) Mantengan trazabilidad respecto de la referencia temporal oficial y del Tiempo Universal Coordinado;  
b) Utilicen fuentes redundantes;  
c) Permitan monitorear desviaciones;  
d) Generen alertas ante pérdida de sincronización;  
e) Registren eventos y ajustes relevantes;  
f) Se sujeten a la tolerancia y al método de medición aprobados en la CPS.

No deberán realizarse afirmaciones de equivalencia o superioridad metrológica respecto del CENAM sin evidencia formal que las sustente.

### 3. Formato de los sellos de tiempo

Las solicitudes y respuestas deberán cumplir con RFC 3161 y con los perfiles técnicos autorizados.

Cada sello deberá vincular, al menos:

a) Hash del dato o documento sellado;  
b) Algoritmo de hash;  
c) Fecha y hora;  
d) Número de serie único;  
e) Identificador de política asignado bajo `1.3.6.1.4.1.63888`;  
f) Certificado de la TSA;  
g) Firma electrónica de la TSA.

### 4. Gestión criptográfica

La clave privada de la TSA deberá:

a) Ser independiente de la clave de la AC raíz;  
b) Ser independiente de las claves de OCSP y otros servicios;  
c) Permanecer bajo control de un servicio criptográfico autorizado;  
d) Estar protegida mediante controles de acceso, separación de funciones, monitoreo y registro de operaciones;  
e) Ser no exportable. Cuando una limitación técnica impida aplicar esta restricción, la excepción requerirá aprobación formal de la Coordinación de Política Digital, análisis de riesgo documentado y controles compensatorios equivalentes que protejan la confidencialidad, integridad y uso exclusivo de la clave.

El certificado de la TSA deberá cumplir íntegramente el perfil autoritativo establecido en el apartado 4.2 del Anexo A. Este documento no redefine ni duplica dicho perfil.

### 5. Algoritmos

| Elemento | Requisito |
|---|---|
| Función hash aceptada | SHA-256 o superior |
| Algoritmo de firma | Conforme al perfil técnico vigente del Anexo A |
| Formato | RFC 3161 |
| Identificador de política | OID aprobado y registrado bajo el PEN `1.3.6.1.4.1.63888` |

Los algoritmos autorizados deberán revisarse periódicamente.

### 6. Operación y disponibilidad

La TSA deberá contar con:

a) Monitoreo continuo de sincronización;  
b) Alertas por desviación;  
c) Controles de acceso administrativo;  
d) Registro de solicitudes y respuestas;  
e) Respaldo de configuraciones y bitácoras;  
f) Procedimientos de continuidad;  
g) Procedimientos de suspensión controlada cuando no pueda garantizarse la precisión temporal.

La TSA no deberá emitir sellos de tiempo cuando la desviación se encuentre fuera de la tolerancia establecida en la CPS, determinada mediante el método de medición definido en ese mismo documento.

### 7. Bitácoras y evidencias

Deberán conservarse, al menos:

a) Fecha y hora de cada operación;  
b) Número de serie del sello;  
c) Hash recibido;  
d) Algoritmo utilizado;  
e) Resultado de la operación;  
f) Eventos de sincronización;  
g) Desviaciones detectadas;  
h) Cambios de configuración;  
i) Accesos administrativos;  
j) Incidentes y periodos de indisponibilidad.

La Autoridad de Certificación será responsable de la custodia operativa de las bitácoras y evidencias de la TSA, las cuales se conservarán hasta por diez años. Su eliminación solo procederá cuando haya concluido dicho plazo y no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que exija conservarlas por más tiempo.

### 8. Incidentes

Cuando exista pérdida de sincronización, compromiso de la clave, emisión incorrecta o cualquier evento que afecte la confianza de los sellos emitidos, deberán activarse los procedimientos de incidentes y continuidad.

La Autoridad de Certificación determinará el alcance del incidente, los sellos afectados, las notificaciones necesarias y las medidas de recuperación.

### 9. Cese de la TSA

El cese deberá contemplar:

a) Aviso a usuarios y terceros confiantes;  
b) Tratamiento de sellos emitidos;  
c) Conservación de bitácoras y evidencias;  
d) Publicación de información de validación;  
e) Revocación o expiración controlada del certificado TSA;  
f) Destrucción segura de la clave una vez cumplidas las obligaciones posteriores.

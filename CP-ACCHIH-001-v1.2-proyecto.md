<div align="center">
  <img src="./img/logo1.png" alt="Gobierno del Estado" height="80" style="margin-right: 30px;" />
  <img src="./img/logo2.png" alt="Autoridad Certificadora" height="80" />
</div>
<br>

# Política de Certificación  
## Autoridad de Certificación de Gobierno del Estado de Chihuahua

**Clave del documento:** CP-ACCHIH-001  
**OID:** 1.3.6.1.4.1.63888.1.1  
**Versión:** 1.2  
**Estado:** Proyecto  
**Fecha de emisión:** Octubre 2024  
**Fecha de entrada en vigor:** Octubre 2024  
**Autoridad responsable:** Coordinación de Política Digital  
**Órgano de aprobación:** Coordinación de Política Digital y Consejo Técnico  
**Sitio de publicación:** autoridadcertificadora.chihuahua.gob.mx  
**Apartado de publicación:** Normatividad Operativa  

---

# Control documental

| Elemento | Descripción |
|---|---|
| Nombre del documento | Política de Certificación de la Autoridad de Certificación de Gobierno del Estado de Chihuahua |
| Clave | CP-ACCHIH-001 |
| OID | 1.3.6.1.4.1.63888.1.1 |
| Versión | 1.2 |
| Estado | Proyecto |
| Fecha de emisión | Octubre 2024 |
| Fecha de entrada en vigor | Octubre 2024 |
| Autoridad responsable | Coordinación de Política Digital |
| Autoridad emisora | Autoridad de Certificación de Gobierno del Estado de Chihuahua |
| Denominación institucional de difusión | Autoridad Certificadora |
| Aprobación | Coordinación de Política Digital y Consejo Técnico |
| Ubicación oficial de publicación | autoridadcertificadora.chihuahua.gob.mx, apartado de Normatividad Operativa |
| Documento relacionado | Declaración de Prácticas de Certificación de la Autoridad de Certificación de Gobierno del Estado de Chihuahua |
| Periodicidad de revisión | Cuando existan cambios normativos, técnicos, operativos o de seguridad que lo ameriten, o por determinación de la Coordinación de Política Digital o del Consejo Técnico |

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---:|---|---|
| 1.0 | Octubre 2024 | Emisión inicial del documento | Coordinación de Política Digital |
| 1.1 | [●] | Integración de información técnica y operativa derivada del despliegue inicial | Coordinación de Política Digital |
| 1.2 | [●] | Revisión de consistencia normativa, neutralidad tecnológica, conservación, sellado de tiempo y arquitectura PKI | Coordinación de Política Digital |

---

# 1. Introducción

## 1.1. Objeto de la Política de Certificación

La presente Política de Certificación tiene por objeto establecer el marco normativo, técnico y operativo general bajo el cual la Autoridad de Certificación de Gobierno del Estado de Chihuahua emite, administra, publica, valida y revoca certificados digitales destinados al uso de firma electrónica avanzada y servicios relacionados dentro de su ámbito de competencia.

Esta Política define las reglas generales de confianza aplicables a los certificados emitidos por la Autoridad de Certificación, incluyendo los sujetos que pueden solicitarlos, los usos permitidos y prohibidos, los procedimientos generales de identificación y autenticación, la vigencia de los certificados, los supuestos de revocación, las obligaciones de los participantes, los límites de responsabilidad, los mecanismos de validación de estado, la publicación de información, la conservación documental, la interoperabilidad, la portabilidad y los principios de seguridad aplicables.

La presente Política será aplicable a los certificados emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua, así como a los actos, documentos electrónicos, sistemas, servicios y procedimientos que expresamente se sujeten a ella.

## 1.2. Alcance

La Autoridad de Certificación de Gobierno del Estado de Chihuahua emitirá certificados digitales para:

a) Personas servidoras públicas del Poder Ejecutivo del Estado de Chihuahua;  
b) Personas físicas ciudadanas;  
c) Personas físicas que actúen como representantes legales de personas morales con domicilio establecido en el Estado de Chihuahua;  
d) Servicios de validación de estado de certificados mediante OCSP;  
e) Mecanismos complementarios de validación, incluyendo listas de revocación de certificados cuando resulten necesarias para fines de respaldo, interoperabilidad, continuidad operativa o validación histórica.

La emisión de certificados para sujetos distintos podrá realizarse mediante convenios de colaboración, convenios de portabilidad, instrumentos jurídicos equivalentes o disposiciones aplicables que permitan extender el uso, reconocimiento o aceptación de los certificados emitidos por la Autoridad de Certificación.

La Autoridad de Certificación podrá extender su ámbito de operación o reconocimiento, mediante los instrumentos correspondientes, hacia el Poder Legislativo del Estado, el Poder Judicial del Estado, municipios, organismos descentralizados, órganos desconcentrados, universidades, órganos autónomos, entidades públicas de otros estados y entidades u órganos federales.

## 1.3. Naturaleza de la Política de Certificación

La presente Política de Certificación constituye el documento rector de alto nivel que establece los principios, reglas y condiciones generales bajo los cuales opera la infraestructura de certificación digital de la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

La Política de Certificación define el marco de confianza de los certificados emitidos por la Autoridad de Certificación. No sustituye a la Declaración de Prácticas de Certificación, ni a los procedimientos técnicos, manuales operativos, lineamientos de seguridad, formatos, guías, convenios o instrumentos específicos que regulen la operación cotidiana de la Autoridad de Certificación.

## 1.4. Relación entre la Política de Certificación y la Declaración de Prácticas de Certificación

La Política de Certificación establece qué reglas deben cumplirse para la emisión, administración, uso, validación y revocación de certificados digitales.

La Declaración de Prácticas de Certificación describe cómo la Autoridad de Certificación implementa dichas reglas en su operación cotidiana, incluyendo procedimientos, controles, roles, mecanismos tecnológicos, bitácoras, evidencias, medidas de seguridad, continuidad operativa, respuesta a incidentes y demás prácticas administrativas y técnicas.

En caso de discrepancia entre la Política de Certificación y la Declaración de Prácticas de Certificación, prevalecerá la Política de Certificación, salvo que la Declaración de Prácticas de Certificación establezca controles técnicos u operativos más estrictos, siempre que no contradigan la presente Política ni la normatividad aplicable.

## 1.5. Marco normativo aplicable y de referencia

La presente Política se emite tomando en consideración, de manera enunciativa y no limitativa:

a) Constitución Política de los Estados Unidos Mexicanos;  
b) Constitución Política del Estado de Chihuahua;  
c) Ley de Gobierno Digital para el Estado de Chihuahua;  
d) Ley de Firma Electrónica Avanzada de orden federal;  
e) Disposiciones generales derivadas de la Ley de Firma Electrónica Avanzada de orden federal, cuando resulten aplicables como referencia normativa, técnica u operativa;  
f) Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados;  
g) Legislación estatal aplicable en materia de protección de datos personales;  
h) Ley General de Transparencia y Acceso a la Información Pública;  
i) Legislación estatal aplicable en materia de transparencia y acceso a la información pública;  
j) Ley General de Archivos;  
k) Legislación estatal aplicable en materia de archivos, gestión documental y conservación de expedientes;  
l) Legislación aplicable en materia de responsabilidades administrativas;  
m) NOM-151-SCFI-2016, Requisitos que deben observarse para la conservación de mensajes de datos y digitalización de documentos, o la que la sustituya;  
n) Normatividad aplicable en materia de seguridad de la información, tecnologías de la información, gobierno digital e interoperabilidad;  
o) Estándares X.509 para certificados digitales;  
p) RFC 5280, relativo a certificados de clave pública e infraestructura de clave pública X.509;  
q) RFC 6960, relativo al protocolo OCSP;  
r) RFC 3161, relativo a sellado de tiempo;  
s) RFC 3647, como referencia metodológica para la estructura de políticas y prácticas de certificación;  
t) Estándares ETSI aplicables a firmas electrónicas y documentos firmados, incluyendo PAdES;  
u) Estándares ISO/IEC aplicables en materia de seguridad de la información, continuidad y gestión de riesgos;  
v) Criterios técnicos que emita la Coordinación de Política Digital;  
w) Acuerdos, convenios de colaboración, convenios de portabilidad, lineamientos, manuales, formatos y demás instrumentos aprobados por la autoridad competente.

## 1.6. Principios rectores

La operación de la Autoridad de Certificación se regirá por los principios de legalidad, seguridad jurídica, autenticidad, integridad, confidencialidad, disponibilidad, trazabilidad, no repudio, protección de datos personales, conservación documental, interoperabilidad, neutralidad tecnológica razonable, continuidad operativa, responsabilidad, transparencia operativa, mínimo privilegio, separación de funciones, gestión de riesgos y mejora continua.

## 1.7. Definiciones y acrónimos

**AC:** Autoridad de Certificación de Gobierno del Estado de Chihuahua.  

**Autoridad Certificadora:** Denominación institucional de difusión utilizada para identificar públicamente a la Autoridad de Certificación de Gobierno del Estado de Chihuahua en portales, guías, formatos, herramientas, campañas y comunicaciones dirigidas a ciudadanía, dependencias y usuarios. Su uso no implica una entidad distinta.  

**AR:** Autoridad de Registro autorizada para realizar funciones de identificación, validación, registro o apoyo operativo en el ciclo de vida de los certificados.  

**Agente registrador:** Persona autorizada para intervenir en procesos de enrolamiento, validación de identidad, revisión documental o atención de solicitudes.  

**Certificado digital:** Documento electrónico emitido por la Autoridad de Certificación que vincula datos de verificación de firma con una persona titular o con un servicio autorizado.  

**CP:** Política de Certificación.  

**CPS:** Declaración de Prácticas de Certificación.  

**CRL:** Lista de revocación de certificados.  

**FEA:** Firma Electrónica Avanzada.  

**Firmante:** Persona física titular de un certificado de firma electrónica avanzada que utiliza su clave privada para firmar electrónicamente un documento o mensaje de datos.  

**OCSP:** Protocolo de consulta en línea utilizado para verificar el estado de vigencia o revocación de un certificado digital.  

**PAdES:** Formato de firma electrónica avanzada aplicable a documentos PDF.  

**Repositorio:** Sitio o sistema administrado por la Autoridad de Certificación para publicar certificados, información de estado, CP, CPS, avisos, formatos, guías y demás información pública relacionada con los servicios de certificación.  

**Solicitante:** Persona física que solicita la emisión de un certificado digital.  

**Tercero confiante:** Persona, dependencia, entidad, sistema o institución que confía en un certificado emitido por la Autoridad de Certificación y verifica su validez.  

**Titular:** Persona física a favor de quien se emite un certificado digital.  

**TSA:** Autoridad de Sellado de Tiempo encargada de emitir sellos de tiempo vinculados a documentos, firmas o evidencias electrónicas.

---

# 2. Identificación de la Autoridad de Certificación

## 2.1. Denominación oficial y denominación institucional de difusión

Para efectos jurídicos, normativos, técnicos y de emisión de certificados digitales, la entidad emisora se denominará:

**Autoridad de Certificación de Gobierno del Estado de Chihuahua.**

Dicha denominación será utilizada en los certificados digitales emitidos bajo la presente Política, en la Declaración de Prácticas de Certificación, en los perfiles técnicos de certificado, en las respuestas de validación de estado, en los registros oficiales y en los instrumentos normativos que regulen la infraestructura de certificación.

Sin perjuicio de lo anterior, para efectos de comunicación institucional, identidad pública, difusión, portal electrónico, materiales de orientación, guías de usuario, formatos, campañas, herramientas y demás elementos de interacción con la ciudadanía y las dependencias, podrá emplearse la denominación:

**Autoridad Certificadora.**

El uso de la denominación “Autoridad Certificadora” se entenderá referido a la Autoridad de Certificación de Gobierno del Estado de Chihuahua y no implicará la existencia de una entidad distinta.

## 2.2. Dependencia responsable

La Autoridad de Certificación dependerá formalmente de la Coordinación de Política Digital, responsable de su conducción institucional, normativa, técnica y operativa.

## 2.3. Órgano de aprobación

La presente Política será aprobada por la Coordinación de Política Digital y el Consejo Técnico.

## 2.4. Portal oficial y repositorio público

La Autoridad de Certificación publicará la información relacionada con sus servicios en:

**autoridadcertificadora.chihuahua.gob.mx**

La Política de Certificación y la Declaración de Prácticas de Certificación se publicarán en el apartado **Normatividad Operativa**.

---

# 3. Comunidad de confianza y ámbito de aplicación

## 3.1. Integrantes

La comunidad de confianza estará integrada por:

a) La Autoridad de Certificación;  
b) La Coordinación de Política Digital;  
c) El Consejo Técnico;  
d) Las autoridades de registro;  
e) Los agentes registradores;  
f) Las personas solicitantes;  
g) Las personas titulares y firmantes;  
h) Las personas servidoras públicas;  
i) Las personas físicas ciudadanas;  
j) Las personas físicas representantes legales de personas morales;  
k) Las dependencias y entidades usuarias;  
l) Los sujetos incorporados mediante convenio;  
m) Los terceros confiantes;  
n) Los administradores de sistemas autorizados;  
o) Los servicios tecnológicos autorizados.

## 3.2. Personas servidoras públicas

Las personas servidoras públicas podrán solicitar certificados para el ejercicio de sus funciones, previa autorización del superior jerárquico o de la unidad administrativa competente.

La separación del cargo, baja del servicio público, cambio de dependencia, cambio de unidad administrativa o cambio de cargo distinto dará lugar a la revocación definitiva del certificado.

## 3.3. Personas físicas ciudadanas

Las personas físicas ciudadanas podrán solicitar certificados de firma electrónica avanzada conforme a los requisitos de identidad, autenticación, generación de clave, aceptación, uso y revocación previstos en esta Política.

La emisión será gratuita.

## 3.4. Representantes legales de personas morales

Los certificados serán emitidos a favor de la persona física representante legal, incorporando o vinculando el atributo de representación correspondiente.

La terminación, modificación, limitación o pérdida de las facultades de representación dará lugar a la revocación del certificado.

## 3.5. Terceros confiantes

Los terceros confiantes deberán verificar la vigencia, estado de revocación, cadena de confianza, integridad documental, uso permitido y sello de tiempo cuando corresponda.

---

# 4. Tipos de certificados

## 4.1. Tipos autorizados

La Autoridad de Certificación podrá emitir:

a) Certificados de firma electrónica avanzada para personas servidoras públicas;  
b) Certificados de firma electrónica avanzada para personas físicas ciudadanas;  
c) Certificados de firma electrónica avanzada para representantes legales de personas morales;  
d) Certificados para servicios OCSP;  
e) Certificados para firma de CRL, cuando se utilicen;  
f) Certificados de infraestructura necesarios para la operación de la AC, TSA, repositorio, plataforma institucional y servicios relacionados.

## 4.2. Vigencias

a) Certificado de la AC raíz: hasta quince años;  
b) Certificados de usuario final: hasta cuatro años;  
c) Certificados OCSP, CRL, TSA e infraestructura: conforme al perfil técnico aplicable.

---

# 5. Usos permitidos y prohibidos

## 5.1. Principio general

El uso de la firma electrónica avanzada no será obligatorio de forma general. Sin embargo, cuando sea utilizada válidamente, producirá los efectos jurídicos correspondientes, incluyendo el no repudio conforme a la normatividad aplicable.

## 5.2. Usos permitidos

Los certificados podrán utilizarse para firmar documentos electrónicos internos o externos, incluyendo oficios, comunicaciones, autorizaciones, constancias, resoluciones, dictámenes, acuerdos, convenios, contratos, actas, informes, solicitudes, expedientes electrónicos y demás documentos de impacto jurídico o administrativo.

## 5.3. Formato de firma

Los documentos firmados mediante la plataforma institucional deberán utilizar formato PAdES e incorporar sello de tiempo.

## 5.4. Usos prohibidos

Queda prohibido:

a) Suplantar identidad;  
b) Firmar con información falsa o alterada;  
c) Compartir o transferir la clave privada;  
d) Utilizar certificados vencidos o revocados;  
e) Utilizar un certificado fuera de su alcance;  
f) Utilizar certificados de usuario final para firmar certificados, respuestas OCSP o CRL;  
g) Utilizar el certificado después de cambio de cargo, dependencia, unidad administrativa o pérdida de representación;  
h) Alterar certificados, firmas, sellos de tiempo, evidencias o bitácoras;  
i) Utilizar certificados en sistemas críticos no autorizados.

---

# 6. Identificación y autenticación

## 6.1. Modalidades de enrolamiento

La identificación podrá realizarse mediante:

a) Enrolamiento presencial ante agente registrador;  
b) Enrolamiento remoto mediante aplicación web progresiva;  
c) Enrolamiento mixto.

## 6.2. Verificación automatizada de identidad

La Autoridad de Certificación podrá apoyarse en servicios de verificación automatizada de identidad, ya sea mediante proveedor tecnológico autorizado, solución institucional propia o desarrollo interno autorizado, para realizar validación documental, validación biométrica, prueba de vida, análisis de autenticidad de documentos, comparación facial, detección de riesgo, prevención de suplantación de identidad y generación de evidencias técnicas.

Dicho servicio tendrá carácter auxiliar y no decidirá por sí mismo la emisión, rechazo o revocación del certificado.

## 6.3. Datos mínimos de identificación

Deberán validarse, cuando menos:

a) Nombre completo;  
b) CURP;  
c) RFC;  
d) Correo electrónico;  
e) Identificación oficial o mecanismo equivalente;  
f) Información adicional según el tipo de certificado.

Para personas servidoras públicas se validará además dependencia, unidad administrativa, situación activa y autorización jerárquica.

Para representantes legales se validará la existencia de la persona moral, domicilio en Chihuahua y vigencia de facultades.

## 6.4. Prueba de posesión de clave privada

La Autoridad de Certificación deberá verificar que la persona solicitante posee la clave privada correspondiente a la clave pública que será certificada.

## 6.5. Generación local de claves

El par de claves de usuario deberá generarse en el equipo de la persona titular. La clave privada no deberá transmitirse a la AC, AR, agentes registradores, servicios de verificación ni terceros.

---

# 7. Contenido de los certificados

## 7.1. Datos del emisor

Los certificados identificarán como emisor a:

**Autoridad de Certificación de Gobierno del Estado de Chihuahua.**

## 7.2. Datos del titular

Podrán incluir:

a) Nombre completo;  
b) CURP;  
c) RFC;  
d) Correo electrónico;  
e) Entidad federativa;  
f) País;  
g) Código postal;  
h) Localidad;  
i) Unidad administrativa;  
j) Dependencia u organismo;  
k) Atributo de representación legal.

## 7.3. Atributos X.509 autorizados

Podrán utilizarse:

a) S;  
b) C;  
c) PostalCode;  
d) L;  
e) OU;  
f) O;  
g) E;  
h) CN;  
i) SerialNumber;  
j) 2.5.4.45.

## 7.4. Datos no permitidos

No deberán incorporarse datos personales sensibles, domicilio particular completo, teléfono personal, datos biométricos directos, imágenes de identificación, documentos completos de identidad ni información innecesaria.

---

# 8. Ciclo de vida del certificado

## 8.1. Etapas

El ciclo de vida comprenderá:

a) Solicitud;  
b) Identificación;  
c) Autenticación;  
d) Validación;  
e) Autorización, cuando corresponda;  
f) Generación de claves;  
g) Prueba de posesión de clave privada;  
h) Emisión;  
i) Aceptación;  
j) Uso;  
k) Renovación;  
l) Revocación definitiva;  
m) Expiración;  
n) Archivo de evidencias.

## 8.2. Emisión inicial

Toda emisión deberá iniciar con una solicitud y estará condicionada al cumplimiento satisfactorio de los requisitos aplicables.

## 8.3. Renovación

La renovación consistirá en la emisión de un nuevo certificado antes del vencimiento del vigente, siempre que no exista causa de revocación ni cambio sustantivo de datos, calidad o autorización.

## 8.4. Ausencia de reemisión

La Autoridad de Certificación no realizará reemisión de certificados.

Cuando exista error, pérdida o compromiso de clave privada, cambio de información esencial, cambio de dependencia, cambio de unidad administrativa, cambio de cargo, baja del servicio público, modificación o pérdida de representación, o cualquier otra causa que afecte la confianza o vigencia del certificado, se revocará definitivamente el certificado anterior.

La persona interesada podrá tramitar una nueva emisión, sujeta al cumplimiento completo de los requisitos aplicables.

## 8.5. Expiración

El certificado expirará automáticamente al concluir su vigencia. Las firmas generadas antes del vencimiento podrán conservar sus efectos si puede acreditarse que fueron realizadas durante la vigencia y que el certificado no estaba revocado.

---

# 9. Revocación definitiva

## 9.1. Naturaleza

La revocación es anticipada, definitiva e irreversible. No existe suspensión temporal.

## 9.2. Causas generales

Serán causas de revocación:

a) Solicitud del titular;  
b) Pérdida o compromiso de clave privada;  
c) Uso no autorizado;  
d) Información falsa o incorrecta;  
e) Error material en el certificado;  
f) Incumplimiento de CP, CPS o términos de uso;  
g) Orden de autoridad competente;  
h) Riesgo de suplantación;  
i) Fallecimiento;  
j) Cualquier otra causa prevista en la CPS.

## 9.3. Servidores públicos

Además:

a) Separación del cargo;  
b) Baja;  
c) Cambio de dependencia;  
d) Cambio de unidad administrativa;  
e) Cambio de cargo distinto;  
f) Pérdida de autorización;  
g) Solicitud del superior jerárquico o unidad competente.

## 9.4. Representantes legales

Además:

a) Terminación de facultades;  
b) Revocación o modificación del poder;  
c) Limitación de facultades;  
d) Extinción o cambio jurídico relevante de la persona moral;  
e) Pérdida del domicilio establecido en Chihuahua, cuando sea requisito.

## 9.5. Efectos

La revocación surtirá efectos a partir de la fecha y hora registrada por la Autoridad de Certificación.

---

# 10. Validación del estado de certificados

## 10.1. OCSP

El servicio OCSP será el mecanismo principal de consulta de estado.

## 10.2. CRL complementaria

La AC podrá emitir CRL como mecanismo complementario para respaldo, interoperabilidad, continuidad operativa o validación histórica.

## 10.3. Obligación de los terceros confiantes

Antes de aceptar una firma, deberán verificar:

a) Vigencia;  
b) Estado de revocación;  
c) Cadena de confianza;  
d) Integridad documental;  
e) Sello de tiempo;  
f) Uso permitido.

---

# 11. Repositorio público

El portal oficial podrá publicar:

a) CP vigente e históricas;  
b) CPS vigente e históricas;  
c) Certificados emitidos;  
d) Información de estado;  
e) OCSP;  
f) CRL;  
g) Certificados de infraestructura pública;  
h) Avisos de incidentes;  
i) Formatos;  
j) Guías;  
k) Herramientas;  
l) Términos y condiciones;  
m) Avisos de privacidad;  
n) Datos de contacto.

---

# 12. Plataforma institucional de firmado

## 12.1. Sujetos autorizados

La plataforma estará disponible para personas servidoras públicas, dependencias y sujetos incorporados mediante convenio.

La emisión de un certificado ciudadano no otorgará acceso automático a la plataforma.

## 12.2. PAdES y sellado de tiempo

Todo documento firmado mediante la plataforma institucional deberá utilizar PAdES e incorporar sello de tiempo.

## 12.3. Conservación

La plataforma institucional conservará copia íntegra de los documentos firmados hasta por diez años, conforme a los controles de seguridad, disponibilidad, integridad, acceso y conservación aplicables.

La conservación realizada por la plataforma no sustituirá las obligaciones archivísticas de la dependencia dueña del documento.

---

# 13. Autoridad de Sellado de Tiempo

## 13.1. Referencia temporal

La TSA utilizará como referencia de tiempo cierto la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya. Para su operación técnica podrán utilizarse servicios de sincronización de alta disponibilidad, siempre que permitan mantener trazabilidad respecto de dicha referencia temporal y del Tiempo Universal Coordinado.

## 13.2. Uso obligatorio

Todo documento firmado mediante la plataforma institucional deberá incorporar sello de tiempo.

---

# 14. Conservación documental y expediente electrónico

## 14.1. NOM-151-SCFI-2016

La conservación de documentos electrónicos, mensajes de datos, evidencias técnicas, acuses, constancias, sellos de tiempo, hashes, bitácoras y demás elementos asociados al proceso de firma electrónica avanzada deberá observar, cuando resulte aplicable, la NOM-151-SCFI-2016 o la norma que la sustituya.

## 14.2. Plazo

La plataforma institucional conservará copia íntegra de los documentos firmados hasta por diez años. Este plazo constituye el periodo máximo ordinario de conservación prestado por la plataforma y no sustituye las obligaciones archivísticas de la dependencia responsable. La eliminación al concluir el plazo solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que requiera conservar el documento o sus evidencias por más tiempo, y cuando se haya efectuado la transferencia documental que corresponda.

## 14.3. Responsabilidad de la dependencia

La dependencia dueña del documento deberá prever su conservación conforme a sus temporalidades documentales, cuadro general de clasificación archivística, catálogo de disposición documental y demás disposiciones aplicables.

---

# 15. Interoperabilidad, portabilidad y reconocimiento

## 15.1. Principio general

La AC promoverá la interoperabilidad técnica, jurídica y operativa de sus certificados.

## 15.2. Reconocimiento del SAT

La AC podrá reconocer certificados emitidos por el Servicio de Administración Tributaria en los trámites y sistemas en que resulte jurídicamente procedente y técnicamente compatible.

## 15.3. Convenios

Podrán celebrarse convenios de colaboración o portabilidad con poderes, municipios, organismos descentralizados, órganos desconcentrados, universidades, órganos autónomos, otras entidades federativas y órganos federales.

## 15.4. Límites

El reconocimiento no será ilimitado y podrá restringirse por tipo de certificado, trámite, sistema, vigencia, nivel de confianza, alcance territorial o institucional, perfil técnico y condiciones del convenio.

---

# 16. Obligaciones

## 16.1. Autoridad de Certificación

Deberá operar conforme a CP, CPS y normatividad aplicable; proteger sus claves; administrar el ciclo de vida; publicar información de validación; revocar certificados; conservar evidencias; proteger datos personales; mantener bitácoras; atender incidentes y auditorías; y mantener continuidad operativa.

## 16.2. Titulares

Deberán custodiar su clave privada, verificar sus datos, utilizar el certificado dentro de su alcance, solicitar revocación ante pérdida o compromiso y no utilizar certificados vencidos o revocados.

## 16.3. Dependencias usuarias

Deberán gestionar autorizaciones, informar bajas y cambios, solicitar revocaciones, conservar expedientes y proteger la información contenida en los documentos.

## 16.4. Terceros confiantes

Deberán verificar la validez técnica y jurídica antes de aceptar una firma.

---

# 17. Responsabilidades y límites de responsabilidad

## 17.1. Autoridad de Certificación

La AC responderá por las funciones bajo su control: emisión, administración, publicación, validación, revocación y conservación de evidencias.

## 17.2. Exclusiones

La AC no será responsable por:

a) Uso indebido del certificado;  
b) Custodia negligente de clave privada;  
c) Uso fuera de vigencia o después de revocación;  
d) Información falsa del solicitante;  
e) Falta de validación por terceros;  
f) Fallas de sistemas externos;  
g) Fuerza mayor;  
h) Contenido de documentos firmados;  
i) Actos fuera de competencia o representación.

---

# 18. Seguridad de la información

La AC implementará controles administrativos, técnicos, físicos y organizacionales para proteger confidencialidad, integridad, disponibilidad, autenticidad, trazabilidad y resiliencia.

Los controles deberán abarcar infraestructura PKI, claves criptográficas, OCSP, CRL, TSA, plataforma institucional, repositorio, enrolamiento, servicios de verificación, bases de datos, bitácoras, documentos conservados, redes y proveedores.

---

# 19. Gestión de claves criptográficas

## 19.1. Clave de la AC

La clave privada de la AC será administrada mediante un servicio criptográfico autorizado, bajo controles de acceso, mínimo privilegio, autenticación multifactor, registro de operaciones, segregación de funciones y restricciones de exportación cuando resulten aplicables. La clave de la AC raíz no deberá utilizarse para sellado de tiempo, cifrado de datos, firma de documentos de usuario final, autenticación de cliente o servidor ni firma de código. Los servicios OCSP y TSA deberán utilizar claves y certificados independientes.

## 19.2. Arquitectura técnica

La arquitectura vigente de la Autoridad de Certificación opera sobre infraestructura de nube de alta disponibilidad, con servicios desacoplados, componentes redundantes, almacenamiento administrado y mecanismos de escalamiento y recuperación.

Las operaciones criptográficas de la Autoridad de Certificación se realizan mediante un servicio administrado de gestión de claves autorizado, sujeto a controles de acceso, separación de funciones, registro de operaciones, monitoreo y restricciones de exportación cuando resulten aplicables.

La operación vigente mediante una Autoridad de Certificación raíz emisora en línea se reconoce como arquitectura transitoria y continuará siendo reconocida hasta su sustitución, expiración o revocación, bajo controles compensatorios de acceso, monitoreo, trazabilidad, separación de funciones, continuidad y respuesta a incidentes.

La arquitectura objetivo será una cadena compuesta por una Autoridad de Certificación raíz fuera de línea, una sola capa de autoridades intermedias subordinadas emisoras y certificados de entidad final. La raíz objetivo deberá utilizar `pathLenConstraint=1` y cada autoridad intermedia emisora deberá utilizar `pathLenConstraint=0`; las autoridades intermedias no podrán emitir otras autoridades subordinadas.

La transición requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, perfiles técnicos aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de la Política y la Declaración de Prácticas de Certificación.

## 19.3. Claves de usuario

Las claves privadas de usuario final se generarán en el equipo del titular y no serán recibidas, custodiadas, respaldadas ni recuperadas por la AC.

---

# 20. Bitácoras, trazabilidad y auditoría

La AC registrará solicitudes, validaciones, autorizaciones, emisiones, renovaciones, revocaciones, consultas OCSP, CRL, firmas, sellos de tiempo, accesos administrativos, cambios de configuración, fallas, respaldos, restauraciones, publicaciones e incidentes.

Las bitácoras deberán protegerse contra alteración, eliminación o acceso no autorizado.

La AC se sujetará a auditorías internas y a las que ordene la Secretaría de la Función Pública u otra autoridad competente.

---

# 21. Gestión de incidentes

La AC deberá contar con un proceso que contemple detección, registro, clasificación, análisis, contención, erradicación, recuperación, notificación, documentación y lecciones aprendidas.

Los incidentes críticos podrán requerir suspensión de emisión, revocación de certificados, generación de nuevas claves, reconstrucción de cadenas de confianza y publicación de avisos.

---

# 22. Continuidad operativa y recuperación ante desastre

La infraestructura de la Autoridad de Certificación deberá operar con medidas de alta disponibilidad, redundancia, respaldo, monitoreo, escalamiento y recuperación acordes con la criticidad de los servicios de emisión, revocación, OCSP, TSA, repositorio y conservación de evidencias.

La Autoridad de Certificación deberá mantener planes de continuidad operativa y recuperación ante desastre que contemplen, al menos:

a) Redundancia de componentes críticos;  
b) Replicación y recuperación de bases de datos;  
c) Respaldos protegidos de configuraciones, bitácoras, evidencias y documentos;  
d) Recuperación de servicios criptográficos;  
e) Procedimientos alternos de validación y revocación;  
f) Responsables, prioridades y mecanismos de comunicación;  
g) Pruebas y simulacros periódicos.

Los detalles de implementación, proveedores y servicios tecnológicos utilizados deberán documentarse en la Declaración de Prácticas de Certificación y en los procedimientos internos correspondientes.

---

# 23. Cese de operaciones

El cese deberá realizarse conforme a un plan aprobado por la Coordinación de Política Digital y el Consejo Técnico.

El plan deberá contemplar avisos, estado de certificados, transferencia de servicios, conservación de registros y evidencias, operación posterior de OCSP o CRL, custodia de claves y protección de datos personales.

---

# 24. Tarifas y gratuidad

## 24.1. Ciudadanía

La emisión de certificados para personas físicas ciudadanas será gratuita.

## 24.2. Personas servidoras públicas

La emisión será gratuita, condicionada a la autorización del superior jerárquico o unidad administrativa competente.

## 24.3. Plataforma institucional

El acceso a la plataforma institucional estará reservado a personas servidoras públicas, dependencias y sujetos incorporados mediante convenio.

---

# 25. Aprobación, modificación, publicación y vigencia

La presente Política deberá ser aprobada por la Coordinación de Política Digital y el Consejo Técnico.

Las modificaciones sustantivas deberán someterse a la misma aprobación.

La versión vigente se publicará en:

**autoridadcertificadora.chihuahua.gob.mx**

dentro del apartado **Normatividad Operativa**.

La Política entrará en vigor en la fecha indicada en el control documental, una vez aprobada y publicada.

---

# Anexos

*Nota aclaratoria: Los siguientes anexos se emitirán, aprobarán y publicarán como documentos normativos, técnicos u operativos independientes, y formarán parte integral del marco de confianza de la Autoridad de Certificación.*

## Anexo A. Perfil técnico de certificados  
## Anexo B. Matriz de roles y responsabilidades  
## Anexo C. Matriz de causas de revocación  
## Anexo D. Procedimiento de enrolamiento presencial  
## Anexo E. Procedimiento de enrolamiento remoto  
## Anexo F. Procedimiento de emisión  
## Anexo G. Procedimiento de revocación  
## Anexo H. Procedimiento de incidentes  
## Anexo I. Procedimiento de continuidad operativa  
## Anexo J. Procedimiento de cese de operaciones  
## Anexo K. Perfil PAdES institucional  
## Anexo L. Política de sellado de tiempo  
## Anexo M. Formato de autorización de superior jerárquico  
## Anexo N. Formato de solicitud de certificado  
## Anexo O. Formato de revocación  
## Anexo P. Términos y condiciones de uso  
## Anexo Q. Aviso de privacidad

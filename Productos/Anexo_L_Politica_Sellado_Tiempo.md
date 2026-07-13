# Anexo L. Política de Sellado de Tiempo

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.1  
**Estado:** Proyecto revisado  

## 1. Objeto y alcance

El presente documento establece las reglas generales bajo las cuales opera la Autoridad de Sellado de Tiempo vinculada a la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

La TSA emitirá sellos de tiempo para documentos, firmas electrónicas, hashes y evidencias electrónicas procesadas por los servicios institucionales autorizados.

## 2. Referencia temporal

La referencia de tiempo cierto será la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya.

Para mantener disponibilidad y continuidad, la TSA podrá utilizar servicios técnicos de sincronización de tiempo de alta disponibilidad, siempre que:

a) Mantengan trazabilidad respecto de la referencia temporal oficial y del Tiempo Universal Coordinado;  
b) Utilicen fuentes redundantes;  
c) Permitan monitorear desviaciones;  
d) Generen alertas ante pérdida de sincronización;  
e) Registren eventos y ajustes relevantes;  
f) Se sujeten a tolerancias documentadas en la CPS.

No deberán realizarse afirmaciones de equivalencia o superioridad metrológica respecto del CENAM sin evidencia formal que las sustente.

## 3. Formato de los sellos de tiempo

Las solicitudes y respuestas deberán cumplir con RFC 3161 y con los perfiles técnicos autorizados.

Cada sello deberá vincular, al menos:

a) Hash del dato o documento sellado;  
b) Algoritmo de hash;  
c) Fecha y hora;  
d) Número de serie único;  
e) Identificador de política;  
f) Certificado de la TSA;  
g) Firma electrónica de la TSA.

## 4. Gestión criptográfica

La clave privada de la TSA deberá:

a) Ser independiente de la clave de la AC raíz;  
b) Ser independiente de las claves de OCSP y otros servicios;  
c) Permanecer bajo control de un servicio criptográfico autorizado;  
d) Estar protegida mediante controles de acceso, separación de funciones, monitoreo y registro de operaciones;  
e) No ser exportable cuando la tecnología utilizada permita imponer dicha restricción.

El certificado de la TSA deberá estar limitado exclusivamente al uso de sellado de tiempo mediante la extensión `timeStamping`.

## 5. Algoritmos

| Elemento | Requisito |
|---|---|
| Función hash aceptada | SHA-256 o superior |
| Algoritmo de firma | RSA con clave de al menos 2048 bits, o algoritmo autorizado equivalente |
| Formato | RFC 3161 |
| Identificador de política | OID aprobado para la política de sellado de tiempo |

La longitud exacta de las claves y los algoritmos autorizados deberán definirse en el perfil técnico vigente y revisarse periódicamente.

## 6. Operación y disponibilidad

La TSA deberá contar con:

a) Monitoreo continuo de sincronización;  
b) Alertas por desviación;  
c) Controles de acceso administrativo;  
d) Registro de solicitudes y respuestas;  
e) Respaldo de configuraciones y bitácoras;  
f) Procedimientos de continuidad;  
g) Procedimientos de suspensión controlada cuando no pueda garantizarse la precisión temporal.

La TSA no deberá emitir sellos de tiempo cuando la desviación se encuentre fuera de la tolerancia autorizada.

## 7. Bitácoras y evidencias

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

La conservación se realizará durante los plazos legales, archivísticos, probatorios y operativos aplicables.

## 8. Incidentes

Cuando exista pérdida de sincronización, compromiso de la clave, emisión incorrecta o cualquier evento que afecte la confianza de los sellos emitidos, deberán activarse los procedimientos de incidentes y continuidad.

La Autoridad de Certificación determinará el alcance del incidente, los sellos afectados, las notificaciones necesarias y las medidas de recuperación.

## 9. Cese de la TSA

El cese deberá contemplar:

a) Aviso a usuarios y terceros confiantes;  
b) Tratamiento de sellos emitidos;  
c) Conservación de bitácoras y evidencias;  
d) Publicación de información de validación;  
e) Revocación o expiración controlada del certificado TSA;  
f) Destrucción segura de la clave una vez cumplidas las obligaciones posteriores.

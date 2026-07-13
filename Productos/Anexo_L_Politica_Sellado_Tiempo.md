# Anexo L. Política de Sellado de Tiempo

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

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
f) Se sujeten a la tolerancia y al método de medición aprobados en la CPS.

No deberán realizarse afirmaciones de equivalencia o superioridad metrológica respecto del CENAM sin evidencia formal que las sustente.

## 3. Formato de los sellos de tiempo

Las solicitudes y respuestas deberán cumplir con RFC 3161 y con los perfiles técnicos autorizados.

Cada sello deberá vincular, al menos:

a) Hash del dato o documento sellado;  
b) Algoritmo de hash;  
c) Fecha y hora;  
d) Número de serie único;  
e) Identificador de política asignado bajo `1.3.6.1.4.1.63888`;  
f) Certificado de la TSA;  
g) Firma electrónica de la TSA.

## 4. Gestión criptográfica

La clave privada de la TSA deberá:

a) Ser independiente de la clave de la AC raíz;  
b) Ser independiente de las claves de OCSP y otros servicios;  
c) Permanecer bajo control de un servicio criptográfico autorizado;  
d) Estar protegida mediante controles de acceso, separación de funciones, monitoreo y registro de operaciones;  
e) Ser no exportable. Cuando una limitación técnica impida aplicar esta restricción, la excepción requerirá aprobación formal de la Coordinación de Política Digital, análisis de riesgo documentado y controles compensatorios equivalentes que protejan la confidencialidad, integridad y uso exclusivo de la clave.

El certificado de la TSA deberá cumplir íntegramente el perfil autoritativo establecido en el apartado 4.2 del Anexo A. Este documento no redefine ni duplica dicho perfil.

## 5. Algoritmos

| Elemento | Requisito |
|---|---|
| Función hash aceptada | SHA-256 o superior |
| Algoritmo de firma | Conforme al perfil técnico vigente del Anexo A |
| Formato | RFC 3161 |
| Identificador de política | OID aprobado y registrado bajo el PEN `1.3.6.1.4.1.63888` |

Los algoritmos autorizados deberán revisarse periódicamente.

## 6. Operación y disponibilidad

La TSA deberá contar con:

a) Monitoreo continuo de sincronización;  
b) Alertas por desviación;  
c) Controles de acceso administrativo;  
d) Registro de solicitudes y respuestas;  
e) Respaldo de configuraciones y bitácoras;  
f) Procedimientos de continuidad;  
g) Procedimientos de suspensión controlada cuando no pueda garantizarse la precisión temporal.

La TSA no deberá emitir sellos de tiempo cuando la desviación se encuentre fuera de la tolerancia establecida en la CPS, determinada mediante el método de medición definido en ese mismo documento.

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

La Autoridad de Certificación será responsable de la custodia operativa de las bitácoras y evidencias de la TSA, las cuales se conservarán hasta por diez años. Su eliminación solo procederá cuando haya concluido dicho plazo y no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que exija conservarlas por más tiempo.

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

# Anexo K. Perfil PAdES Institucional

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto revisado  
**IANA PEN:** `1.3.6.1.4.1.63888`  

## 1. Objeto

El presente anexo define el perfil mínimo para las firmas electrónicas avanzadas aplicadas a documentos PDF mediante la plataforma institucional.

## 2. Estándar base

La plataforma institucional utilizará firmas PAdES conforme a la familia de estándares ETSI EN 319 142.

El nivel mínimo será **PAdES Baseline B-T**, que incorpora un sello de tiempo sobre la firma y permite acreditar una referencia temporal confiable asociada al acto de firma.

PAdES-B-T no deberá considerarse, por sí solo, un mecanismo completo de validación a largo plazo. Cuando el periodo de conservación, el valor probatorio o el riesgo del documento lo requieran, deberán incorporarse los elementos necesarios para conformidad **PAdES Baseline B-LT** o **PAdES Baseline B-LTA**.

### 2.1. Matriz de conformidad

| Nivel | Firma Baseline B | Sello de tiempo RFC 3161 sobre la firma | Certificados y cadena incorporados | Evidencias de revocación incorporadas | Sellos de archivo posteriores | Regla de conformidad |
|---|---:|---:|---:|---:|---:|---|
| PAdES B-T | Obligatorio | Obligatorio | Opcional dentro del PDF; deberán conservarse como evidencia asociada | Opcional dentro del PDF; deberán conservarse como evidencia asociada | No requerido | No podrá declararse B-T sin sello de tiempo válido sobre la firma. |
| PAdES B-LT | Obligatorio | Obligatorio | Obligatorio | Obligatorio | No requerido | El PDF deberá contener el material necesario para validar la firma y el estado de los certificados sin depender de la disponibilidad inmediata de servicios externos. |
| PAdES B-LTA | Obligatorio | Obligatorio | Obligatorio | Obligatorio | Obligatorio | Además de cumplir B-LT, el PDF deberá incorporar uno o más sellos de archivo que protejan la firma y su material de validación para conservación prolongada. |

La presencia de una representación visual, hoja de firmas, código QR o folio no determina el nivel de conformidad PAdES.

## 3. Algoritmos

| Elemento | Requisito mínimo |
|---|---|
| Función hash | SHA-256 o superior |
| Algoritmo de firma | RSA con clave de al menos 2048 bits, o algoritmo autorizado equivalente |
| Sello de tiempo | RFC 3161 |
| Certificado de firmante | Certificado vigente y no revocado al momento de la firma |
| Certificado TSA | Conforme al perfil autoritativo definido en el apartado 4.2 del Anexo A |

Los algoritmos deberán revisarse conforme al estado de la técnica y a la política criptográfica institucional.

## 4. Validación al momento de firma

La plataforma deberá verificar, al menos:

a) Integridad del documento;  
b) Correspondencia entre la firma y el certificado;  
c) Vigencia del certificado;  
d) Estado de revocación mediante OCSP y, cuando proceda, CRL;  
e) Cadena de confianza;  
f) Uso permitido del certificado;  
g) Validez del sello de tiempo;  
h) Correspondencia entre el sello de tiempo y la firma.

## 5. Evidencias de validación

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

## 6. Representación visual

La representación visual de la firma podrá contener:

a) Nombre completo del firmante;  
b) Fecha y hora de firma asociada al sello de tiempo;  
c) Identificador o número de serie del certificado, cuando resulte necesario;  
d) Leyenda institucional de firma electrónica avanzada;  
e) Datos del cargo, dependencia o unidad administrativa cuando correspondan.

La representación visual será informativa. La validez de la firma dependerá de los elementos criptográficos contenidos en el documento y de su correcta validación.

## 7. Firmas múltiples

La plataforma deberá preservar la integridad de las firmas previamente incorporadas cuando se agreguen firmas adicionales.

Cada firma deberá contar con su propio certificado, sello de tiempo y evidencia de validación.

## 8. Conservación y mantenimiento de evidencias

La plataforma institucional, bajo responsabilidad operativa de la Autoridad de Certificación, conservará los documentos y sus evidencias asociadas hasta por diez años, sin sustituir las obligaciones archivísticas de la dependencia responsable del expediente.

La Autoridad de Certificación deberá evaluar la aptitud criptográfica y de validación de las evidencias de manera periódica y, en todo caso, antes del vencimiento de certificados o sellos de tiempo, o antes de que un algoritmo deje de ser aceptable. Cuando sea necesario, ejecutará el resellado, la incorporación de material de validación o la migración a B-LT o B-LTA.

Una vez concluido el plazo de conservación de la plataforma, la eliminación solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que exija conservar el documento o sus evidencias, y cuando se haya realizado la transferencia que corresponda a la dependencia responsable.

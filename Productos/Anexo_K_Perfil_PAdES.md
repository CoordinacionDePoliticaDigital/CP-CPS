# Anexo K. Perfil PAdES Institucional

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.1  
**Estado:** Proyecto revisado  

## 1. Objeto

El presente anexo define el perfil mínimo para las firmas electrónicas avanzadas aplicadas a documentos PDF mediante la plataforma institucional.

## 2. Estándar base

La plataforma institucional utilizará firmas PAdES conforme a la familia de estándares ETSI EN 319 142.

El nivel mínimo será **PAdES Baseline B-T**, que incorpora un sello de tiempo sobre la firma y permite acreditar una referencia temporal confiable asociada al acto de firma.

PAdES-B-T no deberá considerarse, por sí solo, un mecanismo completo de validación a largo plazo. Cuando el periodo de conservación, el valor probatorio o el riesgo del documento lo requieran, deberán incorporarse o conservarse los elementos necesarios para evolucionar o validar conforme a niveles **PAdES Baseline B-LT** o **PAdES Baseline B-LTA**.

## 3. Algoritmos

| Elemento | Requisito mínimo |
|---|---|
| Función hash | SHA-256 o superior |
| Algoritmo de firma | RSA con clave de al menos 2048 bits, o algoritmo autorizado equivalente |
| Sello de tiempo | RFC 3161 |
| Certificado de firmante | Certificado vigente y no revocado al momento de la firma |
| Certificado TSA | Certificado autorizado exclusivamente para sellado de tiempo |

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

Cuando se implemente PAdES-B-LT o B-LTA, los materiales de validación deberán incorporarse al documento conforme al estándar aplicable.

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

## 8. Conservación

Los documentos y evidencias deberán conservarse conforme a la Política de Certificación, la CPS, la NOM-151-SCFI-2016 cuando resulte aplicable y las disposiciones archivísticas correspondientes.

Para documentos sujetos a conservación prolongada deberán definirse procedimientos de actualización de evidencias, resellado o migración a perfiles B-LT o B-LTA antes de que los algoritmos, certificados o sellos de tiempo pierdan aptitud de validación.

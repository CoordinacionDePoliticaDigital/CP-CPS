# Acuse de revocación del Certificado de Firma Electrónica Avanzada

**Documento relacionado:** CP-ACCHIH-001 y CPS-ACCHIH-001
**Versión:** 1.0
**Estado:** Vigente
**Fecha de entrada en vigor:** 14 de agosto de 2026

**Modalidad:** Revocación directa por la persona titular  
**Sistema:** CERTAC  
**Fecha y hora de ejecución:** {{FECHA_HORA}}  
**Folio:** {{FOLIO}}  
**Código de verificación:** {{CODIGO_VERIFICACION}}

La **Autoridad de Certificación de Gobierno del Estado de Chihuahua**, identificada institucionalmente como **Autoridad Certificadora**, hace constar que la solicitud firmada por la persona titular fue validada y que la revocación del certificado señalado fue ejecutada satisfactoriamente.

## Datos de la persona titular

- Nombre completo: {{NOMBRE_COMPLETO}}
- CURP: {{CURP}}
- RFC: {{RFC}}

## Datos de la revocación

- Número de serie revocado: {{NUMERO_SERIE}}
- Clave de causal: {{CLAVE_CAUSAL}}
- Denominación normalizada de la causal: {{DENOMINACION_CAUSAL}}
- Descripción de los hechos: {{DESCRIPCION_HECHOS}}
- Fecha y hora efectiva de revocación: {{FECHA_HORA_REVOCACION}}
- Persona o proceso autorizado que ejecutó: {{EJECUTOR}}
- Estado de publicación: {{ESTADO_PUBLICACION}}
- Referencia del evento de publicación u outbox, o del registro durable alterno autorizado cuando corresponda: {{REFERENCIA_EVENTO_PUBLICACION}} (No aplica si la publicación ya fue confirmada)
- Fecha y hora de confirmación de publicación, cuando corresponda: {{FECHA_HORA_PUBLICACION}}

La descripción de los hechos se obtiene de la solicitud directa CERTAC 05 mediante la correspondencia `{{DESCRIPCION_HECHOS}}`; la denominación normalizada se obtiene de `{{DENOMINACION_CAUSAL}}` conforme al catálogo vigente.

- Persona o proceso autorizado que ejecutó: {{EJECUTOR}}

La revocación es definitiva e irreversible. El certificado queda invalidado para efectos de validación y no deberá ser aceptado para crear o verificar firmas posteriores a la fecha y hora efectiva indicada. Cuando el estado de publicación sea **pendiente**, este acuse acredita que la revocación local quedó confirmada durablemente y conserva la referencia de los eventos de publicación; deberá actualizarse o complementarse cuando OCSP y, en su caso, CRL reflejen el estado revocado. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado.

**Firma o sello electrónico de la Autoridad Certificadora:** {{FIRMA_ACUSE}}

**Referencia o identificador de la firma o sello:** {{REFERENCIA_FIRMA_O_SELLO}}

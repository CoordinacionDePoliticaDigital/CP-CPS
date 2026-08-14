# Acuse de revocación del Certificado de Firma Electrónica Avanzada

**Documento relacionado:** CP-ACCHIH-001 y CPS-ACCHIH-001
**Versión:** 1.0
**Estado:** Vigente
**Fecha de entrada en vigor:** 14 de agosto de 2026

**Modalidad:** Revocación ejecutada por agente autorizado  
**Sistema:** CERTAC  
**Fecha y hora de ejecución:** {{FECHA_HORA}}  
**Folio:** {{FOLIO}}  
**Código de verificación:** {{CODIGO_VERIFICACION}}

La **Autoridad de Certificación de Gobierno del Estado de Chihuahua**, identificada institucionalmente como **Autoridad Certificadora**, hace constar que el agente autorizado verificó la identidad o legitimidad de la solicitud, revisó la causal y ejecutó satisfactoriamente la revocación del certificado señalado.

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
- Sujeto que inició la revocación: {{INICIADOR}}
- Autorización o representación invocada, cuando corresponda: {{AUTORIZACION_REPRESENTACION}}
- Agente ejecutor: {{NOMBRE_AGENTE}}
- Estado de publicación: {{ESTADO_PUBLICACION}}
- Referencia del evento de publicación u outbox, o del registro durable alterno autorizado cuando corresponda: {{REFERENCIA_EVENTO_PUBLICACION}} (No aplica si la publicación ya fue confirmada)
- Fecha y hora de confirmación de publicación, cuando corresponda: {{FECHA_HORA_PUBLICACION}}

La revocación es definitiva e irreversible. El certificado queda invalidado para efectos de validación y no deberá ser aceptado para crear o verificar firmas posteriores a la fecha y hora efectiva indicada. Cuando el estado de publicación sea **pendiente**, este acuse acredita que la revocación local quedó confirmada durablemente y conserva la referencia de los eventos de publicación; deberá actualizarse o complementarse cuando OCSP y, en su caso, CRL reflejen el estado revocado. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado.

**Firma electrónica avanzada del agente autorizado:** {{FIRMA_AGENTE}}

**Referencia o identificador de la firma del agente:** {{REFERENCIA_FIRMA_AGENTE}}

**Sello electrónico de la Autoridad Certificadora:** {{SELLO_ACUSE}}

**Referencia o identificador del sello:** {{REFERENCIA_SELLO_ACUSE}}

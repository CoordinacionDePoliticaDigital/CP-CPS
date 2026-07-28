# Anexos D al G: Procedimientos Operativos (Alto Nivel)

## Anexo D. Procedimiento de Enrolamiento Presencial
1. **Solicitud:** El solicitante agenda una cita o acude a una agencia registradora.
2. **Presentación:** El solicitante presenta documentación original (INE/Pasaporte, comprobante de domicilio, CURP, RFC).
3. **Cotejo Biométrico y Documental:** El Agente Registrador captura biométricos (huellas, fotografía, firma autógrafa) y verifica la coincidencia física e identidad contra bases de datos (ej. RENAPO).
4. **Validación:** El Agente Registrador aprueba el expediente en el sistema.

## Anexo E. Procedimiento de Enrolamiento Remoto
1. **Solicitud Web:** El usuario accede a la plataforma de enrolamiento remoto.
2. **Captura de Datos:** Sube anverso y reverso de su identificación oficial, e ingresa su CURP y RFC.
3. **Prueba de Vida (Liveness):** El sistema realiza captura de video o biometría facial interactiva para asegurar que la persona está presente.
4. **Validación Automatizada:** El motor biométrico compara la prueba de vida contra la fotografía de la identificación.
5. **Aprobación:** Si el score de confianza es alto, se autoriza; si es dudoso, pasa a revisión manual por un Agente Registrador.

## Anexo F. Procedimiento de Emisión
1. **Autorización:** Una vez que el enrolamiento (presencial o remoto) es aprobado, el sistema habilita la etapa de emisión.
2. **Generación de Claves:** En el equipo o dispositivo del usuario final (navegador o app local) se genera el par de claves criptográficas. La clave privada se cifra con una contraseña definida por el usuario.
3. **Firma del CSR:** El navegador envía el Certifcate Signing Request (CSR) firmado con la clave privada generada hacia la Autoridad de Certificación.
4. **Emisión de AC:** La CA Raíz en línea valida el CSR y la autorización previa, y firma el certificado público (`.cer`).
5. **Descarga:** El usuario descarga su certificado público y guarda su llave privada (`.key`) localmente.

## Anexo G. Procedimiento de Revocación

Esta sección queda sustituida por el documento autoritativo `Productos/Anexo_G_Procedimiento_Revocacion.md`. No deberá utilizarse como fuente normativa ni operativa independiente.

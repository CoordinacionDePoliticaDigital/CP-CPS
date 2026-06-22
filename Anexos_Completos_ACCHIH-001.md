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
1. **Iniciación:** El titular, su superior jerárquico, o la AC inician una solicitud de revocación.
2. **Autenticación de Solicitud:** Se verifica la identidad del solicitante o la legitimidad de la causa (ej. acta de defunción, oficio de despido).
3. **Procesamiento:** El sistema administrativo procesa la orden de revocar.
4. **Actualización de Estado:** El número de serie del certificado se incorpora al servicio OCSP (o CRL si aplica).
5. **Notificación:** Se envía un correo electrónico al titular informando que su certificado ha sido revocado y la fecha/hora de la acción.
# Anexos H al J: Procedimientos de Seguridad y Continuidad (Alto Nivel)

## Anexo H. Procedimiento de Gestión de Incidentes
1. **Detección y Registro:** Cualquier anomalía técnica, operativa o de seguridad se reporta al Oficial de Seguridad y se registra en el sistema de tickets.
2. **Clasificación y Contención:** Se evalúa la criticidad (Baja, Media, Alta, Crítica). Si es crítico (ej. compromiso de claves), se aíslan los sistemas afectados de la red.
3. **Erradicación y Recuperación:** El equipo de TI elimina la causa raíz del incidente y restaura los servicios afectados desde el último respaldo limpio.
4. **Notificación:** En caso de afectación a terceros, se emiten avisos en el portal oficial y comunicaciones directas.
5. **Lecciones Aprendidas:** Se documenta el análisis post-mortem para mejorar los controles preventivos.

## Anexo I. Procedimiento de Continuidad Operativa (DRP/BCP)
1. **Respaldo Regular:** Generación automatizada de respaldos de bases de datos e instanciación de almacenamiento de objetos distribuidos de alta durabilidad para conservar bitácoras, evidencias y configuraciones.
2. **Alta Disponibilidad y Escalamiento:** Uso nativo de orquestación de contenedores con escalamiento automático y bases de datos desplegadas en múltiples zonas de disponibilidad (Multi-AZ) para evitar interrupciones en los servicios de firma, OCSP y TSA.
3. **Restauración Criptográfica:** Procedimientos respaldados en la nube mediante módulos de seguridad en hardware (HSM) e infraestructura como código (IaC), permitiendo reconstruir la arquitectura perimetral y lógica rápidamente en caso de desastre regional.
4. **Pruebas y Simulacros:** Ejecución obligatoria de pruebas de recuperación y simulacros de failover entre zonas de disponibilidad.

## Anexo J. Procedimiento de Cese de Operaciones
1. **Planeación:** Si la Autoridad de Certificación debe dejar de operar permanentemente, se redactará un plan detallado aprobado por el Consejo Técnico con meses de antelación.
2. **Aviso Público:** Publicación masiva anunciando la fecha límite de operación y emisión.
3. **Revocación Masiva o Caducidad:** Decisión técnica sobre si revocar todos los certificados activos o dejarlos expirar de forma natural manteniendo vivo únicamente el servicio OCSP.
4. **Custodia de Llaves y Destrucción:** Destrucción criptográfica segura de las claves privadas de la CA Raíz.
5. **Archivo Histórico:** Resguardo permanente de las bitácoras, evidencias de enrolamiento y base de datos de certificados bajo las leyes archivísticas estatales para futuras auditorías o juicios.
# Anexo P. Términos y Condiciones de Uso
*Nota: Este documento consolida las declaraciones y responsabilidades del titular derivadas de la "Firma Electrónica Avanzada del Estado de Chihuahua".*

**Declaraciones preliminares:** Se reconoce el derecho que tienen las personas para interactuar con los órganos del Estado o entre sí, a través del uso de las herramientas tecnológicas y el deber que tienen tanto dichos entes, como la ciudadanía de respetar, proteger y garantizar el ejercicio de este derecho.
La utilización del Certificado de Firma Electrónica Avanzada del Estado de Chihuahua constituye el pleno y expreso consentimiento por parte de la persona titular para observar y sujetarse respecto de cada uno de los términos y condiciones que aquí se contienen.

**Responsabilidades de Resguardo:**
Que la Firma Electrónica Avanzada del Estado de Chihuahua se compone de los archivos con terminación ".KEY" (la llave privada) más el que lleva terminación ".CER" (el certificado digital) y la contraseña de la llave privada, los cuales quedarán en resguardo bajo la exclusiva responsabilidad del titular. Es obligación actuar con la adecuada diligencia y establecer los medios razonables para mantener absoluta confidencialidad respecto del resguardo de estos archivos.

**Vigencia y Extinción:**
La vigencia máxima es de cuatro años. En caso de riesgo de confidencialidad, separación del cargo, fallecimiento, pérdida de facultades legales o incumplimiento, se procederá a la revocación o extinción definitiva.

---

# Anexo Q. Aviso de Privacidad Integral
*Nota: Resumen de las disposiciones de privacidad aplicables al sistema de Firma Electrónica Avanzada.*

La Coordinación de Política Digital del Estado de Chihuahua es la responsable del tratamiento de los datos personales que nos proporcione, los cuales serán protegidos conforme a lo dispuesto por la Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados, la Ley de Protección de Datos Personales del Estado de Chihuahua y demás normatividad aplicable.

**¿Qué datos personales recabamos y para qué finalidad?**
Los datos personales que recabemos serán utilizados con la finalidad de verificar y autenticar la identidad de las personas usuarias, gestionar el proceso de enrolamiento remoto y presencial, generar, administrar, renovar o revocar certificados digitales.
Se solicitarán:
- Nombre completo
- CURP y RFC
- Número telefónico y correo electrónico
- Datos de autenticación y bitácoras electrónicas

**Transferencia de datos personales**
Se informa que no se realizarán transferencias de datos personales, salvo aquellas necesarias para atender requerimientos de información de una autoridad competente, debidamente fundados y motivados.

**Derechos ARCO**
Usted podrá ejercer sus derechos de acceso, rectificación, cancelación, oposición y portabilidad de datos personales directamente ante la Unidad de Transparencia de la Coordinación de Política Digital del Estado de Chihuahua.
# Anexo A. Perfil Técnico de Certificados

> [!WARNING]
> *Nota: Este documento ha sido adaptado para reflejar el perfil técnico de los certificados emitidos en el entorno productivo de la Autoridad de Certificación de Gobierno del Estado de Chihuahua, desplegado en infraestructura de alta disponibilidad.*

## 1. Introducción
El presente anexo define los perfiles técnicos de los certificados digitales emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua (AC), de conformidad con el estándar internacional X.509 v3 y el RFC 5280.

## 2. Perfil del Certificado Raíz (AC Raíz)
- **Versión:** V3
- **Número de Serie:** Generado de forma aleatoria y única (ej. 30303030...).

| Atributo | Valor | Descripción |
| :--- | :--- | :--- |
| **Issuer (Emisor)** | `CN=Autoridad de Certificación de Gobierno del Estado de Chihuahua, E=autoridad.certificadora@chihuahua.gob.mx, O=Gobierno del Estado de Chihuahua, OU=Coordinación de Política Digital, L=Chihuahua, S=Chihuahua, C=MX, PostalCode=31000` | Entidad que emite y firma el certificado (Estado de Chihuahua). |
| **Subject (Titular)** | Igual al Issuer | Para el certificado raíz, el titular es la misma AC. |
| **Validity (Vigencia)** | Not Before: [Fecha de emisión]<br>Not After: [Fecha de emisión + 15 años] | Periodo de validez. (15 años). |
| **Key Size** | RSA 4096 bits | Longitud robusta recomendada. |
| **Signature Algorithm** | `sha512RSA` | Algoritmo de firma de alta seguridad soportado por KMS. |

### Extensiones del Certificado Raíz

| Extensión | Criticidad | Valor | Explicación |
| :--- | :--- | :--- | :--- |
| **Key Usage** | Crítica | `Digital Signature, Non-Repudiation, Key Encipherment, Data Encipherment, Certificate Sign, CRL Sign` | Permite firmar certificados, CRLs, y cifrado. |
| **Basic Constraints** | Crí­tica | `Subject Type=CA`, `Path Length Constraint=None` | Indica que es una Autoridad de Certificación. |
| **Extended Key Usage** | Crí­tica | `Time Stamping (1.3.6.1.5.5.7.3.8)` | Permite que el certificado se use para operaciones asociadas a TSA. |
| **Subject Key Identifier** | No crítica | [Hash de la clave pública] | Identificador de la llave. |

## 3. Perfil del Certificado de Usuario Final (Firma Electrónica Avanzada)
- **Versión:** V3
- **Número de Serie:** Único.
- **Algoritmo de Firma:** `sha512RSA`.
- **Validez:** Hasta 4 años.
- **Subject:** 
  - `CN` = Nombre de la persona física
  - `E` = Correo electrónico
  - `OID.2.5.4.45` = RFC o CURP
  - `SERIALNUMBER` = CURP o RFC
- **Subject Public Key Info:** RSA 2048 bits.

### Extensiones del Certificado de Usuario Final

| Extensión | Criticidad | Valor |
| :--- | :--- | :--- |
| **Key Usage** | Crítica | `Digital Signature, Non-Repudiation, Key Encipherment, Key Agreement` |
| **Extended Key Usage** | No crítica | `Client Authentication (1.3.6.1.5.5.7.3.2), Secure Email (1.3.6.1.5.5.7.3.4)` |
| **Basic Constraints** | Crítica | `Subject Type=End Entity`, `Path Length Constraint=None` |
| **Subject Alternative Name** | No crítica | `RFC822 Name=[correo electrónico]` |
| **Authority Information Access** | No crítica | URLs de OCSP y CA Issuers |
# Anexo B. Matriz de Roles y Responsabilidades

El presente anexo describe los principales roles involucrados en la infraestructura de la Autoridad de Certificación y sus responsabilidades esenciales.

| Rol | Responsabilidades Principales |
|---|---|
| **Coordinación de Política Digital** | Autorizar la emisión de políticas y prácticas. Ejercer el liderazgo institucional. Designar a los administradores principales. |
| **Consejo Técnico** | Aprobar la CP y CPS. Fungir como órgano colegiado de toma de decisiones estratégicas. |
| **Administrador de PKI (Root Admin)** | Gestionar la clave privada de la CA Raíz. Ejecutar las ceremonias de generación de claves. Configurar los servicios criptográficos core. |
| **Oficial de Seguridad** | Monitorear el cumplimiento normativo. Revisar bitácoras. Gestionar incidentes de seguridad y aprobar controles de acceso. |
| **Agente Registrador (RA)** | Validar presencial o remotamente la identidad de los solicitantes. Cotejar documentación. Autorizar o denegar solicitudes de enrolamiento. |
| **Persona Titular / Firmante** | Resguardar celosamente su clave privada y contraseña. Informar sobre cambios en sus datos. Solicitar revocación en caso de compromiso. |
| **Tercero Confiante** | Validar la vigencia, revocación (OCSP/CRL), cadena de confianza e integridad documental de los certificados y firmas que recibe antes de otorgarles validez. |
# Anexo C. Matriz de Causas de Revocación

Este anexo clasifica y consolida las causas por las cuales se deberá proceder a la revocación definitiva de un certificado de Firma Electrónica Avanzada emitido por la Autoridad de Certificación, según el tipo de titular.

## 1. Causas Generales (Aplicables a todos los titulares)
| Causa | Supuesto | Responsable de solicitar / ejecutar |
|---|---|---|
| **Solicitud expresa** | El titular ya no desea usar el certificado. | Titular |
| **Compromiso de clave** | Sospecha o certeza de que la clave privada, contraseña o medio de almacenamiento ha sido robado, copiado o vulnerado. | Titular / Agente Registrador |
| **Información Falsa** | Detección de que el certificado se emitió con información alterada o falsa. | Autoridad de Certificación |
| **Fallecimiento** | Deceso de la persona física titular. | Tercero autorizado / Autoridad de Certificación |
| **Resolución de Autoridad** | Mandato judicial o administrativo competente. | Autoridad de Certificación |

## 2. Causas Específicas para Servidores Públicos
| Causa | Supuesto | Responsable de solicitar / ejecutar |
|---|---|---|
| **Baja laboral** | Renuncia, despido o cese de relación laboral con la institución. | Área de Recursos Humanos / Superior Jerárquico |
| **Cambio de Cargo o Dependencia** | Cambio que implique la pérdida de las facultades bajo las cuales se expidió el certificado. | Titular / Superior Jerárquico |
| **Pérdida de Autorización** | El superior jerárquico retira el permiso para que el funcionario ostente la representación institucional. | Superior Jerárquico |

## 3. Causas Específicas para Representantes Legales
| Causa | Supuesto | Responsable de solicitar / ejecutar |
|---|---|---|
| **Pérdida de Poderes** | Revocación, limitación o término del poder notarial. | Representante / Persona Moral / Autoridad |
| **Extinción de la Sociedad** | Fusión, escisión o liquidación de la empresa que representa. | Liquidador / Autoridad |
# Anexo K. Perfil PAdES Institucional

> [!WARNING]
> *Nota: Este documento ha sido adaptado para reflejar el perfil técnico PAdES utilizado en el entorno productivo de la plataforma Firmame de Gobierno del Estado de Chihuahua.*

## 1. Estándar Base
La plataforma institucional utilizará el formato **PAdES (PDF Advanced Electronic Signatures)**, integrando constancias de conservación y validación a largo plazo. Las firmas se generan y estampan a través de la infraestructura criptográfica de la Autoridad de Certificación de Gobierno del Estado de Chihuahua.


## 2. Algoritmos Soportados
- **Hash:** SHA-256 o superior.
- **Firma:** `sha512RSA` con llaves RSA de 2048 bits (para usuarios y sellos de tiempo operativos) y 4096 bits (para constancias de conservación a largo plazo).

## 3. Elementos Visuales de la Firma y Sellos
La representación visual de la firma en el documento PDF contendrá elementos de validación humana y criptográfica:
- **Datos del Firmante:** Nombre, RFC/CURP y correo electrónico.
- **Trazo Autógrafo:** Incorporación de la imagen del dibujo de trazo de firma autógrafa capturada en la aplicación (Servicio Canvas).
- **Evidencia Temporal:** Estampa de tiempo aplicada criptográficamente por la TSA del Gobierno del Estado de Chihuahua y visible en el documento.
- **Hoja de Firmas:** Inclusión de una hoja anexa final que resume las firmas recolectadas, los códigos QR de verificación, el folio o identificador único del documento, y el respaldo legal avalado por la Autoridad Certificadora.
# Anexo L. Política de Sellado de Tiempo (TSP)

> [!WARNING]
> *Nota: Este documento ha sido redactado con base en estándares genéricos (RFC 3161) y queda pendiente de revisión y aceptación final para su ajuste al alcance propio de la Autoridad de Certificación de Gobierno del Estado de Chihuahua.*

## 1. Alcance
Establece las reglas técnicas y operativas bajo las cuales opera la Autoridad de Sellado de Tiempo (TSA) vinculada a la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

## 2. Referencia Temporal
La TSA se sincronizará utilizando servicios de tiempo de alta disponibilidad en la nube. Este servicio se respalda por una flota de relojes atómicos y satelitales redundantes, ajustados al estándar global Tiempo Universal Coordinado (UTC), ofreciendo una precisión equivalente o superior a la del Centro Nacional de Metrología (CENAM).

## 3. Emisión de Sellos de Tiempo (Time-Stamps)
- **Formato:** Acorde a RFC 3161 (`TimeStampReq` y `TimeStampResp`).
- **Gestión Criptográfica:** Las operaciones de firma de la TSA se delegan a un Módulo de Seguridad en Hardware (KMS) configurado en la nube.
- **Algoritmo de Firma de la TSA:** Se generarán firmas con `sha512RSA`. La infraestructura mantiene dos perfiles de certificados de Autoridad de Sellado:
  - **TSA 2048 (`CN=Gobierno del Estado de Chihuahua TSA 2048`):** Llave de 2048 bits para sellos operativos generales.
  - **TSA 4096 (`CN=Gobierno del Estado de Chihuahua TSA 4096`):** Llave de 4096 bits para constancias de conservación de largo plazo.
- Ambos certificados operan como entidades finales (`Subject Type=End Entity`), limitados estrictamente al uso de **Firma Digital** y **Time Stamping (1.3.6.1.5.5.7.3.8)**.

## 4. Retención de Bitácoras
Las transacciones de emisión de sellos de tiempo serán auditadas y conservadas conforme a la normativa archivística estatal aplicable.
# Anexo M. Formato de Autorización de Superior Jerárquico

**Autoridad de Certificación de Gobierno del Estado de Chihuahua**
**Formato para Solicitud de Firma Electrónica Avanzada**

**Fecha:** {{FECHA}}
**Folio:** {{FOLIO}}

---

**DATOS DEL SERVIDOR PÚBLICO SOLICITANTE**
- **Nombre Completo:** _________________________________________________
- **CURP:** _________________________________________________
- **RFC:** _________________________________________________
- **Cargo:** _________________________________________________
- **Dependencia / Entidad:** _________________________________________________

**DECLARACIÓN DEL SUPERIOR JERÁRQUICO**
Por este medio, AUTORIZO que la persona servidora pública arriba mencionada obtenga el Certificado de Firma Electrónica Avanzada emitido por la Autoridad de Certificación, para su uso exclusivo en el ejercicio de sus funciones oficiales institucionales. Me comprometo a notificar oportunamente a la Autoridad de Certificación en caso de baja, cambio de adscripción o cambio de cargo que amerite la revocación de dicho certificado.

**DATOS DEL SUPERIOR JERÁRQUICO**
- **Nombre Completo:** _________________________________________________
- **Cargo:** _________________________________________________
- **Firma Autógrafa / Electrónica:** _________________________________________________

---
# Anexo N. Formato de Solicitud de Certificado

**Autoridad de Certificación de Gobierno del Estado de Chihuahua**
**Formato para Solicitud de Firma Electrónica Avanzada**

**Fecha:** {{FECHA}}
**Folio:** {{FOLIO}}

---

**1. TIPO DE SOLICITANTE**
- [ ] Persona Física Ciudadana
- [ ] Persona Servidora Pública
- [ ] Persona Física Representante Legal

**2. DATOS DE IDENTIFICACIÓN**
- **Nombre Completo:** _________________________________________________
- **CURP:** _________________________________________________
- **RFC (Obligatorio):** _________________________________________________
- **Correo Electrónico:** _________________________________________________
- **Teléfono:** _________________________________________________

**3. DECLARACIONES Y ACEPTACIÓN**
Declaro bajo protesta de decir verdad que los datos e información proporcionados son ciertos y verificables. Acepto sujetarme a los Términos y Condiciones de Uso del Certificado, así como a las causales de revocación establecidas en la Política de Certificación (CP-ACCHIH-001).

**Firma del Solicitante:** _________________________________________________

---
# Anexo O. Formato de Solicitud de Revocación

**Autoridad de Certificación de Gobierno del Estado de Chihuahua**
**Formato para Solicitud de Revocación de Firma Electrónica Avanzada**

**Fecha:** {{FECHA}}
**Folio:** {{FOLIO}}

---

**1. DATOS DEL TITULAR DEL CERTIFICADO**
- **Nombre Completo:** _________________________________________________
- **CURP / RFC:** _________________________________________________
- **Número de Serie del Certificado (si se conoce):** ________________________________

**2. MOTIVO DE LA REVOCACIÓN**
- [ ] Solicitud personal (ya no se requiere)
- [ ] Pérdida, robo o compromiso de la clave privada/contraseña
- [ ] Cese de funciones laborales institucionales / Pérdida de facultades legales
- [ ] Fallecimiento del titular (adjuntar acta)
- [ ] Otra causa: _________________________________________________

**3. DECLARACIÓN**
Solicito formal e irrevocablemente la revocación definitiva del certificado arriba mencionado. Entiendo que esta acción no puede deshacerse y cualquier firma realizada posteriormente con este certificado carecerá de validez jurídica.

**Nombre y Firma del Solicitante:** _________________________________________________
*(Puede ser el titular, superior jerárquico o tercero autorizado)*

---

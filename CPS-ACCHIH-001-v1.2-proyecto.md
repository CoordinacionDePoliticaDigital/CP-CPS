<div align="center">
  <img src="./img/logo1.png" alt="Gobierno del Estado" height="80" style="margin-right: 30px;" />
  <img src="./img/logo2.png" alt="Autoridad Certificadora" height="80" />
</div>
<br>

# Declaración de Prácticas de Certificación (CPS)
## Autoridad de Certificación de Gobierno del Estado de Chihuahua

**Clave del documento:** CPS-ACCHIH-001  
**OID:** 1.3.6.1.4.1.63888.1.2  
**Versión:** 1.2  
**Estado:** Proyecto  
**Fecha de emisión:** Pendiente de formalización  
**Fecha de entrada en vigor:** Octubre 2024  
**Autoridad responsable:** Coordinación de Política Digital  
**Autoridad emisora:** Autoridad de Certificación de Gobierno del Estado de Chihuahua  
**Denominación institucional de difusión:** Autoridad Certificadora  
**Órgano de aprobación:** Coordinación de Política Digital y Consejo Técnico  
**Sitio de publicación:** autoridadcertificadora.chihuahua.gob.mx  
**Apartado de publicación:** Normatividad Operativa  
**Periodicidad de revisión:** Cuando existan cambios normativos, técnicos, operativos o de seguridad que lo ameriten, o por determinación de la Coordinación de Política Digital o del Consejo Técnico

---

# Control documental

| Elemento | Descripción |
|---|---|
| Nombre del documento | Declaración de Prácticas de Certificación de la Autoridad de Certificación de Gobierno del Estado de Chihuahua |
| Clave | CPS-ACCHIH-001 |
| OID | 1.3.6.1.4.1.63888.1.2 |
| Versión | 1.2 |
| Estado | Proyecto |
| Fecha de emisión | Pendiente de formalización |
| Fecha de entrada en vigor | Octubre 2024 |
| Autoridad responsable | Coordinación de Política Digital |
| Autoridad emisora | Autoridad de Certificación de Gobierno del Estado de Chihuahua |
| Denominación institucional de difusión | Autoridad Certificadora |
| Aprobación | Coordinación de Política Digital y Consejo Técnico |
| Política asociada | CP-ACCHIH-001, OID 1.3.6.1.4.1.63888.1.1 |
| Ubicación oficial de publicación | autoridadcertificadora.chihuahua.gob.mx, apartado Normatividad Operativa |
| Periodicidad de revisión | Cuando existan cambios normativos, técnicos, operativos o de seguridad que lo ameriten, o por determinación de la Coordinación de Política Digital o del Consejo Técnico |

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---:|---|---|
| 1.0 | Octubre 2024 | Emisión inicial del documento | Coordinación de Política Digital |
| 1.1 | Pendiente de formalización | Integración de información técnica y operativa derivada del despliegue inicial | Coordinación de Política Digital |
| 1.2 | Pendiente de formalización | Alineación con la CP v1.2, perfiles vigentes y objetivo, CENAM, transición PKI y conservación | Coordinación de Política Digital |

---

# 1. Introducción

## 1.1. Visión general

Esta Declaración de Prácticas de Certificación describe cómo la Autoridad de Certificación de Gobierno del Estado de Chihuahua implementa las reglas establecidas en la Política de Certificación CP-ACCHIH-001. Comprende procedimientos, controles, roles, mecanismos tecnológicos, evidencias, bitácoras, continuidad operativa, gestión de incidentes y prácticas administrativas y técnicas aplicables al ciclo de vida de los certificados y servicios relacionados.

En caso de discrepancia prevalecerá la Política de Certificación, salvo que esta CPS establezca controles más estrictos que no la contradigan.

## 1.2. Identificación del documento

- **Nombre:** Declaración de Prácticas de Certificación.
- **Clave:** CPS-ACCHIH-001.
- **OID:** `1.3.6.1.4.1.63888.1.2`.
- **OID de la Política asociada:** `1.3.6.1.4.1.63888.1.1`.
- **IANA PEN institucional:** `1.3.6.1.4.1.63888`.

## 1.3. Entidades PKI

- **Autoridad de Certificación:** entidad responsable de emitir, administrar, validar y revocar certificados.
- **Autoridad de Registro y agentes autorizados:** responsables de verificar identidad, documentación, autorizaciones y solicitudes.
- **Autoridad de Sellado de Tiempo:** servicio criptográfico independiente que emite sellos de tiempo conforme a RFC 3161.
- **Respondedores OCSP:** servicios autorizados que publican el estado de los certificados emitidos por su autoridad emisora correspondiente.
- **Personas suscriptoras o titulares:** personas físicas y personas servidoras públicas titulares de certificados.
- **Terceros confiantes:** personas, instituciones y sistemas que validan certificados, firmas y sellos de tiempo.

## 1.4. Neutralidad tecnológica

Las referencias a servicios de nube, gestión de claves, orquestación, almacenamiento, redes, identidad o mensajería describen capacidades funcionales y controles requeridos. Las secciones 5 a 8 de esta CPS documentan la arquitectura funcional, las categorías de servicios tecnológicos, los controles aplicados y el modelo general de implementación. Los nombres de proveedores, productos, marcas, cuentas, regiones y configuraciones concretas se documentarán en inventarios, diagramas, procedimientos y registros internos sujetos a control de cambios, cuando su publicación pueda afectar la seguridad, la continuidad operativa o las condiciones de contratación.

---

# 2. Publicación y repositorios

La Autoridad de Certificación publicará en `autoridadcertificadora.chihuahua.gob.mx`, dentro del apartado Normatividad Operativa, la CP, la CPS, certificados públicos de infraestructura, información de estado, CRL cuando corresponda, términos, avisos, formatos y guías.

El servicio OCSP será el mecanismo principal de validación de estado. Las CRL serán complementarias para respaldo, interoperabilidad, continuidad operativa y validación histórica.

Los puntos de distribución, direcciones de servicio, certificados públicos y huellas criptográficas deberán mantenerse actualizados en el repositorio oficial y en los perfiles técnicos aplicables.

---

# 3. Identificación y autenticación

## 3.1. Registro inicial

La identificación podrá realizarse de forma presencial, remota o mixta. Se validarán, según el tipo de certificado, nombre completo, CURP, RFC, correo electrónico, identificación oficial o mecanismo equivalente y la información adicional necesaria.

Para personas servidoras públicas se validará además la dependencia, unidad administrativa, cargo, situación activa y autorización del superior jerárquico o unidad competente.

Para representantes legales se verificará la identidad de la persona física, la existencia de la persona moral, su domicilio establecido en el Estado de Chihuahua y la vigencia y alcance de las facultades de representación.

Los servicios automatizados de verificación de identidad tendrán carácter auxiliar y no decidirán por sí mismos la emisión, rechazo o revocación.

## 3.2. Renovación

La renovación solo procederá cuando el certificado vigente pueda utilizarse para firmar la solicitud, no exista causa de revocación y los datos y autorizaciones continúen vigentes.

La renovación implicará la revocación definitiva del certificado anterior y la emisión de un certificado nuevo. No existe reemisión ni reactivación.

Los certificados vencidos, revocados o cuyos datos hayan cambiado requerirán un nuevo trámite de emisión con la validación aplicable.

---

# 4. Requisitos operativos del ciclo de vida

## 4.1. Solicitud y emisión

La solicitud se realizará mediante los sistemas autorizados. El par de claves de usuario final se generará localmente en el dispositivo de la persona solicitante. La clave privada no será transmitida, recibida, almacenada, custodiada, respaldada ni recuperada por la AC, la AR, los agentes o los servicios de verificación.

La solicitud de certificado deberá incluir una prueba de posesión de la clave privada correspondiente a la clave pública presentada.

La emisión requerirá validación de identidad, revisión de requisitos y autorización cuando corresponda. Los acuses solo se generarán después de la ejecución satisfactoria del trámite.

## 4.2. Entrega y aceptación

El certificado emitido se pondrá a disposición de la persona titular mediante un mecanismo autenticado y se notificará por un canal institucional autorizado.

La aceptación comprenderá la verificación de los datos contenidos en el certificado y la aceptación de la CP, la CPS, los términos y condiciones de uso y el aviso de privacidad aplicable.

## 4.3. Revocación

La revocación será definitiva e irreversible. No existe suspensión temporal.

Podrá ser iniciada por la persona titular mediante una solicitud firmada con el certificado vigente o por un agente autorizado cuando la persona titular no disponga de la clave, desconozca su contraseña o concurra otra causal que requiera intervención asistida.

El sistema solo ejecutará revocaciones asistidas firmadas por una persona con rol de agente autorizado. La fecha y hora efectiva deberán registrarse y publicarse mediante OCSP y, cuando corresponda, CRL.

La separación del cargo, baja del servicio público, cambio de dependencia, unidad administrativa o cargo distinto dará lugar a revocación definitiva y a una nueva solicitud con la autorización correspondiente.

---

# 5. Controles de gestión, operativos y físicos

## 5.1. Controles físicos y ambientales

Los componentes de infraestructura deberán operar en instalaciones o centros de datos con controles de acceso físico, energía, climatización, detección y respuesta a incidentes, continuidad y registro de accesos acordes con la criticidad de los servicios.

Las estaciones y oficinas utilizadas por agentes autorizados deberán contar con medidas de acceso físico, protección de dispositivos, bloqueo de sesión, manejo seguro de documentos y prevención de observación o extracción no autorizada.

## 5.2. Roles y separación de funciones

Se mantendrán roles diferenciados para administración de infraestructura, gestión criptográfica, autorización de emisiones, revocación, auditoría, seguridad, soporte y operación.

Las operaciones sensibles requerirán mínimo privilegio, autenticación multifactor, trazabilidad y, cuando el riesgo lo amerite, control dual o aprobación adicional.

## 5.3. Auditoría y bitácoras

Se registrarán solicitudes, validaciones, autorizaciones, emisiones, renovaciones, revocaciones, consultas OCSP, publicaciones de CRL, firmas, sellos de tiempo, accesos administrativos, cambios de configuración, fallas, respaldos, restauraciones e incidentes.

Las bitácoras deberán protegerse contra alteración, eliminación y acceso no autorizado. La AC realizará auditorías internas y atenderá las que ordene la Secretaría de la Función Pública u otra autoridad competente.

## 5.4. Continuidad operativa

La infraestructura deberá contar con redundancia, respaldos protegidos, recuperación de configuraciones, bases de datos, bitácoras y evidencias, procedimientos alternos de validación y revocación, responsables designados, prioridades de recuperación, comunicaciones y pruebas periódicas.

---

# 6. Controles de seguridad técnica

## 6.1. Gestión de claves de la AC

Las claves privadas de la AC se administrarán mediante servicios criptográficos autorizados y no exportables por defecto, con mínimo privilegio, autenticación multifactor, segregación de funciones, bitácoras y control de cambios.

Cualquier excepción a la no exportabilidad de la clave raíz requerirá análisis de riesgo documentado, aprobación formal de la Coordinación de Política Digital y controles compensatorios equivalentes.

La clave de la AC raíz no se utilizará para sellado de tiempo, cifrado de datos, firma de documentos de usuario final, autenticación de cliente o servidor ni firma de código. OCSP y TSA utilizarán claves y certificados independientes.

## 6.2. Gestión de claves de usuario

Las claves privadas de usuario final se generarán localmente y permanecerán bajo control exclusivo de la persona titular. La AC no ofrecerá recuperación ni custodia de dichas claves.

## 6.3. Seguridad informática y de red

Los sistemas se segmentarán por función y ambiente. Las comunicaciones usarán protocolos cifrados vigentes, autenticación fuerte, listas de control, monitoreo, gestión de vulnerabilidades, protección contra abuso, registro de eventos y procedimientos de respuesta a incidentes.

Las versiones mínimas de protocolos, algoritmos, tamaños de clave y configuraciones concretas se establecerán en los perfiles técnicos y estándares internos aprobados.

---

# 7. Perfiles de certificados, OCSP y TSA

## 7.1. Perfiles vigentes durante la transición

Los certificados actualmente desplegados conservarán reconocimiento hasta su expiración o revocación. Sus extensiones y usos documentan una condición transitoria y no deberán utilizarse como plantilla para nuevas emisiones después de la aprobación y puesta en operación de los perfiles objetivo.

El certificado raíz vigente es una raíz emisora en línea y presenta extensiones amplias, incluyendo usos que no corresponden al perfil objetivo. Los certificados de usuario final vigentes pueden incluir usos extendidos de autenticación de cliente y correo seguro. Estas condiciones deberán mantenerse identificadas en inventarios y validadores para preservar la interoperabilidad histórica sin reproducirlas en nuevas emisiones.

## 7.2. Arquitectura objetivo y perfiles nuevos

La arquitectura objetivo será:

**AC raíz fuera de línea → AC intermedia emisora → certificado de entidad final.**

La raíz utilizará `pathLenConstraint=1` y únicamente `keyCertSign` y `cRLSign`, sin EKU. Cada intermedia emisora utilizará `pathLenConstraint=0` y no podrá emitir otras autoridades subordinadas.

Los certificados de firma electrónica avanzada de usuario final estarán destinados a firma de documentos y no incluirán `clientAuth`, `serverAuth`, `emailProtection`, `codeSigning`, `timeStamping` u `OCSPSigning`, salvo que exista un perfil separado, aprobado y asociado a un OID específico.

El `Subject` de los certificados de usuario final mantendrá el mapeo actualmente desplegado para preservar compatibilidad con los certificados ya emitidos y con los sistemas validadores:

- `commonName` (`2.5.4.3`) contendrá el nombre completo de la persona titular.
- `emailAddress` (`1.2.840.113549.1.9.1`) contendrá el correo electrónico validado.
- `serialNumber` (`2.5.4.5`) contendrá la CURP.
- `x500UniqueIdentifier` (`2.5.4.45`) contendrá el RFC.

Los certificados históricos que presenten una etiqueta distinta en alguna herramienta de visualización conservarán su validez siempre que el atributo codificado sea el OID `2.5.4.45`. La CPS utilizará exclusivamente la denominación normativa `x500UniqueIdentifier` para dicho OID.

La CURP y el RFC no deberán intercambiarse, duplicarse en ambos atributos ni asignarse a campos distintos dentro de este perfil. Los certificados previamente emitidos con este mapeo conservarán plena validez hasta su expiración o revocación.

Los detalles normativos adicionales se regirán por los siguientes documentos controlados:

| Documento | Versión controlada | Fecha de entrada en vigor | Referencia de control de cambios |
|---|---:|---|---|
| Anexo A. Perfil Técnico de Certificados | 1.2 | Octubre 2024 | Historial y control documental del propio Anexo A |
| Anexo K. Perfil PAdES Institucional | 1.2 | Octubre 2024 | Historial y control documental del propio Anexo K |
| Anexo L. Política de Sellado de Tiempo | 1.2 | Octubre 2024 | Historial y control documental del propio Anexo L |

Toda modificación de versión, fecha de entrada en vigor o regla normativa de cualquiera de estos anexos requerirá revisar y actualizar esta CPS, registrar el cambio en su historial y mantener sincronizadas las referencias anteriores antes de su publicación o aplicación productiva.

## 7.3. OCSP

OCSP será el mecanismo principal de validación de estado. Cada certificado de respondedor OCSP deberá ser emitido directamente por la autoridad emisora de los certificados cuyo estado responde.

Los certificados emitidos directamente por la raíz vigente requerirán un respondedor directamente emitido por esa raíz. Los certificados emitidos por una intermedia requerirán un respondedor directamente emitido por esa misma intermedia. Un certificado de respondedor no podrá reutilizarse fuera del ámbito de su emisor.

El certificado OCSP utilizará exclusivamente el EKU crítico `id-kp-OCSPSigning`.

## 7.4. TSA y referencia temporal

La TSA utilizará certificados independientes cuyo único EKU será `timeStamping` (`1.3.6.1.5.5.7.3.8`) marcado como crítico.

La referencia oficial será la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya. Podrán utilizarse servicios técnicos de sincronización de alta disponibilidad siempre que exista trazabilidad documentada respecto de dicha referencia y del Tiempo Universal Coordinado.

El parámetro operativo único de sincronización se controlará mediante la siguiente ficha auditable:

| Campo | Valor o estado requerido |
|---|---|
| Identificador | POT-TSA-001 |
| Versión | 1.0 |
| Tolerancia máxima | Pendiente de aprobación técnica y operativa |
| Unidad de medida | Milisegundos |
| Método de medición | Pendiente de aprobación técnica y operativa |
| Frecuencia de verificación | Pendiente de aprobación técnica y operativa |
| Fuentes de contraste | Pendiente de aprobación técnica y operativa |
| Acciones ante desviaciones | Pendiente de aprobación técnica y operativa |
| Evidencias conservadas | Registros de medición, alertas, ajustes, incidentes y autorizaciones |
| Autoridad aprobadora | Coordinación de Política Digital y Consejo Técnico |
| Fecha de entrada en vigor | No aplicable hasta su aprobación formal |

La tolerancia no podrá aplicarse, publicarse ni declararse mientras la ficha no contenga un valor numérico aprobado, método de medición, frecuencia, fuentes de contraste, acciones ante desviaciones, versión vigente y fecha expresa de entrada en vigor. Hasta entonces, no deberá declararse una tolerancia numérica ni equivalencia metrológica no sustentada.

Todo documento firmado mediante la plataforma institucional deberá incorporar sello de tiempo. Los perfiles PAdES se regirán por el Anexo K versión 1.2 y la política operativa de sellado por el Anexo L versión 1.2, ambos con fecha de entrada en vigor de octubre de 2024 y sujetos al control de cambios establecido en la sección 7.2.

---

# 8. Transición de la arquitectura PKI

La raíz emisora en línea vigente se reconoce como arquitectura transitoria con controles compensatorios de acceso, monitoreo, trazabilidad, separación de funciones, continuidad y respuesta a incidentes.

La aceptación transitoria caducará en un plazo máximo de veinticuatro meses contado desde octubre de 2024, fecha de entrada en vigor de la CP v1.2. Al finalizar dicho plazo, la raíz vigente deberá haber dejado de emitir certificados nuevos, sin afectar la validación histórica de los certificados emitidos antes de su retiro.

La Coordinación de Política Digital, por conducto de la unidad responsable de la Autoridad de Certificación, ejecutará y documentará la migración. El avance se revisará trimestralmente y se reportará al Consejo Técnico.

El cese de emisión de la raíz vigente requerirá evidencia documentada de que:

a) Las pruebas de interoperabilidad de la nueva cadena concluyeron satisfactoriamente en los sistemas y escenarios definidos en el plan de pruebas;  
b) El cien por ciento de los validadores críticos inventariados fue actualizado y probado, y existe un listado nominal de los validadores no críticos pendientes con responsable y fecha comprometida;  
c) La continuidad de OCSP y CRL fue verificada mediante pruebas funcionales, de disponibilidad y de validación histórica;  
d) La arquitectura vigente y la arquitectura objetivo coexistieron operativamente durante al menos noventa días naturales sin incidentes críticos atribuibles a la nueva cadena;  
e) Se publicaron la nueva cadena, sus huellas, puntos de distribución, instrucciones de confianza y avisos a terceros confiantes; y  
f) Las evidencias fueron revisadas por la unidad responsable de la Autoridad de Certificación y aprobadas por la Coordinación de Política Digital y el Consejo Técnico.

La transición incluirá ceremonia de generación de claves, perfiles aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia, inventario de dependencias, actualización de validadores, comunicación a terceros confiantes y procedimientos de retiro.

Para dependencias o validadores que no hayan concluido su migración al vencimiento de los veinticuatro meses se aplicará un plan de contingencia documentado, sin extender la emisión de nuevos certificados desde la raíz vigente. Dicho plan podrá contemplar ventanas controladas de actualización, soporte prioritario, validadores puente, distribución extraordinaria de cadenas de confianza y restricciones temporales de operación. Cada excepción operativa deberá contar con responsable, análisis de riesgo, fecha límite, controles compensatorios y aprobación de la Coordinación de Política Digital; el Consejo Técnico recibirá seguimiento hasta su cierre.

---

# 9. Conservación de documentos y evidencias

La plataforma conservará copia íntegra de los documentos firmados hasta por diez años, contados desde la fecha y hora consignadas en el sello de tiempo institucional incorporado al documento. Este será el evento único para calcular la fecha ordinaria de eliminación y sustentar la transferencia documental.

La conservación de la plataforma no sustituirá las obligaciones archivísticas de la dependencia responsable. La eliminación solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que exija conservar el documento o sus evidencias por más tiempo y se haya realizado la transferencia correspondiente.

Las evidencias de emisión, renovación, revocación, OCSP, CRL, sellado de tiempo, auditoría e incidentes se conservarán conforme a su finalidad, riesgo, temporalidad documental y normatividad aplicable.

---

# 10. Auditoría de cumplimiento

La AC realizará verificaciones periódicas sobre enrolamiento, emisión, revocación, gestión de claves, OCSP, TSA, bitácoras, continuidad, perfiles y publicación.

Los hallazgos deberán documentarse, asignarse a una persona responsable, clasificarse por riesgo y contar con fecha objetivo y evidencia de cierre.

---

# 11. Asuntos legales

Las responsabilidades, confidencialidad, propiedad y custodia de claves, causales de revocación, protección de datos personales, conservación, límites de responsabilidad y uso permitido se regirán por la CP, esta CPS, los términos y condiciones, los avisos de privacidad y la normatividad aplicable.

La emisión de certificados será gratuita para personas físicas ciudadanas y personas servidoras públicas. El acceso a la plataforma institucional no se deriva automáticamente de la emisión de un certificado ciudadano.

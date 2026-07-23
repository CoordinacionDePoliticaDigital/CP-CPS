# Anexo G. Procedimiento de revocación

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Declaración relacionada:** CPS-ACCHIH-001  
**Anexo relacionado:** Anexo C. Matriz de causas de revocación  
**Formato relacionado:** Anexo O. Formato de Solicitud de Revocación  
**Versión:** 1.2  
**Estado:** Proyecto  
**Autoridad responsable:** Coordinación de Política Digital  
**Órgano de aprobación:** Coordinación de Política Digital y Consejo Técnico  

---

## 1. Objeto

El presente procedimiento establece las actividades, controles, responsabilidades, evidencias y resultados aplicables a la revocación definitiva de certificados emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

La revocación será definitiva e irreversible. No existe suspensión temporal, reactivación, modificación ni reemisión del certificado revocado. Cuando la persona interesada continúe requiriendo un certificado, deberá iniciar un trámite independiente de nueva emisión o renovación, según corresponda.

## 2. Alcance

Este procedimiento será aplicable a:

- certificados de firma electrónica avanzada de personas físicas ciudadanas;
- certificados de personas servidoras públicas;
- certificados de personas físicas en calidad de representantes legales;
- certificados de servicios OCSP, TSA, CRL o infraestructura, con las adecuaciones técnicas y autorizaciones que correspondan;
- revocaciones iniciadas mediante CERTAC, por agentes autorizados, por la propia Autoridad de Certificación o por mandato de autoridad competente.

## 3. Documentos y reglas de referencia

La causa de revocación deberá seleccionarse exclusivamente del catálogo normalizado del Anexo C.

El Anexo O se utilizará como formato normativo de solicitud y registro cuando el trámite requiera intervención documental. Los formatos operativos de CERTAC podrán implementar los mismos campos de forma electrónica, siempre que conserven la clave normalizada, denominación, evidencias, autorizaciones, fechas, ejecutor y acuse exigidos.

En caso de discrepancia prevalecerán la CP, la CPS y el Anexo C, en ese orden.

## 4. Roles y responsabilidades

### 4.1. Persona titular

Podrá solicitar la revocación directa cuando conserve el certificado vigente, la clave privada y la contraseña necesarias para firmar la solicitud.

Deberá comunicar sin demora la pérdida, exposición, acceso no autorizado o sospecha de compromiso de la clave privada.

### 4.2. Agente autorizado

Deberá:

- verificar la identidad de la persona compareciente;
- validar su legitimidad, mandato, autorización o representación;
- verificar la causa y las evidencias;
- seleccionar la clave normalizada correcta;
- firmar la autorización o solicitud asistida;
- ejecutar la operación únicamente cuando su rol esté vigente y autorizado;
- preservar las evidencias y generar el acuse correspondiente.

La firma del agente acredita su intervención y ejecución, pero no sustituye el mandato, autorización o representación exigible a la persona solicitante.

### 4.3. Superior jerárquico, enlace institucional, recursos humanos o unidad competente

Podrán iniciar revocaciones relacionadas con baja, separación, cambio de dependencia, unidad administrativa, cargo o retiro formal de autorización.

Deberán aportar oficio, constancia, movimiento de personal, consulta a fuente oficial u otra evidencia verificable.

### 4.4. Autoridad de Certificación

Será responsable de:

- validar el cumplimiento del procedimiento;
- ejecutar o autorizar la revocación;
- registrar la fecha y hora efectiva;
- publicar el estado mediante OCSP y, cuando corresponda, CRL;
- generar y conservar el expediente y acuse;
- escalar incidentes y preservar evidencias;
- informar a la persona titular cuando resulte posible y jurídicamente procedente.

### 4.5. Autoridad judicial o administrativa

Las órdenes deberán ser identificables, verificables y emitidas por autoridad competente. La fecha de efectos señalada en la orden se conservará como metadato jurídico; no retrotraerá el estado técnico publicado mediante OCSP o CRL.

## 5. Modalidades de revocación

### 5.1. Revocación directa por la persona titular

Procederá cuando la persona titular:

1. ingrese al sistema autorizado;
2. identifique el certificado;
3. seleccione la causa normalizada;
4. describa brevemente los hechos;
5. firme la solicitud con el certificado vigente;
6. confirme el carácter definitivo e irreversible de la operación.

El sistema verificará la firma, la vigencia del certificado, su correspondencia con la persona titular y la integridad de la solicitud antes de ejecutar la revocación.

### 5.2. Revocación asistida por agente autorizado

Procederá cuando:

- la persona titular no disponga de la clave privada;
- desconozca la contraseña;
- exista pérdida, exposición o compromiso de la clave;
- intervenga un representante o tercero legitimado;
- medie orden de autoridad;
- la solicitud provenga de una dependencia, superior jerárquico, unidad competente o de la propia Autoridad de Certificación.

El simple olvido de contraseña, sin evidencia de pérdida, exposición o compromiso de la clave privada, se registrará bajo `01_Solicitud_del_titular`. No deberá clasificarse bajo la causa 06.

## 6. Recepción y apertura del expediente

Toda solicitud deberá recibir un folio único.

El expediente deberá asociarse, al menos, con:

- número de serie del certificado;
- identidad de la persona titular;
- causa principal y causas adicionales;
- persona o entidad que inicia la revocación;
- agente o proceso que interviene;
- evidencias y referencias documentales;
- estado del trámite;
- bitácora de acciones y decisiones.

No deberán incorporarse contraseñas, claves privadas ni datos personales innecesarios.

## 7. Identificación del certificado

La identificación se realizará mediante el número de serie y, cuando sea necesario, mediante CURP, RFC, nombre, correo electrónico, dependencia, unidad administrativa o atributo de representación.

Antes de continuar deberá verificarse que:

- el certificado existe;
- corresponde a la persona titular o sujeto afectado;
- no se encuentra ya revocado;
- su estado y cadena pueden consultarse;
- el número de serie coincide en la solicitud, expediente y operación.

Si el certificado ya se encuentra vencido, el expediente podrá cerrarse sin ejecutar una nueva revocación, salvo que exista una necesidad legal, probatoria, histórica o de investigación que requiera registrar formalmente la causa.

## 8. Selección y validación de la causa

La causa deberá registrarse con su clave y denominación normalizadas.

Cuando concurran varias causas:

- se registrará como principal la que describa con mayor precisión el motivo determinante;
- cada causa adicional se documentará con clave y denominación;
- las evidencias podrán compartirse cuando sustenten más de una causa;
- la causa 11 solo podrá utilizarse cuando ninguna de las causas 01 a 10 resulte aplicable y exista fundamento expreso.

La causa 06 se limitará a pérdida, exposición o compromiso de la clave privada o del medio que la contiene.

## 9. Validación de legitimidad y evidencias

### 9.1. Solicitud de la persona titular

La solicitud directa firmada con el certificado vigente acreditará la voluntad de la persona titular.

Cuando intervenga otra persona deberán validarse mandato, autorización expresa o acreditación de representación y registrarse su referencia documental.

### 9.2. Personas morales

Para disolución o liquidación podrán intervenir las personas liquidadoras legalmente facultadas.

Para escisión podrá intervenir cualquiera de las sociedades escindidas. Para fusión podrá intervenir la sociedad subsistente, además de las personas o autoridades legitimadas conforme al Anexo C.

### 9.3. Fallecimiento

Se requerirá acta o constancia oficial de defunción y legitimidad de la persona solicitante. Se registrará bajo `09_Cambio_de_circunstancias_del_sujeto`, conservando la descripción específica **Fallecimiento del titular**.

### 9.4. Orden judicial o administrativa

La orden deberá contener autoridad emisora, referencia, alcance, certificado o persona afectada y, cuando corresponda, fecha de efectos.

La autenticidad y competencia deberán validarse antes de la ejecución, salvo que la orden disponga atención inmediata y exista un mecanismo institucional autorizado para su verificación posterior.

## 10. Clasificación de prioridad

Se considerarán de atención urgente:

- pérdida, exposición o compromiso de clave privada;
- suplantación o documentación falsa;
- uso indebido activo;
- orden de autoridad con ejecución inmediata;
- compromiso de cuenta, dispositivo o sistema desde el cual pueda utilizarse la clave;
- afectación potencial a múltiples certificados, validadores o servicios.

Las revocaciones urgentes deberán ser atendidas por el canal operativo disponible con prioridad sobre trámites ordinarios y deberán vincularse, cuando corresponda, con el procedimiento de gestión de incidentes.

## 11. Autorización de la revocación

Antes de ejecutar, el sistema o agente deberá confirmar:

- identificación inequívoca del certificado;
- legitimidad de quien solicita o inicia;
- causa normalizada;
- evidencia mínima;
- autorizaciones necesarias;
- ausencia de errores materiales en número de serie o identidad;
- rol vigente de la persona ejecutora;
- disponibilidad de los servicios de publicación de estado.

Las causas 05, 07, 10 y 11 requerirán validación expresa de la Autoridad de Certificación o de la unidad competente designada, además de la intervención técnica del agente cuando corresponda.

## 12. Ejecución técnica

La revocación deberá ejecutarse como una operación única, autenticada y trazable.

El sistema deberá:

1. verificar nuevamente el estado del certificado;
2. registrar la causa principal y las adicionales;
3. registrar a la persona o proceso ejecutor;
4. registrar la fecha y hora efectiva de revocación;
5. cambiar el estado del certificado de forma definitiva;
6. publicar o poner a disposición el nuevo estado mediante OCSP;
7. incorporar la revocación en la CRL correspondiente cuando aplique;
8. registrar el resultado de cada publicación;
9. impedir reactivación, modificación o reversión ordinaria.

La fecha y hora efectiva será la registrada por la Autoridad de Certificación al ejecutar, registrar y publicar el estado. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica.

## 13. Verificación posterior

Después de ejecutar deberá comprobarse:

- respuesta OCSP con estado revocado;
- correspondencia del número de serie;
- causa y fecha registradas;
- incorporación en CRL cuando corresponda;
- integridad de bitácoras;
- generación del acuse;
- cierre o escalamiento de incidentes relacionados.

Si la publicación OCSP o CRL falla, la revocación no deberá revertirse. El incidente deberá escalarse y la publicación deberá reintentarse mediante los mecanismos de continuidad autorizados.

## 14. Acuse de revocación

El acuse solo se generará cuando la revocación haya sido ejecutada satisfactoriamente.

Deberá incluir, al menos:

- folio;
- identificación de la persona titular;
- número de serie;
- clave y denominación de la causa principal;
- fecha y hora efectiva;
- persona o proceso ejecutor;
- resultado de publicación del estado;
- firma o sello electrónico del acuse y su referencia.

Cuando exista una orden con fecha de efectos distinta, podrá incluirse como metadato jurídico claramente diferenciado de la fecha efectiva técnica.

## 15. Notificación

La Autoridad de Certificación notificará la revocación a la persona titular por el canal registrado, cuando sea posible y no exista impedimento legal, judicial, de seguridad o de investigación.

Para personas servidoras públicas podrá notificarse también al superior jerárquico, enlace institucional o unidad competente.

La notificación no condiciona la eficacia de la revocación.

## 16. Firmas anteriores y posteriores

La revocación no invalida automáticamente las firmas realizadas antes de la fecha y hora efectiva. Su validez deberá evaluarse mediante sello de tiempo, integridad, cadena de confianza, estado histórico y normatividad aplicable.

Las firmas realizadas después de la fecha y hora efectiva no deberán considerarse válidas con base en el certificado revocado.

Las órdenes de autoridad con una fecha de efectos jurídica anterior deberán analizarse de forma separada y no modificarán retroactivamente el estado técnico publicado.

## 17. Conservación del expediente

El expediente deberá conservarse conforme a la CP, la CPS, las temporalidades documentales y la normatividad aplicable.

Deberán preservarse:

- solicitud y autorizaciones;
- evidencias;
- bitácoras;
- decisión y validaciones;
- resultados OCSP y CRL;
- acuse firmado o sellado;
- comunicaciones y notificaciones;
- referencias de incidentes o actos de autoridad.

## 18. Excepciones e incidencias

No deberá ejecutarse una revocación cuando:

- no pueda identificarse inequívocamente el certificado;
- la persona solicitante carezca de legitimidad o representación acreditada;
- no exista evidencia mínima;
- se pretenda utilizar la causa 11 sin fundamento;
- exista inconsistencia material no resuelta;
- el rol de ejecución no esté autorizado.

La negativa o suspensión del trámite deberá documentarse. No se generará acuse de revocación si la operación no fue ejecutada.

## 19. Métricas y revisión

La Autoridad de Certificación deberá revisar periódicamente, al menos:

- número de revocaciones por causa;
- tiempos de atención ordinaria y urgente;
- solicitudes rechazadas o incompletas;
- fallas de publicación OCSP o CRL;
- uso de la causa residual 11;
- revocaciones por compromiso o fraude;
- calidad e integridad de expedientes y acuses.

Los hallazgos deberán generar acciones correctivas, preventivas o de mejora cuando corresponda.

## 20. Control de cambios

Toda modificación a este procedimiento deberá evaluar su impacto en:

- Anexo C;
- Anexo O;
- formatos y flujos de CERTAC;
- CPS;
- OCSP y CRL;
- bitácoras, acuses e integraciones;
- procedimientos de incidentes y continuidad.

Los cambios sustantivos requerirán aprobación de la Coordinación de Política Digital y del Consejo Técnico, así como actualización de versión y fecha de entrada en vigor.
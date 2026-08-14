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

La revocación será definitiva e irreversible. No existe suspensión temporal, reactivación, modificación ni reemisión del certificado revocado. Cuando la persona interesada continúe requiriendo un certificado, deberá iniciar un trámite independiente de nueva emisión. Un certificado revocado no será elegible para renovación.

## 2. Alcance

Este procedimiento será aplicable a:

- certificados de firma electrónica avanzada de personas físicas ciudadanas;
- certificados de personas servidoras públicas;
- certificados de personas físicas en calidad de representantes legales;
- certificados de servicios OCSP, TSA, firma de CRL o infraestructura, conforme al procedimiento específico previsto en la sección 4.6;
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

### 4.6. Certificados de servicios e infraestructura

Para certificados OCSP, TSA, de firma de CRL o de infraestructura, el expediente deberá estructurarse conforme al siguiente contrato, distinto del aplicable a certificados de personas físicas titulares:

- **Identificador del activo o servicio:** identificación del componente criptográfico, respondedor, firmante de tiempo, firmante de CRL u otro activo de infraestructura vinculado al certificado.
- **Propietario institucional:** dependencia, unidad administrativa o entidad responsable del activo o servicio.
- **Unidad responsable de operación:** área encargada de operar, monitorear y mantener el servicio.
- **Solicitante autorizado:** persona o proceso con facultades vigentes para solicitar la revocación, que podrá ser el propietario institucional, la unidad responsable, la Autoridad de Certificación, el área de seguridad o una autoridad competente.
- **Evidencia y autorización:** inventario, orden de cambio, reporte de incidente, compromiso de clave, retiro del servicio, sustitución de componente, resolución de autoridad u otra evidencia técnica o administrativa aplicable, además de la autorización de ejecución emitida por la Autoridad de Certificación o por la unidad formalmente designada.
- **Persona ejecutora:** agente o proceso autorizado que ejecutó la revocación.

Los formularios de firma electrónica avanzada diseñados para personas titulares naturales quedan fuera del alcance de estos certificados. El expediente deberá vincular inequívocamente el certificado, su clave pública, el servicio, el activo, el ambiente y la autoridad emisora.

Antes de ejecutar la revocación deberá verificarse la validez de cada uno de los elementos descritos.

La revocación directa mediante firma con el propio certificado no será requisito para estos certificados. La solicitud y autorización deberán realizarse mediante un canal institucional autenticado y quedar vinculadas al expediente, con identificación de quien solicita, quien autoriza y quien ejecuta.

Antes de revocar un certificado OCSP, TSA, de firma de CRL o de infraestructura deberá ejecutarse un plan de sustitución o continuidad que incluya, según corresponda:

1. generar o habilitar una clave y un certificado de reemplazo con perfil autorizado;
2. distribuir la nueva cadena y configuración a los componentes dependientes;
3. comprobar firma, validación, publicación y monitoreo con el certificado de reemplazo;
4. realizar el cambio controlado del servicio y confirmar que no existan dependencias activas del certificado saliente;
5. preservar inventarios, evidencias de transición, responsables y criterios de reversión;
6. revocar el certificado saliente únicamente después de confirmar la continuidad del servicio.

Cuando exista compromiso confirmado o riesgo inminente que impida mantener temporalmente el certificado saliente, la Autoridad de Certificación podrá ordenar su aislamiento y revocación inmediata. En ese caso deberá activarse previamente o de forma simultánea un respondedor, firmante o mecanismo alterno autorizado, aplicar el procedimiento de continuidad operativa y documentar cualquier periodo de degradación. No deberá continuarse la publicación con una clave comprometida.

## 5. Modalidades de revocación

### 5.1. Revocación directa por la persona titular

Procederá cuando la persona titular:

1. ingrese al sistema autorizado;
2. identifique el certificado;
3. seleccione la causa normalizada;
4. describa brevemente los hechos;
5. adjunte o referencie la evidencia mínima exigible por la causa seleccionada cuando esta no sea `01_Solicitud_del_titular`;
6. firme la solicitud con el certificado vigente;
7. confirme el carácter definitivo e irreversible de la operación.

El sistema verificará la firma, la vigencia del certificado, su correspondencia con la persona titular, la integridad de la solicitud y la evidencia mínima exigible por la causa antes de ejecutar la revocación. Cuando la causa requiera evidencia corporativa, registral, judicial o administrativa que la persona titular no pueda aportar por este canal, el trámite deberá continuar mediante revocación asistida.

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

La causa 06 se aplicará a la pérdida de la clave privada o del medio que la contiene, exposición, acceso no autorizado, copia, sospecha razonable de compromiso o cualquier circunstancia que afecte su confidencialidad. El simple olvido de la contraseña, sin evidencia de pérdida, exposición, acceso no autorizado, copia o sospecha razonable de compromiso, se tramitará bajo `01_Solicitud_del_titular` mediante revocación asistida.

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

La orden deberá contener autoridad emisora, referencia, alcance, certificado o persona afectada y, cuando corresponda, fecha de efectos. Deberá recibirse por un canal institucional autenticado y comprobarse la identidad del emisor, la integridad del documento y la competencia de la autoridad antes de ejecutar, incluso cuando se solicite atención inmediata.

Las comprobaciones esenciales no podrán diferirse: canal institucional autenticado, identidad del emisor, integridad del documento, competencia de la autoridad e identificación inequívoca del certificado o sujeto afectado. Únicamente podrán aplazarse comprobaciones documentales complementarias, como cotejos secundarios, incorporación de copias certificadas o validaciones de forma no determinantes, cuando exista autorización explícita de emergencia emitida por la unidad jurídica o la Autoridad de Certificación y se establezca en el expediente un plazo no mayor a veinticuatro horas para completarlas. Si la verificación posterior de esos elementos complementarios falla, se preservarán las evidencias, se notificará de inmediato a la unidad jurídica y al Consejo Técnico, se abrirá un incidente y se determinarán las medidas jurídicas y operativas procedentes, sin ocultar ni alterar el registro de la actuación ejecutada.

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
- disponibilidad del mecanismo durable de registro local y de la cola transaccional de publicación, o del canal alterno de continuidad autorizado que la sustituya.

Toda revocación asistida requerirá la firma electrónica avanzada de una persona con rol vigente de agente autorizado, incluida aquella iniciada por la propia Autoridad de Certificación o por una unidad competente. Las causas 05, 07, 10 y 11 requerirán además validación expresa de la Autoridad de Certificación o de la unidad competente designada.

Si la cola transaccional u outbox no está disponible y la revocación es urgente, antes de iniciar la transacción deberá activarse un canal alterno de continuidad autorizado. Este canal deberá crear una reserva durable no publicable con estado pendiente de confirmación local, registrando su identificador idempotente, fecha y hora de reserva, responsable que lo autorizó y evidencia de activación. La fecha y hora efectiva no se asignará en la reserva: se asignará y persistirá únicamente en la transacción atómica que confirme la revocación local. Tras confirmar exitosamente la transacción, la reserva se promoverá a publicación pendiente y se vinculará con la fecha y hora efectiva definida al commit; ese registro sustituirá temporalmente al evento de outbox. La propagación externa por el canal alterno deberá iniciarse únicamente después de promover la reserva a publicación pendiente. Si el commit falla o no ocurre, la reconciliación deberá excluir la reserva. La indisponibilidad del outbox deberá documentarse como incidente y conciliarse posteriormente con el outbox sin alterar la fecha y hora efectiva ni duplicar la publicación.

## 12. Ejecución técnica

La decisión de revocación y su registro local deberán ejecutarse como una operación autenticada, trazable y durable. Antes de construir cualquier respuesta OCSP o entrada de CRL, el sistema asignará y persistirá una fecha y hora efectiva única de revocación. Ese mismo valor se utilizará sin modificación en la publicación técnica y en todos los reintentos posteriores.

El sistema deberá:

1. verificar nuevamente el estado del certificado;
2. registrar la causa principal y las adicionales;
3. registrar a la persona o proceso ejecutor;
4. dentro de una misma transacción atómica, verificar mediante bloqueo o actualización compare-and-set por emisor y número de serie que el certificado no esté ya revocado; si ya está revocado, reutilizar la fecha efectiva y el evento de publicación existentes sin crear una nueva publicación, devolver el acuse existente o registrar idempotentemente su generación pendiente si este falta; si no está revocado, asignar y persistir la fecha y hora efectiva única, cambiar el estado local a revocado y registrar los eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL, o promover la reserva durable alterna a publicación pendiente cuando el outbox esté indisponible; la transacción solo deberá confirmarse si las tres operaciones y el vínculo con el evento de publicación quedan registrados satisfactoriamente, o si se comprueba que el certificado ya estaba revocado y se reutilizan sus eventos existentes;
5. después de confirmar la transacción, construir e intentar la publicación o puesta a disposición del nuevo estado mediante OCSP utilizando esa misma fecha y hora;
6. incorporar la revocación en la CRL correspondiente cuando aplique, utilizando esa misma fecha y hora;
7. registrar el resultado de cada intento de publicación;
8. impedir reactivación, modificación o reversión ordinaria.

La fecha y hora efectiva será la asignada y persistida en la misma transacción atómica que confirme durablemente la revocación local y registre el evento de publicación pendiente. Una reserva durable alterna previa conservará exclusivamente su propia fecha y hora de reserva y se vinculará después con la fecha efectiva asignada al commit. Si la transacción no puede completar esos tres registros, no deberá confirmarse parcialmente. La publicación OCSP o CRL deberá reproducir ese mismo valor; los reintentos no podrán sustituirlo por una fecha posterior. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica.

## 13. Verificación posterior

Después de ejecutar deberá comprobarse:

- correspondencia del número de serie;
- causa y fecha registradas;
- integridad de bitácoras;
- cierre o escalamiento de incidentes relacionados.

Tras confirmar la publicación correspondiente, deberá comprobarse además:

- respuesta OCSP con estado revocado;
- incorporación en CRL cuando corresponda;
- generación del acuse definitivo.

Mientras el estado sea **publicación pendiente**, la comprobación de la respuesta OCSP revocada y la incorporación en la CRL quedarán explícitamente diferidas, y no se emitirá el acuse definitivo.

Si la publicación OCSP o CRL falla, la revocación local no deberá revertirse. El evento conservará el estado **publicación pendiente** en la cola transaccional u outbox o, mientras se reconcilia, en el registro durable alterno autorizado de la sección 11; mantendrá la fecha y hora efectiva ya persistida. Deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado. La reconciliación no podrá descartar el evento alterno ni crear una segunda publicación para el mismo identificador.

Ante cualquier falla de publicación, los servicios institucionales deberán rechazar inmediatamente los usos nuevos o posteriores a la fecha y hora efectiva con base en el estado local durable, sin esperar a que OCSP o CRL reflejen la actualización. La validación de firmas o documentos generados antes de esa fecha deberá conservar la ruta histórica de la sección 16, evaluando sello de tiempo, integridad, cadena de confianza y estado histórico. Para toda revocación clasificada como urgente conforme a la sección 10, la primera falla activará además el mecanismo alterno autorizado de continuidad y la actualización externa por el canal alterno disponible, sin esperar a que se agote el límite ordinario de reintentos. Esta regla comprende, entre otros, compromiso o riesgo de la clave privada, suplantación o documentación falsa, uso indebido activo, órdenes de ejecución inmediata, compromiso de cuentas, dispositivos o sistemas y afectaciones potenciales a múltiples certificados, validadores o servicios. Para revocaciones no urgentes, el rechazo institucional será igualmente inmediato para usos nuevos o posteriores, mientras que los mecanismos alternos de propagación externa se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación.

## 14. Acuse de revocación

El acuse de revocación se generará cuando la revocación local haya quedado confirmada durablemente y exista fecha y hora efectiva persistida. Si OCSP o CRL aún no reflejan el nuevo estado, el acuse deberá indicar **publicación pendiente**, conservar la fecha y hora efectiva ya asignada e identificar los eventos de outbox relacionados o, mientras se reconcilia la continuidad, el identificador del registro durable alterno y su referencia idempotente; deberá actualizarse o complementarse cuando la publicación quede confirmada.

Deberá incluir, al menos:

- folio;
- identificación de la persona titular, cuando corresponda; para certificados de infraestructura deberá incluirse el identificador del activo o servicio, propietario institucional, unidad responsable y solicitante autorizado conforme a la sección 4.6;
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

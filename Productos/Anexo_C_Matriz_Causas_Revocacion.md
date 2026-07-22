# Anexo C. Matriz de causas de revocación

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión:** 1.2  
**Estado:** Proyecto  
**Autoridad responsable:** Coordinación de Política Digital  
**Órgano de aprobación:** Coordinación de Política Digital y Consejo Técnico  

---

## 1. Objeto

El presente anexo establece el catálogo normalizado de causas de revocación aplicable a los certificados emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua, así como los sujetos legitimados para solicitarla, las evidencias mínimas, el tratamiento operativo y los efectos asociados.

La revocación será definitiva e irreversible. No existe suspensión temporal ni reactivación del certificado revocado.

## 2. Reglas generales

1. Toda revocación deberá vincularse con una causa del catálogo contenido en este anexo.
2. La causa seleccionada deberá corresponder con los hechos y evidencias disponibles.
3. Cuando concurran varias causas, se registrará como principal la que describa con mayor precisión el motivo determinante. Cada causa adicional deberá documentarse en el expediente mediante su clave y denominación normalizadas.
4. La clave `11_Otra_causal_definida_en_el_certificado` solo se utilizará cuando ninguna de las causas 01 a 10 describa adecuadamente el supuesto y exista fundamento documentado en la CP, la CPS, el perfil del certificado, los términos y condiciones, un convenio aplicable o una determinación de autoridad competente.
5. La fecha y hora de ejecución será aquella en que la Autoridad de Certificación complete satisfactoriamente la operación y publique el estado correspondiente. La fecha y hora efectiva aplicable coincidirá ordinariamente con la ejecución. En la causa `02_Orden_judicial_o_administrativa`, la orden podrá señalar una fecha de efectos anterior; en ese caso se registrarán por separado la fecha y hora ordenadas y la fecha y hora de ejecución, sin alterar ni retrotraer la publicación técnica en OCSP o CRL. Los actos y firmas anteriores a la ejecución se evaluarán conforme al alcance de la orden, la evidencia temporal y la normatividad aplicable.
6. La revocación deberá publicarse mediante OCSP y, cuando corresponda, CRL.
7. La revocación de un certificado no invalida por sí misma las firmas generadas antes de la fecha y hora efectiva de revocación; su validez deberá evaluarse conforme a la integridad del documento, sello de tiempo, cadena de confianza, estado histórico del certificado y, cuando corresponda, los efectos establecidos por una orden de autoridad.
8. Cuando CERTAC o un formato histórico presente la opción específica **Fallecimiento del titular**, esta deberá registrarse operativamente bajo la causa canónica `09_Cambio_de_circunstancias_del_sujeto`, conservando en el expediente la etiqueta específica y el acta o constancia oficial correspondiente.

## 3. Matriz de causas

| Clave | Denominación normalizada | Supuesto de aplicación | Solicitante o iniciador autorizado | Evidencia mínima | Tratamiento operativo |
|---|---|---|---|---|---|
| `01_Solicitud_del_titular` | Solicitud de la persona titular | La persona titular solicita voluntariamente la revocación de su certificado, sin necesidad de acreditar compromiso de clave u otra causa adicional. | Persona titular mediante CERTAC; representante o tercero autorizado; agente autorizado cuando la persona titular no pueda firmar la solicitud. | Solicitud firmada por la persona titular con certificado vigente o, cuando intervenga otra persona, mandato, autorización expresa de la persona titular o documento que acredite la representación, además de la identificación y firma del agente ejecutor. La referencia de la autorización, mandato o representación deberá registrarse en el expediente. | Revocación inmediata una vez validadas la legitimidad de la solicitud y, cuando corresponda, la autorización o representación invocada. |
| `02_Orden_judicial_o_administrativa` | Orden judicial o administrativa | Existe mandamiento emitido por autoridad competente que ordena o requiere la revocación. | Autoridad competente; unidad jurídica o administrativa facultada; agente autorizado que ejecute la orden. | Oficio, resolución, mandamiento o acto de autoridad identificable y verificable. | Ejecución prioritaria conforme al alcance y fecha de efectos señalados en la orden. Se registrarán separadamente la fecha de efectos ordenada y la fecha de ejecución técnica. |
| `03_Disolución_de_persona_moral` | Disolución de persona moral | La persona moral representada ha sido disuelta, liquidada o ha dejado de existir jurídicamente, afectando el atributo de representación incorporado o vinculado al certificado. | Persona representante; persona liquidadora; autoridad competente; dependencia que acredite el hecho; agente autorizado. | Documento registral, acta, resolución o constancia oficial de disolución o liquidación. | Revocación del certificado de la persona física en su calidad de representante legal. |
| `04_Fusión_o_escisión` | Fusión o escisión de persona moral | La persona moral se fusiona, escinde o modifica de forma que cambian la identidad, continuidad o facultades de representación asociadas al certificado. | Persona representante; cualquiera de las sociedades escindidas; sociedad subsistente en caso de fusión; autoridad competente; unidad jurídica; agente autorizado. | Instrumento corporativo, inscripción registral, resolución o constancia oficial. | Revocación y, cuando proceda, nueva solicitud con la personalidad y facultades vigentes. |
| `05_Certificado_no_cumple_requisitos_legales` | Incumplimiento de requisitos legales o normativos | Se determina que el certificado, su emisión o sus datos no cumplen requisitos legales, normativos, de la CP, la CPS o del perfil técnico aplicable. | Autoridad de Certificación; auditoría; autoridad competente; unidad jurídica o de cumplimiento. | Dictamen, hallazgo, resolución, expediente de emisión o evidencia técnica documentada. | Revocación y análisis de impacto sobre certificados, perfiles o procesos relacionados. |
| `06_Riesgo_confidencialidad_datos_de_creación_de_firma` | Pérdida, exposición o compromiso de la clave privada | Existe pérdida de la clave privada o del medio que la contiene, exposición, acceso no autorizado, copia, sospecha razonable de compromiso o cualquier circunstancia que afecte su confidencialidad. El simple olvido de la contraseña, sin evidencia de pérdida, exposición o compromiso, no corresponde a esta causa y deberá tramitarse como `01_Solicitud_del_titular` mediante revocación asistida. | Persona titular; superior jerárquico; área de seguridad; Autoridad de Certificación; agente autorizado. | Declaración de la persona titular, reporte de incidente, evidencia técnica o análisis de riesgo que sustente la pérdida, exposición o compromiso. | Revocación urgente; contención del incidente y nueva emisión solo mediante trámite independiente. |
| `07_Documentación_de_identidad_falsa` | Documentación o identidad falsa | Se detecta falsedad, alteración, suplantación o inconsistencia material en la documentación o evidencias utilizadas para identificar a la persona titular. | Autoridad de Certificación; agente registrador; servicio de verificación; autoridad competente; auditoría. | Evidencias de verificación, dictamen documental, reporte de fraude o resolución de autoridad. | Revocación inmediata, preservación de evidencias y escalamiento al proceso de incidentes o autoridad competente. |
| `08_Término_de_cargo_de_servicio_público` | Terminación, modificación del cargo o retiro de autorización | La persona titular causa baja, se separa del cargo, cambia de dependencia, unidad administrativa, desempeña un cargo distinto al autorizado para el certificado vigente o el superior jerárquico o la unidad competente retira expresamente la autorización para su uso. | Superior jerárquico; enlace institucional; recursos humanos; unidad administrativa competente; Autoridad de Certificación. | Aviso institucional, movimiento de personal, oficio, constancia, retiro formal de autorización o consulta a fuente oficial. | Revocación definitiva. Si continúa requiriendo certificado, deberá presentar nueva solicitud con autorización actualizada. |
| `09_Cambio_de_circunstancias_del_sujeto` | Cambio de circunstancias o fallecimiento de la persona titular | Cambian datos esenciales, identidad, representación, facultades, situación jurídica o cualquier circunstancia relevante que haga inexacto o improcedente el certificado vigente; incluye el fallecimiento de la persona titular. | Persona titular; superior jerárquico; persona moral; familiar o tercero legitimado; autoridad competente; Autoridad de Certificación. | Documento que acredite el cambio, declaración, actualización registral, evidencia oficial o, en caso de fallecimiento, acta o constancia oficial de defunción. | Revocación definitiva. Cuando proceda por un cambio distinto del fallecimiento, podrá tramitarse una nueva emisión; no existe reemisión ni modificación del certificado vigente. |
| `10_Uso_indebido_del_certificado` | Uso indebido del certificado | El certificado se utiliza fuera de su alcance, para suplantar identidad, compartir la clave, firmar información falsa, eludir controles o realizar actos no autorizados. | Autoridad de Certificación; dependencia usuaria; área de seguridad; auditoría; tercero afectado; autoridad competente. | Bitácoras, documentos firmados, reporte de incidente, dictamen, denuncia o evidencia técnica. | Revocación, preservación de evidencias y aplicación de los procedimientos administrativos, legales o de seguridad correspondientes. |
| `11_Otra_causal_definida_en_el_certificado` | Otra causa formalmente sustentada | Existe una causa no comprendida en las anteriores, prevista en el certificado, la CP, la CPS, los términos y condiciones, un convenio aplicable o una determinación de autoridad competente. | Sujeto facultado conforme al fundamento invocado. | Fundamento expreso y evidencia suficiente que justifique el uso de esta clave residual. | Requiere motivación documentada y validación por la Autoridad de Certificación antes de ejecutar la revocación. |

## 4. Correspondencia con modalidades de CERTAC

### 4.1. Revocación directa por la persona titular

Podrá utilizarse cuando la persona titular conserve el certificado vigente, la clave privada y la contraseña necesaria para firmar su solicitud. La causa más frecuente será `01_Solicitud_del_titular`, sin perjuicio de seleccionar otra causa cuando corresponda a los hechos.

### 4.2. Revocación asistida por agente autorizado

Se utilizará cuando la persona titular no disponga de la clave privada, desconozca su contraseña, exista compromiso de clave, medie orden de autoridad o la revocación sea iniciada por una dependencia, superior jerárquico, unidad competente o la propia Autoridad de Certificación.

El olvido de la contraseña, por sí solo y sin evidencia de pérdida, exposición o compromiso de la clave privada, se registrará bajo `01_Solicitud_del_titular`; no deberá clasificarse bajo la causa 06.

El agente deberá verificar identidad, legitimidad, causal, autorización o representación cuando corresponda, y evidencias antes de firmar y ejecutar la revocación.

## 5. Reglas de selección y registro

El expediente de revocación deberá contener, al menos:

- folio del trámite;
- número de serie del certificado;
- clave y denominación de la causa principal;
- clave y denominación normalizadas de cada causa adicional, cuando existan;
- descripción breve de los hechos;
- sujeto que inició la revocación;
- mandato, autorización o acreditación de representación y su referencia, cuando corresponda;
- agente o proceso autorizado que la ejecutó;
- evidencia o referencia documental;
- fecha y hora de ejecución;
- fecha y hora efectiva aplicable y, para la causa 02, fecha de efectos ordenada cuando sea distinta;
- resultado de publicación en OCSP y, cuando corresponda, CRL;
- firma o sello electrónico del acuse.

No deberán registrarse contraseñas, claves privadas ni datos personales innecesarios dentro del expediente.

## 6. Casos que requieren atención prioritaria

Se tratarán como urgentes las revocaciones relacionadas con:

- compromiso o pérdida de clave privada;
- suplantación o documentación falsa;
- uso indebido activo;
- orden de autoridad con ejecución inmediata;
- compromiso de una cuenta, dispositivo o sistema desde el cual pueda utilizarse la clave;
- riesgo de emisión o validación incorrecta a escala múltiple.

La CPS y el procedimiento de gestión de incidentes definirán los tiempos operativos, responsables, escalamiento y mecanismos alternos aplicables.

## 7. Control de cambios

Toda modificación al catálogo, claves, denominaciones o reglas de aplicación deberá:

1. mantener compatibilidad con los registros históricos;
2. evaluar su impacto en CERTAC, OCSP, CRL, acuses, auditoría y sistemas integrados;
3. ser aprobada por la Coordinación de Política Digital y el Consejo Técnico;
4. actualizar la versión de este anexo y, cuando corresponda, la CP y la CPS.

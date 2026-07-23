# Anexo O. Formato de Solicitud de Revocación

**Autoridad de Certificación de Gobierno del Estado de Chihuahua**  
**Formato para Solicitud de Revocación de Firma Electrónica Avanzada**

**Fecha:** {{FECHA}}  
**Folio:** {{FOLIO}}

---

## 1. Datos de la persona titular del certificado

- **Nombre completo:** _________________________________________________
- **CURP:** _________________________________________________
- **RFC:** _________________________________________________
- **Número de serie del certificado:** ________________________________

## 2. Causa de revocación

Seleccione una sola causa principal del catálogo normalizado del Anexo C. Cuando concurran varias causas, registre como principal la que describa con mayor precisión el motivo determinante y documente las adicionales mediante su clave y denominación normalizadas.

- [ ] `01_Solicitud_del_titular` — Solicitud de la persona titular.
- [ ] `02_Orden_judicial_o_administrativa` — Orden judicial o administrativa.
- [ ] `03_Disolución_de_persona_moral` — Disolución, liquidación o extinción de la persona moral representada.
- [ ] `04_Fusión_o_escisión` — Fusión o escisión de la persona moral.
- [ ] `05_Certificado_no_cumple_requisitos_legales` — Incumplimiento de requisitos legales, normativos o técnicos.
- [ ] `06_Riesgo_confidencialidad_datos_de_creación_de_firma` — Pérdida de la clave privada o del medio que la contiene, exposición, acceso no autorizado, copia o compromiso. El olvido de contraseña, sin evidencia de pérdida, exposición o compromiso, deberá registrarse como `01_Solicitud_del_titular` mediante revocación asistida.
- [ ] `07_Documentación_de_identidad_falsa` — Documentación falsa, alterada o suplantación de identidad.
- [ ] `08_Término_de_cargo_de_servicio_público` — Baja, separación, cambio de dependencia, unidad administrativa o cargo, o retiro formal de autorización.
- [ ] `09_Cambio_de_circunstancias_del_sujeto` — Cambio de datos, representación, facultades, situación jurídica, incapacidad o fallecimiento de la persona titular.
- [ ] `10_Uso_indebido_del_certificado` — Uso fuera de alcance, fraudulento o no autorizado.
- [ ] `11_Otra_causal_definida_en_el_certificado` — Otra causa formalmente sustentada.

**Descripción de los hechos:**  
________________________________________________________________________  
________________________________________________________________________

**Causas adicionales relacionadas, cuando existan:**

1. **Clave normalizada:** ____________________  **Denominación:** ______________________________
2. **Clave normalizada:** ____________________  **Denominación:** ______________________________
3. **Clave normalizada:** ____________________  **Denominación:** ______________________________

**Documento o evidencia de soporte:**  
________________________________________________________________________

Para fallecimiento de la persona titular deberá adjuntarse acta o constancia oficial de defunción. La causa se registrará bajo la clave `09_Cambio_de_circunstancias_del_sujeto` con la descripción específica **Fallecimiento del titular**.

La clave `11_Otra_causal_definida_en_el_certificado` requiere fundamento expreso y evidencia suficiente; no deberá utilizarse cuando alguna de las causas 01 a 10 resulte aplicable.

## 3. Declaración

Solicito o autorizo, según la calidad con la que comparezco, la revocación definitiva e irreversible del certificado señalado. Reconozco que no existe suspensión temporal, reactivación ni reemisión del certificado revocado.

**Nombre de la persona solicitante o agente autorizado:**  
________________________________________________________________________

**Calidad con la que comparece:**

- [ ] Persona titular.
- [ ] Agente autorizado.
- [ ] Superior jerárquico, enlace institucional o unidad competente.
- [ ] Persona representante, liquidadora o sociedad legitimada.
- [ ] Autoridad judicial o administrativa.
- [ ] Familiar o tercero legalmente legitimado.
- [ ] Otra: _________________________________________________

**Mandato, autorización o representación invocada, cuando corresponda:**  
________________________________________________________________________

**Referencia documental de la autorización o representación:**  
________________________________________________________________________

**Firma:** _________________________________________________

---

## 4. Registro de ejecución

- **Clave normalizada registrada:** {{CLAVE_CAUSAL}}
- **Denominación registrada:** {{DENOMINACION_CAUSAL}}
- **Fecha y hora efectiva de revocación:** {{FECHA_HORA_EFECTIVA}}
- **Fecha de efectos ordenada como metadato jurídico, para causa 02 cuando sea distinta:** {{FECHA_HORA_ORDENADA}}
- **Persona o proceso autorizado que ejecutó:** {{EJECUTOR}}
- **Resultado de publicación OCSP:** {{RESULTADO_OCSP}}
- **Resultado de publicación CRL, cuando corresponda:** {{RESULTADO_CRL}}
- **Firma o sello electrónico del acuse:** {{FIRMA_O_SELLO_ACUSE}}
- **Referencia, identificador o fecha de la firma o sello:** {{REFERENCIA_FIRMA_O_SELLO}}

La fecha y hora efectiva será la registrada por la Autoridad de Certificación al completar la ejecución y publicar el estado técnico. Una fecha anterior indicada por una orden judicial o administrativa se conservará únicamente como metadato jurídico y no retrotraerá el estado publicado en OCSP o CRL.

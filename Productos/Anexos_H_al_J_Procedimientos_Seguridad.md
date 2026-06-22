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

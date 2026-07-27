from pathlib import Path

path = Path("Productos/Anexo_G_Procedimiento_Revocacion.md")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        "- certificados de servicios OCSP, TSA, CRL o infraestructura, con las adecuaciones técnicas y autorizaciones que correspondan;",
        "- certificados de servicios OCSP, TSA, firma de CRL o infraestructura, conforme al procedimiento específico previsto en la sección 4.6;",
    ),
    (
        "### 4.5. Autoridad judicial o administrativa\n\nLas órdenes deberán ser identificables, verificables y emitidas por autoridad competente. La fecha de efectos señalada en la orden se conservará como metadato jurídico; no retrotraerá el estado técnico publicado mediante OCSP o CRL.",
        "### 4.5. Autoridad judicial o administrativa\n\nLas órdenes deberán ser identificables, verificables y emitidas por autoridad competente. La fecha de efectos señalada en la orden se conservará como metadato jurídico; no retrotraerá el estado técnico publicado mediante OCSP o CRL.\n\n### 4.6. Certificados de servicios e infraestructura\n\nPara certificados OCSP, TSA, de firma de CRL o de infraestructura, la persona titular será sustituida operativamente por el activo o servicio criptográfico identificado y por su responsable institucional.\n\nAntes de ejecutar la revocación deberá verificarse:\n\n- el propietario institucional del activo o servicio y la unidad responsable de su operación;\n- la identidad y vigencia de facultades de la persona solicitante autorizada, que podrá ser el propietario del activo, la unidad responsable, la Autoridad de Certificación, el área de seguridad o una autoridad competente;\n- la vinculación inequívoca entre el certificado, su clave pública, el servicio, el activo, el ambiente y la autoridad emisora;\n- la evidencia técnica o administrativa aplicable, como inventario, orden de cambio, reporte de incidente, compromiso de clave, retiro del servicio, sustitución de componente o resolución de autoridad;\n- la autorización de ejecución emitida por la Autoridad de Certificación o por la unidad formalmente designada.\n\nLa revocación directa mediante firma con el propio certificado no será requisito para estos certificados. La solicitud y autorización deberán realizarse mediante un canal institucional autenticado y quedar vinculadas al expediente, con identificación de quien solicita, quien autoriza y quien ejecuta.",
    ),
    (
        "La causa 06 se limitará a pérdida, exposición o compromiso de la clave privada o del medio que la contiene.",
        "La causa 06 se aplicará a la pérdida de la clave privada o del medio que la contiene, exposición, acceso no autorizado, copia, sospecha razonable de compromiso o cualquier circunstancia que afecte su confidencialidad. El simple olvido de la contraseña, sin evidencia de pérdida, exposición, acceso no autorizado, copia o sospecha razonable de compromiso, se tramitará bajo `01_Solicitud_del_titular` mediante revocación asistida.",
    ),
    (
        "La orden deberá contener autoridad emisora, referencia, alcance, certificado o persona afectada y, cuando corresponda, fecha de efectos.\n\nLa autenticidad y competencia deberán validarse antes de la ejecución, salvo que la orden disponga atención inmediata y exista un mecanismo institucional autorizado para su verificación posterior.",
        "La orden deberá contener autoridad emisora, referencia, alcance, certificado o persona afectada y, cuando corresponda, fecha de efectos. Deberá recibirse por un canal institucional autenticado y comprobarse la identidad del emisor, la integridad del documento y la competencia de la autoridad antes de ejecutar, incluso cuando se solicite atención inmediata.\n\nÚnicamente podrá diferirse la verificación completa cuando exista una autorización explícita de emergencia emitida por la unidad jurídica o la Autoridad de Certificación, la orden haya sido recibida mediante un mecanismo institucional autenticado y se establezca en el expediente un plazo de verificación posterior no mayor a veinticuatro horas. Si la verificación posterior falla, se preservarán todas las evidencias, se notificará de inmediato a la unidad jurídica y al Consejo Técnico, se abrirá un incidente y se determinarán las medidas jurídicas y operativas procedentes; la revocación técnicamente ejecutada no se revertirá ni se ocultará.",
    ),
    (
        "- rol vigente de la persona ejecutora;\n- disponibilidad de los servicios de publicación de estado.",
        "- rol vigente de la persona ejecutora;\n- disponibilidad del mecanismo durable de registro local y de la cola transaccional de publicación.",
    ),
    (
        "La revocación deberá ejecutarse como una operación única, autenticada y trazable.",
        "La revocación deberá ejecutarse como una operación autenticada, trazable y durable. El compromiso definitivo del estado local del certificado y el registro transaccional de los eventos de publicación constituirán la operación crítica; la disponibilidad inmediata de OCSP o CRL no condicionará una revocación válida.",
    ),
    (
        "4. registrar la fecha y hora efectiva de revocación;\n5. cambiar el estado del certificado de forma definitiva;\n6. publicar o poner a disposición el nuevo estado mediante OCSP;\n7. incorporar la revocación en la CRL correspondiente cuando aplique;\n8. registrar el resultado de cada publicación;\n9. impedir reactivación, modificación o reversión ordinaria.\n\nLa fecha y hora efectiva será la registrada por la Autoridad de Certificación al ejecutar, registrar y publicar el estado. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica.",
        "4. registrar la fecha y hora efectiva de revocación;\n5. cambiar y confirmar de forma durable el estado local del certificado como revocado;\n6. registrar, dentro de la misma transacción, eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL;\n7. intentar la publicación o puesta a disposición del nuevo estado mediante OCSP;\n8. incorporar la revocación en la CRL correspondiente cuando aplique;\n9. registrar el resultado de cada intento de publicación;\n10. impedir reactivación, modificación o reversión ordinaria.\n\nLa fecha y hora efectiva será la registrada por la Autoridad de Certificación al confirmar durablemente el estado local del certificado como revocado. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica. La publicación OCSP o CRL podrá completarse posteriormente sin modificar la fecha efectiva.",
    ),
    (
        "Si la publicación OCSP o CRL falla, la revocación no deberá revertirse. El incidente deberá escalarse y la publicación deberá reintentarse mediante los mecanismos de continuidad autorizados.",
        "Si la publicación OCSP o CRL falla, la revocación no deberá revertirse. El evento permanecerá pendiente en la cola transaccional u outbox y deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado. Agotado el límite operativo, se activarán los mecanismos de continuidad y el incidente permanecerá abierto hasta confirmar la publicación.",
    ),
    (
        "El acuse solo se generará cuando la revocación haya sido ejecutada satisfactoriamente.",
        "El acuse se generará cuando el estado local del certificado haya quedado confirmado durablemente como revocado. Si OCSP o CRL aún no reflejan el nuevo estado, el acuse deberá indicar **publicación pendiente**, identificar los eventos de outbox relacionados y actualizarse o complementarse cuando la publicación quede confirmada.",
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"No se encontró el texto esperado: {old[:100]}")
    text = text.replace(old, new, 1)

# Exactamente un salto de línea final.
path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")

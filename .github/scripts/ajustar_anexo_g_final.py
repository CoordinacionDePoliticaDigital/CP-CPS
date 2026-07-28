from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "Cuando la persona interesada continúe requiriendo un certificado, deberá iniciar un trámite independiente de nueva emisión o renovación, según corresponda.",
            "Cuando la persona interesada continúe requiriendo un certificado, deberá iniciar un trámite independiente de nueva emisión. Un certificado revocado no será elegible para renovación."
        ),
        (
            "La decisión de revocación y su registro local deberán ejecutarse como una operación autenticada, trazable y durable. El compromiso local será irreversible y deshabilitará inmediatamente el uso institucional del certificado; sin embargo, conforme al Anexo C, la fecha y hora efectiva normativa de revocación se fijará cuando la Autoridad de Certificación complete la publicación técnica del estado mediante OCSP y, cuando corresponda, CRL.",
            "La decisión de revocación y su registro local deberán ejecutarse como una operación autenticada, trazable y durable. Antes de construir cualquier respuesta OCSP o entrada de CRL, el sistema asignará y persistirá una fecha y hora efectiva única de revocación. Ese mismo valor se utilizará sin modificación en la publicación técnica y en todos los reintentos posteriores."
        ),
        (
            "4. registrar la fecha y hora del compromiso local de la decisión de revocación;\n5. cambiar y confirmar de forma durable el estado local como revocación pendiente de publicación;\n6. registrar, dentro de la misma transacción, eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL;\n7. intentar la publicación o puesta a disposición del nuevo estado mediante OCSP;\n8. incorporar la revocación en la CRL correspondiente cuando aplique;\n9. al completar satisfactoriamente la publicación técnica, registrar la fecha y hora efectiva normativa de revocación;\n10. registrar el resultado de cada intento de publicación;\n11. impedir reactivación, modificación o reversión ordinaria.\n\nLa fecha y hora efectiva normativa será aquella en que la Autoridad de Certificación complete satisfactoriamente la operación, registre la revocación y publique el estado correspondiente, conforme al Anexo C. El compromiso local previo permanecerá como evidencia operativa y no se utilizará como fecha efectiva. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica.",
            "4. asignar y persistir la fecha y hora efectiva única de revocación;\n5. cambiar y confirmar de forma durable el estado local como revocado;\n6. registrar, dentro de la misma transacción, eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL, incluyendo la fecha y hora efectiva persistida;\n7. construir e intentar la publicación o puesta a disposición del nuevo estado mediante OCSP utilizando esa misma fecha y hora;\n8. incorporar la revocación en la CRL correspondiente cuando aplique, utilizando esa misma fecha y hora;\n9. registrar el resultado de cada intento de publicación;\n10. impedir reactivación, modificación o reversión ordinaria.\n\nLa fecha y hora efectiva será la asignada y persistida al confirmar durablemente la revocación local. La publicación OCSP o CRL deberá reproducir ese mismo valor; los reintentos no podrán sustituirlo por una fecha posterior. Una fecha anterior contenida en una orden se conservará separadamente como metadato jurídico y no producirá retroactividad técnica."
        ),
        (
            "Si la publicación OCSP o CRL falla, la decisión local no deberá revertirse. El certificado permanecerá deshabilitado para uso institucional y el evento conservará el estado **revocación pendiente de publicación** en la cola transaccional u outbox. Deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado. Agotado el límite operativo, se activarán los mecanismos de continuidad y el incidente permanecerá abierto hasta confirmar la publicación y fijar la fecha y hora efectiva normativa.",
            "Si la publicación OCSP o CRL falla, la revocación local no deberá revertirse. El evento conservará el estado **publicación pendiente** en la cola transaccional u outbox y mantendrá la fecha y hora efectiva ya persistida. Deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado. Agotado el límite operativo, se activarán los mecanismos de continuidad y el incidente permanecerá abierto hasta confirmar la publicación."
        ),
        (
            "Mientras OCSP o CRL no reflejen el nuevo estado, únicamente podrá emitirse una constancia de recepción y compromiso local con la leyenda **revocación pendiente de publicación** y la referencia de los eventos de outbox. El acuse definitivo de revocación se generará cuando la publicación técnica haya quedado confirmada y exista fecha y hora efectiva normativa; la constancia previa deberá actualizarse o complementarse con dicho acuse.",
            "El acuse de revocación se generará cuando la revocación local haya quedado confirmada durablemente y exista fecha y hora efectiva persistida. Si OCSP o CRL aún no reflejan el nuevo estado, el acuse deberá indicar **publicación pendiente**, conservar la fecha y hora efectiva ya asignada e identificar los eventos de outbox relacionados; deberá actualizarse o complementarse cuando la publicación quede confirmada."
        ),
    ],
    Path("Productos/Anexo_C_Matriz_Causas_Revocacion.md"): [
        (
            "5. La fecha y hora efectiva de revocación será aquella en que la Autoridad de Certificación complete satisfactoriamente la operación, registre la revocación y publique el estado correspondiente. Cuando una orden judicial o administrativa señale una fecha anterior, esta se conservará únicamente como fecha de efectos ordenada y metadato jurídico del expediente; no modificará retroactivamente la fecha efectiva de revocación ni la publicación técnica en OCSP o CRL.",
            "5. La fecha y hora efectiva de revocación será aquella que la Autoridad de Certificación asigne y persista al confirmar durablemente el estado local del certificado como revocado. Este valor deberá incorporarse sin modificación en OCSP y, cuando corresponda, CRL, y conservarse en todos los reintentos de publicación. Cuando una orden judicial o administrativa señale una fecha anterior, esta se conservará únicamente como fecha de efectos ordenada y metadato jurídico del expediente; no modificará retroactivamente la fecha efectiva de revocación ni la publicación técnica."
        ),
        (
            "- fecha y hora efectiva de revocación, coincidente con la ejecución, registro y publicación técnica por la Autoridad de Certificación;",
            "- fecha y hora efectiva de revocación, asignada y persistida al confirmar durablemente el estado local y reproducida sin modificación en OCSP y, cuando corresponda, CRL;"
        ),
    ],
    Path("Productos/Anexo_O_Formato_Revocacion.md"): [
        (
            "La fecha y hora efectiva será la registrada por la Autoridad de Certificación al completar la ejecución y publicar el estado técnico. Una fecha anterior indicada por una orden judicial o administrativa se conservará únicamente como metadato jurídico y no retrotraerá el estado publicado en OCSP o CRL.",
            "La fecha y hora efectiva será la asignada y persistida por la Autoridad de Certificación al confirmar durablemente el estado local como revocado. Ese mismo valor deberá reproducirse sin modificación en OCSP y, cuando corresponda, CRL, incluso durante reintentos de publicación. Una fecha anterior indicada por una orden judicial o administrativa se conservará únicamente como metadato jurídico y no retrotraerá el estado técnico."
        ),
    ],
    Path("Productos/Anexos_D_al_G_Procedimientos_Operativos.md"): [
        (
            "## Anexo G. Procedimiento de Revocación\n1. **Iniciación:** El titular, su superior jerárquico, o la AC inician una solicitud de revocación.\n2. **Autenticación de Solicitud:** Se verifica la identidad del solicitante o la legitimidad de la causa (ej. acta de defunción, oficio de despido).\n3. **Procesamiento:** El sistema administrativo procesa la orden de revocar.\n4. **Actualización de Estado:** El número de serie del certificado se incorpora al servicio OCSP (o CRL si aplica).\n5. **Notificación:** Se envía un correo electrónico al titular informando que su certificado ha sido revocado y la fecha/hora de la acción.",
            "## Anexo G. Procedimiento de Revocación\n\nEsta sección queda sustituida por el documento autoritativo `Productos/Anexo_G_Procedimiento_Revocacion.md`. No deberá utilizarse como fuente normativa ni operativa independiente."
        ),
    ],
}

for path, pairs in replacements.items():
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f"No se encontró texto esperado en {path}: {old[:120]}")
        text = text.replace(old, new, 1)
    path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")

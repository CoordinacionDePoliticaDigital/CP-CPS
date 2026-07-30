from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "4. asignar y persistir la fecha y hora efectiva única de revocación;\n5. cambiar y confirmar de forma durable el estado local como revocado;\n6. registrar, dentro de la misma transacción, eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL, incluyendo la fecha y hora efectiva persistida;\n7. construir e intentar la publicación o puesta a disposición del nuevo estado mediante OCSP utilizando esa misma fecha y hora;\n8. incorporar la revocación en la CRL correspondiente cuando aplique, utilizando esa misma fecha y hora;\n9. registrar el resultado de cada intento de publicación;\n10. impedir reactivación, modificación o reversión ordinaria.",
            "4. dentro de una misma transacción atómica, asignar y persistir la fecha y hora efectiva única, cambiar el estado local a revocado y registrar los eventos pendientes de publicación en una cola transaccional u outbox para OCSP y, cuando corresponda, CRL; la transacción solo deberá confirmarse si las tres operaciones quedan registradas satisfactoriamente;\n5. después de confirmar la transacción, construir e intentar la publicación o puesta a disposición del nuevo estado mediante OCSP utilizando esa misma fecha y hora;\n6. incorporar la revocación en la CRL correspondiente cuando aplique, utilizando esa misma fecha y hora;\n7. registrar el resultado de cada intento de publicación;\n8. impedir reactivación, modificación o reversión ordinaria."
        ),
        (
            "La fecha y hora efectiva será la asignada y persistida al confirmar durablemente la revocación local. La publicación OCSP o CRL deberá reproducir ese mismo valor; los reintentos no podrán sustituirlo por una fecha posterior.",
            "La fecha y hora efectiva será la asignada y persistida en la misma transacción atómica que confirme durablemente la revocación local y registre el evento de publicación pendiente. Si la transacción no puede completar esos tres registros, no deberá confirmarse parcialmente. La publicación OCSP o CRL deberá reproducir ese mismo valor; los reintentos no podrán sustituirlo por una fecha posterior."
        ),
    ],
    Path("Formatos/CERTAC/07_Solicitud_Revocacion_Agente_FEA.md"): [
        (
            "- Clave de causal: {{CLAVE_CAUSAL}}\n- Descripción de causal: {{DESCRIPCION_CAUSAL}}",
            "- Clave normalizada de causal: {{CLAVE_CAUSAL}}\n- Denominación normalizada de causal: {{DENOMINACION_CAUSAL}}\n- Descripción de los hechos: {{DESCRIPCION_HECHOS}}"
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

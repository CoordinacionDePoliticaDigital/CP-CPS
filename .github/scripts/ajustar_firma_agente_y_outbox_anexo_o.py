from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "Las causas 05, 07, 10 y 11 requerirán validación expresa de la Autoridad de Certificación o de la unidad competente designada, además de la intervención técnica del agente cuando corresponda.",
            "Toda revocación asistida requerirá la firma electrónica avanzada de una persona con rol vigente de agente autorizado, incluida aquella iniciada por la propia Autoridad de Certificación o por una unidad competente. Las causas 05, 07, 10 y 11 requerirán además validación expresa de la Autoridad de Certificación o de la unidad competente designada."
        ),
    ],
    Path("Productos/Anexo_O_Formato_Revocacion.md"): [
        (
            "- **Resultado de publicación OCSP:** {{RESULTADO_OCSP}}\n- **Resultado de publicación CRL, cuando corresponda:** {{RESULTADO_CRL}}",
            "- **Estado de publicación:** {{ESTADO_PUBLICACION}}\n- **Resultado de publicación OCSP:** {{RESULTADO_OCSP}}\n- **Resultado de publicación CRL, cuando corresponda:** {{RESULTADO_CRL}}\n- **Referencia de eventos de publicación u outbox, cuando exista publicación pendiente:** {{REFERENCIA_OUTBOX}}\n- **Fecha y hora de confirmación de publicación, cuando corresponda:** {{FECHA_HORA_PUBLICACION}}"
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

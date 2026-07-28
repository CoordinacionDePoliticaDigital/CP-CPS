from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "Cuando la revocación sea urgente por pérdida, exposición, acceso no autorizado, copia o sospecha razonable de compromiso de la clave privada, la primera falla de publicación activará inmediatamente el mecanismo alterno autorizado de continuidad, sin esperar a que se agote el límite ordinario de reintentos. Deberá impedirse que los servicios institucionales acepten el certificado revocado y se deberá procurar la actualización externa por el canal alterno disponible hasta confirmar la publicación. Para revocaciones no urgentes, los mecanismos de continuidad se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación.",
            "Para toda revocación clasificada como urgente conforme a la sección 10, la primera falla de publicación activará inmediatamente el mecanismo alterno autorizado de continuidad, sin esperar a que se agote el límite ordinario de reintentos. Esta regla comprende, entre otros, compromiso o riesgo de la clave privada, suplantación o documentación falsa, uso indebido activo, órdenes de ejecución inmediata, compromiso de cuentas, dispositivos o sistemas y afectaciones potenciales a múltiples certificados, validadores o servicios. Deberá impedirse que los servicios institucionales acepten el certificado revocado y se deberá procurar la actualización externa por el canal alterno disponible hasta confirmar la publicación. Para revocaciones no urgentes, los mecanismos de continuidad se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación."
        ),
    ],
    Path("Formatos/CERTAC/06_Acuse_Revocacion_Titular_FEA.md"): [
        (
            "**Firma o sello electrónico de la Autoridad Certificadora:** {{FIRMA_ACUSE}}",
            "**Firma o sello electrónico de la Autoridad Certificadora:** {{FIRMA_ACUSE}}\n\n**Referencia o identificador de la firma o sello:** {{REFERENCIA_FIRMA_O_SELLO}}"
        ),
    ],
    Path("Formatos/CERTAC/08_Acuse_Revocacion_Agente_FEA.md"): [
        (
            "**Firma electrónica avanzada del agente autorizado:** {{FIRMA_AGENTE}}\n\n**Sello electrónico de la Autoridad Certificadora:** {{SELLO_ACUSE}}",
            "**Firma electrónica avanzada del agente autorizado:** {{FIRMA_AGENTE}}\n\n**Referencia o identificador de la firma del agente:** {{REFERENCIA_FIRMA_AGENTE}}\n\n**Sello electrónico de la Autoridad Certificadora:** {{SELLO_ACUSE}}\n\n**Referencia o identificador del sello:** {{REFERENCIA_SELLO_ACUSE}}"
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

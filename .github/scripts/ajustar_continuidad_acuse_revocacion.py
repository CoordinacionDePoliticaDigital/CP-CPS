from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "Si la publicación OCSP o CRL falla, la revocación local no deberá revertirse. El evento conservará el estado **publicación pendiente** en la cola transaccional u outbox y mantendrá la fecha y hora efectiva ya persistida. Deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado. Agotado el límite operativo, se activarán los mecanismos de continuidad y el incidente permanecerá abierto hasta confirmar la publicación.",
            "Si la publicación OCSP o CRL falla, la revocación local no deberá revertirse. El evento conservará el estado **publicación pendiente** en la cola transaccional u outbox y mantendrá la fecha y hora efectiva ya persistida. Deberá reintentarse automáticamente con identificador idempotente, incremento controlado de espera, límite de intentos antes de escalamiento y trazabilidad de cada resultado.\n\nCuando la revocación sea urgente por pérdida, exposición, acceso no autorizado, copia o sospecha razonable de compromiso de la clave privada, la primera falla de publicación activará inmediatamente el mecanismo alterno autorizado de continuidad, sin esperar a que se agote el límite ordinario de reintentos. Deberá impedirse que los servicios institucionales acepten el certificado revocado y se deberá procurar la actualización externa por el canal alterno disponible hasta confirmar la publicación. Para revocaciones no urgentes, los mecanismos de continuidad se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación."
        ),
    ],
    Path("Formatos/CERTAC/06_Acuse_Revocacion_Titular_FEA.md"): [
        (
            "- Fecha y hora efectiva de revocación: {{FECHA_HORA_REVOCACION}}\n- Estado de publicación: {{ESTADO_PUBLICACION}}",
            "- Fecha y hora efectiva de revocación: {{FECHA_HORA_REVOCACION}}\n- Persona o proceso autorizado que ejecutó: {{EJECUTOR}}\n- Estado de publicación: {{ESTADO_PUBLICACION}}"
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

from pathlib import Path

replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "Para toda revocación clasificada como urgente conforme a la sección 10, la primera falla de publicación activará inmediatamente el mecanismo alterno autorizado de continuidad, sin esperar a que se agote el límite ordinario de reintentos. Esta regla comprende, entre otros, compromiso o riesgo de la clave privada, suplantación o documentación falsa, uso indebido activo, órdenes de ejecución inmediata, compromiso de cuentas, dispositivos o sistemas y afectaciones potenciales a múltiples certificados, validadores o servicios. Deberá impedirse que los servicios institucionales acepten el certificado revocado y se deberá procurar la actualización externa por el canal alterno disponible hasta confirmar la publicación. Para revocaciones no urgentes, los mecanismos de continuidad se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación.",
            "Ante cualquier falla de publicación, los servicios institucionales deberán rechazar inmediatamente el certificado revocado con base en el estado local durable, sin esperar a que OCSP o CRL reflejen la actualización. Para toda revocación clasificada como urgente conforme a la sección 10, la primera falla activará además el mecanismo alterno autorizado de continuidad y la actualización externa por el canal alterno disponible, sin esperar a que se agote el límite ordinario de reintentos. Esta regla comprende, entre otros, compromiso o riesgo de la clave privada, suplantación o documentación falsa, uso indebido activo, órdenes de ejecución inmediata, compromiso de cuentas, dispositivos o sistemas y afectaciones potenciales a múltiples certificados, validadores o servicios. Para revocaciones no urgentes, el rechazo institucional será igualmente inmediato, mientras que los mecanismos alternos de propagación externa se activarán al agotarse el límite operativo. En todos los casos, el incidente permanecerá abierto hasta confirmar la publicación."
        ),
    ],
    Path("Formatos/CERTAC/07_Solicitud_Revocacion_Agente_FEA.md"): [
        (
            "## Certificado a revocar",
            "## Persona o entidad que inicia la revocación\n\n- Calidad en que interviene: {{CALIDAD_INICIADOR}}\n- Nombre o denominación: {{NOMBRE_INICIADOR}}\n- CURP, RFC o identificador institucional, cuando corresponda: {{IDENTIFICADOR_INICIADOR}}\n- Relación con la persona titular o fundamento de legitimidad: {{RELACION_O_FUNDAMENTO}}\n- Mandato, autorización, representación o acto de autoridad: {{TIPO_AUTORIZACION_REPRESENTACION}}\n- Referencia documental: {{REFERENCIA_AUTORIZACION_REPRESENTACION}}\n\n## Certificado a revocar"
        ),
        (
            "El agente autorizado hace constar que verificó la identidad de la persona titular o la legitimidad de la solicitud, cotejó la documentación y revisó los elementos que sustentan la causal indicada conforme a la Política de Certificación CP-ACCHIH-001, la Declaración de Prácticas de Certificación y la normatividad aplicable.",
            "El agente autorizado hace constar que verificó la identidad de la persona titular y, cuando la solicitud fue iniciada por una persona representante, tercero legitimado, dependencia, unidad competente o autoridad, verificó también la identidad o identificación institucional de quien inicia, su capacidad, mandato, autorización, representación o fundamento de legitimidad y la referencia documental correspondiente. Asimismo, cotejó la documentación y revisó los elementos que sustentan la causal indicada conforme a la Política de Certificación CP-ACCHIH-001, la Declaración de Prácticas de Certificación y la normatividad aplicable."
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

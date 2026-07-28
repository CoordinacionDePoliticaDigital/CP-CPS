from pathlib import Path

# Ajustes derivados de la revisión del PR #8.
replacements = {
    Path("Productos/Anexo_G_Procedimiento_Revocacion.md"): [
        (
            "La revocación directa mediante firma con el propio certificado no será requisito para estos certificados. La solicitud y autorización deberán realizarse mediante un canal institucional autenticado y quedar vinculadas al expediente, con identificación de quien solicita, quien autoriza y quien ejecuta.",
            "La revocación directa mediante firma con el propio certificado no será requisito para estos certificados. La solicitud y autorización deberán realizarse mediante un canal institucional autenticado y quedar vinculadas al expediente, con identificación de quien solicita, quien autoriza y quien ejecuta.\n\nAntes de revocar un certificado OCSP, TSA, de firma de CRL o de infraestructura deberá ejecutarse un plan de sustitución o continuidad que incluya, según corresponda:\n\n1. generar o habilitar una clave y un certificado de reemplazo con perfil autorizado;\n2. distribuir la nueva cadena y configuración a los componentes dependientes;\n3. comprobar firma, validación, publicación y monitoreo con el certificado de reemplazo;\n4. realizar el cambio controlado del servicio y confirmar que no existan dependencias activas del certificado saliente;\n5. preservar inventarios, evidencias de transición, responsables y criterios de reversión;\n6. revocar el certificado saliente únicamente después de confirmar la continuidad del servicio.\n\nCuando exista compromiso confirmado o riesgo inminente que impida mantener temporalmente el certificado saliente, la Autoridad de Certificación podrá ordenar su aislamiento y revocación inmediata. En ese caso deberá activarse previamente o de forma simultánea un respondedor, firmante o mecanismo alterno autorizado, aplicar el procedimiento de continuidad operativa y documentar cualquier periodo de degradación. No deberá continuarse la publicación con una clave comprometida."
        ),
    ],
    Path("Formatos/CERTAC/06_Acuse_Revocacion_Titular_FEA.md"): [
        (
            "- Fecha y hora efectiva de revocación: {{FECHA_HORA_REVOCACION}}\n- Estado publicado: Revocado.",
            "- Fecha y hora efectiva de revocación: {{FECHA_HORA_REVOCACION}}\n- Estado de publicación: {{ESTADO_PUBLICACION}}\n- Referencia de eventos de publicación u outbox: {{REFERENCIA_OUTBOX}}\n- Fecha y hora de confirmación de publicación, cuando corresponda: {{FECHA_HORA_PUBLICACION}}"
        ),
        (
            "La revocación es definitiva e irreversible. El certificado no podrá utilizarse para generar firmas después de la fecha y hora efectiva indicada. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado.",
            "La revocación es definitiva e irreversible. El certificado no podrá utilizarse para generar firmas después de la fecha y hora efectiva indicada. Cuando el estado de publicación sea **pendiente**, este acuse acreditará la revocación local y conservará la referencia de los eventos de publicación; deberá actualizarse o complementarse cuando OCSP y, en su caso, CRL reflejen el estado revocado. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado."
        ),
    ],
    Path("Formatos/CERTAC/08_Acuse_Revocacion_Agente_FEA.md"): [
        (
            "- Agente ejecutor: {{NOMBRE_AGENTE}}\n- Estado publicado: Revocado.",
            "- Agente ejecutor: {{NOMBRE_AGENTE}}\n- Estado de publicación: {{ESTADO_PUBLICACION}}\n- Referencia de eventos de publicación u outbox: {{REFERENCIA_OUTBOX}}\n- Fecha y hora de confirmación de publicación, cuando corresponda: {{FECHA_HORA_PUBLICACION}}"
        ),
        (
            "La revocación es definitiva e irreversible. El certificado no podrá utilizarse para generar firmas después de la fecha y hora efectiva indicada. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado.",
            "La revocación es definitiva e irreversible. El certificado no podrá utilizarse para generar firmas después de la fecha y hora efectiva indicada. Cuando el estado de publicación sea **pendiente**, este acuse acreditará la revocación local y conservará la referencia de los eventos de publicación; deberá actualizarse o complementarse cuando OCSP y, en su caso, CRL reflejen el estado revocado. Las firmas realizadas previamente deberán evaluarse conforme a su fecha, sello de tiempo, integridad y estado histórico del certificado."
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

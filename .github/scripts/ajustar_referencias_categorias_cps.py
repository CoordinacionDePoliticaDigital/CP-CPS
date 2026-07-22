from pathlib import Path

path = Path("CPS-ACCHIH-001-v1.2-proyecto.md")
text = path.read_text(encoding="utf-8")
old = (
    "Las categorías de servicios tecnológicos comprendidas por esta CPS son: infraestructura de "
    "cómputo y alojamiento; redes y conectividad; almacenamiento y bases de datos; gestión "
    "criptográfica de claves y certificados; identidad, autenticación y control de acceso; "
    "mensajería y notificaciones; monitoreo, registro y auditoría; respaldo, continuidad y "
    "recuperación; conservación de documentos y evidencias; y verificación automatizada de "
    "identidad. Su implementación funcional y controles aplicables se describen en las secciones "
    "5 a 8 y en los procedimientos internos correspondientes."
)
new = (
    "Las categorías de servicios tecnológicos comprendidas por esta CPS son: infraestructura de "
    "cómputo y alojamiento; redes y conectividad; almacenamiento y bases de datos; gestión "
    "criptográfica de claves y certificados; identidad, autenticación y control de acceso; "
    "mensajería y notificaciones; monitoreo, registro y auditoría; respaldo, continuidad y "
    "recuperación; conservación de documentos y evidencias; y verificación automatizada de "
    "identidad. Su implementación funcional y controles aplicables se documentan en las secciones "
    "5 a 8 para infraestructura, seguridad técnica, perfiles, OCSP, TSA y transición PKI; en la "
    "sección 3.1 para verificación automatizada de identidad; en la sección 9 para conservación de "
    "documentos y evidencias; y en los procedimientos internos correspondientes para el detalle "
    "operativo de cada categoría."
)
if old not in text:
    raise SystemExit("No se encontró el texto esperado")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

from pathlib import Path

path = Path("CPS-ACCHIH-001-v1.2-proyecto.md")
text = path.read_text(encoding="utf-8")

old = (
    "Las referencias a servicios de nube, gestión de claves, orquestación, almacenamiento, "
    "redes, identidad o mensajería describen capacidades funcionales y controles requeridos. "
    "Las secciones 5 a 8 de esta CPS documentan la arquitectura funcional, las categorías de "
    "servicios tecnológicos, los controles aplicados y el modelo general de implementación. "
    "Los nombres de proveedores, productos, marcas, cuentas, regiones y configuraciones "
    "concretas se conservarán siempre en inventarios, diagramas, procedimientos y registros "
    "internos sujetos a control de cambios. Su divulgación pública podrá limitarse cuando pueda "
    "afectar la seguridad, la continuidad operativa o las condiciones de contratación."
)

new = old + (
    "\n\nLas categorías de servicios tecnológicos comprendidas por esta CPS son: infraestructura de "
    "cómputo y alojamiento; redes y conectividad; almacenamiento y bases de datos; gestión "
    "criptográfica de claves y certificados; identidad, autenticación y control de acceso; "
    "mensajería y notificaciones; monitoreo, registro y auditoría; respaldo, continuidad y "
    "recuperación; conservación de documentos y evidencias; y verificación automatizada de "
    "identidad. Su implementación funcional y controles aplicables se describen en las secciones "
    "5 a 8 y en los procedimientos internos correspondientes."
)

if old not in text:
    raise SystemExit("No se encontró el texto esperado en la CPS")

path.write_text(text.replace(old, new, 1), encoding="utf-8")

from pathlib import Path

cp = Path("CP-ACCHIH-001-v1.2-proyecto.md")
cps = Path("CPS-ACCHIH-001-v1.2-proyecto.md")

cp_text = cp.read_text(encoding="utf-8")
old_cp = (
    "Los detalles de implementación, proveedores y servicios tecnológicos utilizados "
    "deberán documentarse en la Declaración de Prácticas de Certificación y en los "
    "procedimientos internos correspondientes."
)
new_cp = (
    "La Declaración de Prácticas de Certificación deberá documentar la arquitectura "
    "funcional, las categorías de servicios tecnológicos, los controles aplicados y el "
    "modelo general de implementación. Los nombres de proveedores, productos, cuentas, "
    "regiones, configuraciones concretas y demás detalles susceptibles de afectar la "
    "seguridad o la contratación se documentarán en inventarios, diagramas y procedimientos "
    "internos sujetos a control de cambios."
)
if old_cp not in cp_text:
    raise SystemExit("No se encontró el texto esperado en la CP")
cp.write_text(cp_text.replace(old_cp, new_cp), encoding="utf-8")

cps_text = cps.read_text(encoding="utf-8")
old_cps = (
    "Las referencias a servicios de nube, gestión de claves, orquestación, almacenamiento, "
    "redes, identidad o mensajería describen capacidades funcionales y controles requeridos. "
    "Los proveedores, productos, marcas y configuraciones concretas se documentarán en "
    "inventarios, diagramas, procedimientos y registros internos sujetos a control de cambios."
)
new_cps = (
    "Las referencias a servicios de nube, gestión de claves, orquestación, almacenamiento, "
    "redes, identidad o mensajería describen capacidades funcionales y controles requeridos. "
    "Las secciones 5 a 8 de esta CPS documentan la arquitectura funcional, las categorías de "
    "servicios tecnológicos, los controles aplicados y el modelo general de implementación. "
    "Los nombres de proveedores, productos, marcas, cuentas, regiones y configuraciones "
    "concretas se documentarán en inventarios, diagramas, procedimientos y registros internos "
    "sujetos a control de cambios, cuando su publicación pueda afectar la seguridad, la "
    "continuidad operativa o las condiciones de contratación."
)
if old_cps not in cps_text:
    raise SystemExit("No se encontró el texto esperado en la CPS")
cps.write_text(cps_text.replace(old_cps, new_cps), encoding="utf-8")

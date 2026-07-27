from pathlib import Path

files = {
    Path("Productos/Anexo_A_Perfil_Tecnico_Certificados.md"): [
        (
            "| `O` | Dependencia, entidad u organización relacionada |\n| `OU` | Unidad administrativa |",
            "| `O` | Obligatorio en todos los certificados de persona física. Valor fijo: `Gobierno del Estado de Chihuahua`. |\n| `OU` | Se utilizará únicamente cuando exista adscripción institucional aplicable. En certificados de personas servidoras públicas contendrá la denominación oficial de la dependencia, entidad u organismo de adscripción; en certificados ciudadanos deberá omitirse. |"
        ),
        (
            "La CPS deberá definir el mapeo exacto de CURP, RFC y otros identificadores, evitando duplicidades, ambigüedades y exposición innecesaria de datos personales.",
            "La CPS deberá definir el mapeo exacto de CURP, RFC y otros identificadores, evitando duplicidades, ambigüedades y exposición innecesaria de datos personales.\n\nLa clasificación normativa del perfil del certificado no dependerá del contenido textual del `Subject`, sino de la extensión `Certificate Policies`, mediante el OID institucional correspondiente al tipo de certificado emitido. Los sistemas validadores deberán utilizar dicho OID como criterio canónico de clasificación."
        )
    ],
    Path("CP-ACCHIH-001-v1.2-proyecto.md"): [
        (
            "j) 2.5.4.45.",
            "j) 2.5.4.45.\n\nEn todos los certificados de persona física, `organizationName` (`O`) deberá contener el valor `Gobierno del Estado de Chihuahua`.\n\n`organizationalUnitName` (`OU`) se utilizará únicamente cuando exista una adscripción institucional aplicable. En certificados de personas servidoras públicas deberá contener la denominación oficial de la dependencia, entidad u organismo de adscripción; en certificados ciudadanos deberá omitirse.\n\nLa clasificación normativa del perfil no dependerá del contenido textual del `Subject`, sino de la extensión `Certificate Policies`, mediante el OID institucional correspondiente al tipo de certificado emitido."
        )
    ],
    Path("CPS-ACCHIH-001-v1.2-proyecto.md"): [
        (
            "- `x500UniqueIdentifier` (`2.5.4.45`) contendrá el RFC.\n\nLos certificados históricos",
            "- `x500UniqueIdentifier` (`2.5.4.45`) contendrá el RFC.\n- `organizationName` (`2.5.4.10`) deberá incluirse en todos los certificados de persona física con el valor fijo `Gobierno del Estado de Chihuahua`.\n- `organizationalUnitName` (`2.5.4.11`) se utilizará únicamente cuando exista adscripción institucional aplicable. En certificados de personas servidoras públicas contendrá la denominación oficial de la dependencia, entidad u organismo de adscripción; en certificados ciudadanos se omitirá.\n\nLos certificados históricos"
        ),
        (
            "Los detalles normativos adicionales se regirán por los siguientes documentos controlados:",
            "La clasificación normativa del tipo de certificado no se inferirá del contenido textual del `Subject`. Deberá determinarse mediante la extensión `Certificate Policies`, utilizando el OID institucional aprobado para el perfil correspondiente. Los validadores y sistemas integrados deberán utilizar dicho OID como criterio canónico de clasificación.\n\nLos detalles normativos adicionales se regirán por los siguientes documentos controlados:"
        )
    ]
}

for path, replacements in files.items():
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"No se encontró texto esperado en {path}: {old[:80]}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")

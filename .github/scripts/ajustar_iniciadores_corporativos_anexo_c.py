from pathlib import Path

path = Path("Productos/Anexo_C_Matriz_Causas_Revocacion.md")
text = path.read_text(encoding="utf-8")

replacements = {
    "| `03_Disolución_de_persona_moral` | Disolución de persona moral | La persona moral representada ha sido disuelta, liquidada o ha dejado de existir jurídicamente, afectando el atributo de representación incorporado o vinculado al certificado. | Persona representante; autoridad competente; dependencia que acredite el hecho; agente autorizado. |":
    "| `03_Disolución_de_persona_moral` | Disolución de persona moral | La persona moral representada ha sido disuelta, liquidada o ha dejado de existir jurídicamente, afectando el atributo de representación incorporado o vinculado al certificado. | Persona representante; persona liquidadora; autoridad competente; dependencia que acredite el hecho; agente autorizado. |",
    "| `04_Fusión_o_escisión` | Fusión o escisión de persona moral | La persona moral se fusiona, escinde o modifica de forma que cambian la identidad, continuidad o facultades de representación asociadas al certificado. | Persona representante; autoridad competente; unidad jurídica; agente autorizado. |":
    "| `04_Fusión_o_escisión` | Fusión o escisión de persona moral | La persona moral se fusiona, escinde o modifica de forma que cambian la identidad, continuidad o facultades de representación asociadas al certificado. | Persona representante; cualquiera de las sociedades escindidas; sociedad subsistente en caso de fusión; autoridad competente; unidad jurídica; agente autorizado. |",
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"No se encontró el texto esperado: {old[:80]}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")

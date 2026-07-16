#!/usr/bin/env python3
"""Genera el documento consolidado de anexos desde sus fuentes autoritativas."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Productos" / "Anexos_Consolidados_A_K_L.md"
SOURCES = (
    ROOT / "Productos" / "Anexo_A_Perfil_Tecnico_Certificados.md",
    ROOT / "Productos" / "Anexo_K_Perfil_PAdES.md",
    ROOT / "Productos" / "Anexo_L_Politica_Sellado_Tiempo.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def demote_title(text: str) -> str:
    lines = text.rstrip().splitlines()
    if lines and lines[0].startswith("# "):
        lines[0] = "## " + lines[0][2:]
    return "\n".join(lines)


def render() -> str:
    missing = [str(path.relative_to(ROOT)) for path in SOURCES if not path.exists()]
    if missing:
        raise FileNotFoundError("Fuentes no encontradas: " + ", ".join(missing))

    manifest = "\n".join(
        f"| `{path.relative_to(ROOT).as_posix()}` | `{digest(path)}` |"
        for path in SOURCES
    )
    bodies = "\n\n---\n\n".join(
        demote_title(path.read_text(encoding="utf-8")) for path in SOURCES
    )

    return f"""# Anexos consolidados A, K y L

**Documento relacionado:** Política de Certificación CP-ACCHIH-001  
**Versión del consolidado:** 1.2  
**Estado:** Documento derivado  
**Fuente de verdad:** archivos individuales indicados en el manifiesto  

> Este archivo es generado automáticamente. No deberá editarse de forma manual. Cualquier modificación normativa deberá realizarse en el anexo individual correspondiente y después regenerar este consolidado.

## Manifiesto de fuentes

| Fuente autoritativa | SHA-256 |
|---|---|
{manifest}

---

{bodies}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verifica que el consolidado corresponda exactamente a las fuentes.",
    )
    args = parser.parse_args()
    expected = render()

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("El consolidado está ausente o desactualizado.")
            return 1
        print("El consolidado está sincronizado con sus fuentes.")
        return 0

    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Generado: {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

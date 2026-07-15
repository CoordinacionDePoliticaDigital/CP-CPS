from pathlib import Path

CP = Path("CP-ACCHIH-001-v1.2-proyecto.md")
REVISION = Path("Productos/Revision_CP-ACCHIH-001-v1.2.md")
INTEGRACION = Path("Productos/Integracion_CP-ACCHIH-001-v1.2.md")
BOOTSTRAP = Path("Productos/.pr-bootstrap")

text = CP.read_text(encoding="utf-8")

replacements = {
    "| 1.0 | Octubre 2024 | Emisión inicial del documento | Coordinación de Política Digital |": "| 1.0 | Octubre 2024 | Emisión inicial del documento | Coordinación de Política Digital |\n| 1.1 | [●] | Integración de información técnica y operativa derivada del despliegue inicial | Coordinación de Política Digital |\n| 1.2 | [●] | Revisión de consistencia normativa, neutralidad tecnológica, conservación, sellado de tiempo y arquitectura PKI | Coordinación de Política Digital |",
    "La plataforma conservará copia íntegra de los documentos firmados por un periodo sujeto a las políticas de archivo institucionales vigentes y a las capacidades de almacenamiento disponibles.": "La plataforma institucional conservará copia íntegra de los documentos firmados hasta por diez años. Este plazo constituye el periodo máximo ordinario de conservación prestado por la plataforma y no sustituye las obligaciones archivísticas de la dependencia responsable. La eliminación al concluir el plazo solo procederá cuando no exista obligación legal, archivística, probatoria, administrativa, judicial o de seguridad que requiera conservar el documento o sus evidencias por más tiempo, y cuando se haya efectuado la transferencia documental que corresponda.",
    "La TSA utilizará como referencia de tiempo cierto la hora provista por servicios de sincronización de tiempo de alta disponibilidad en la nube (ej. Amazon Time Sync Service) respaldados por relojes de referencia atómicos, los cuales se sincronizan con los estándares internacionales de Tiempo Universal Coordinado (UTC).": "La TSA utilizará como referencia de tiempo cierto la Hora Oficial de los Estados Unidos Mexicanos provista por el Centro Nacional de Metrología o la fuente oficial que legalmente la sustituya. Para su operación técnica podrán utilizarse servicios de sincronización de alta disponibilidad, siempre que mantengan trazabilidad respecto de dicha referencia temporal y del Tiempo Universal Coordinado. La tolerancia máxima y el método de medición se definirán en la Declaración de Prácticas de Certificación.",
    "La clave privada de la AC será administrada mediante un servicio autorizado de gestión de claves en la nube, bajo controles de acceso, mínimo privilegio, autenticación multifactor, registro de operaciones, segregación de funciones y restricciones de exportación cuando apliquen.": "La clave privada de la AC será administrada mediante un servicio criptográfico autorizado, bajo controles de acceso, mínimo privilegio, autenticación multifactor, registro de operaciones, segregación de funciones y restricciones de exportación cuando resulten aplicables. La clave de la AC raíz no deberá utilizarse para sellado de tiempo, cifrado de datos, firma de documentos de usuario final, autenticación de cliente o servidor ni firma de código. Los servicios OCSP y TSA deberán utilizar claves y certificados independientes.",
    "La operación vigente mediante una Autoridad de Certificación raíz emisora en línea se reconoce como arquitectura transitoria. La arquitectura objetivo será una Autoridad de Certificación raíz fuera de línea y una o más autoridades intermedias subordinadas emisoras.": "La operación vigente mediante una Autoridad de Certificación raíz emisora en línea se reconoce como arquitectura transitoria y continuará siendo reconocida hasta su sustitución, expiración o revocación, bajo controles compensatorios de acceso, monitoreo, trazabilidad, separación de funciones, continuidad y respuesta a incidentes.\n\nLa arquitectura objetivo será una cadena compuesta por una Autoridad de Certificación raíz fuera de línea, una sola capa de autoridades intermedias subordinadas emisoras y certificados de entidad final. La raíz objetivo deberá utilizar `pathLenConstraint=1` y cada autoridad intermedia emisora deberá utilizar `pathLenConstraint=0`; las autoridades intermedias no podrán emitir otras autoridades subordinadas.\n\nLa transición requerirá aprobación de la Coordinación de Política Digital y del Consejo Técnico, ceremonia de generación de claves, perfiles técnicos aprobados, publicación de la nueva cadena, pruebas de interoperabilidad, continuidad de OCSP y CRL, plan de coexistencia y actualización de la Política y la Declaración de Prácticas de Certificación.",
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"No se encontró el texto esperado para reemplazar: {old[:100]}")
    text = text.replace(old, new)

CP.write_text(text, encoding="utf-8")

for path in (REVISION, INTEGRACION, BOOTSTRAP):
    if path.exists():
        path.unlink()

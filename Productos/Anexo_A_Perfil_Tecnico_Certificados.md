# Anexo A. Perfil Técnico de Certificados

> [!WARNING]
> *Nota: Este documento ha sido adaptado para reflejar el perfil técnico de los certificados emitidos en el entorno productivo de la Autoridad de Certificación de Gobierno del Estado de Chihuahua, desplegado en infraestructura de alta disponibilidad.*

## 1. Introducción
El presente anexo define los perfiles técnicos de los certificados digitales emitidos por la Autoridad de Certificación de Gobierno del Estado de Chihuahua (AC), de conformidad con el estándar internacional X.509 v3 y el RFC 5280.

## 2. Perfil del Certificado Raíz (AC Raíz)
- **Versión:** V3
- **Número de Serie:** Generado de forma aleatoria y única (ej. 30303030...).

| Atributo | Valor | Descripción |
| :--- | :--- | :--- |
| **Issuer (Emisor)** | `CN=Autoridad de Certificación de Gobierno del Estado de Chihuahua, E=autoridad.certificadora@chihuahua.gob.mx, O=Gobierno del Estado de Chihuahua, OU=Coordinación de Politica Digital, L=Chihuahua, S=Chihuahua, C=MX, PostalCode=31000` | Entidad que emite y firma el certificado (Estado de Chihuahua). |
| **Subject (Titular)** | Igual al Issuer | Para el certificado raíz, el titular es la misma AC. |
| **Validity (Vigencia)** | Not Before: [Fecha de emisión]<br>Not After: [Fecha de emisión + 15 años] | Periodo de validez. (15 años). |
| **Key Size** | RSA 4096 bits | Longitud robusta recomendada. |
| **Signature Algorithm** | `sha512RSA` | Algoritmo de firma de alta seguridad soportado por KMS. |

### Extensiones del Certificado Raíz

| Extensión | Criticidad | Valor | Explicación |
| :--- | :--- | :--- | :--- |
| **Key Usage** | Crítica | `Digital Signature, Non-Repudiation, Key Encipherment, Data Encipherment, Certificate Sign, CRL Sign` | Permite firmar certificados, CRLs, y cifrado. |
| **Basic Constraints** | Crítica | `Subject Type=CA`, `Path Length Constraint=None` | Indica que es una Autoridad de Certificación. |
| **Extended Key Usage** | Crítica | `Time Stamping (1.3.6.1.5.5.7.3.8)` | Permite que el certificado se use para operaciones asociadas a TSA. |
| **Subject Key Identifier** | No crítica | [Hash de la clave pública] | Identificador de la llave. |

## 3. Perfil del Certificado de Usuario Final (Firma Electrónica Avanzada)
- **Versión:** V3
- **Número de Serie:** Único.
- **Algoritmo de Firma:** `sha512RSA`.
- **Validez:** Hasta 4 años.
- **Subject:** 
  - `CN` = Nombre de la persona física
  - `E` = Correo electrónico
  - `OID.2.5.4.45` = RFC
  - `SERIALNUMBER` = CURP
- **Subject Public Key Info:** RSA 2048 bits.

### Extensiones del Certificado de Usuario Final

| Extensión | Criticidad | Valor |
| :--- | :--- | :--- |
| **Key Usage** | Crítica | `Digital Signature, Non-Repudiation, Key Encipherment, Key Agreement` |
| **Extended Key Usage** | No crítica | `Client Authentication (1.3.6.1.5.5.7.3.2), Secure Email (1.3.6.1.5.5.7.3.4)` |
| **Basic Constraints** | Crítica | `Subject Type=End Entity`, `Path Length Constraint=None` |
| **Subject Alternative Name** | No crítica | `RFC822 Name=[correo electrónico]` |
| **Authority Information Access** | No crítica | URLs de OCSP y CA Issuers |

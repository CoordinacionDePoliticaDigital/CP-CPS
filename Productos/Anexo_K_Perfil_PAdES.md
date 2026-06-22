# Anexo K. Perfil PAdES Institucional

> [!WARNING]
> *Nota: Este documento ha sido adaptado para reflejar el perfil técnico PAdES utilizado en el entorno productivo de la plataforma Firmame de Gobierno del Estado de Chihuahua.*

## 1. Estándar Base
La plataforma institucional utilizará el formato **PAdES (PDF Advanced Electronic Signatures)**, integrando constancias de conservación y validación a largo plazo. Las firmas se generan y estampan a través de la infraestructura criptográfica de la Autoridad de Certificación de Gobierno del Estado de Chihuahua.


## 2. Algoritmos Soportados
- **Hash:** SHA-256 o superior.
- **Firma:** `sha512RSA` con llaves RSA de 2048 bits (para usuarios y sellos de tiempo operativos) y 4096 bits (para constancias de conservación a largo plazo).

## 3. Elementos Visuales de la Firma y Sellos
La representación visual de la firma en el documento PDF contendrá elementos de validación humana y criptográfica:
- **Datos del Firmante:** Nombre, RFC/CURP y correo electrónico.
- **Trazo Autógrafo:** Incorporación de la imagen del dibujo de trazo de firma autógrafa capturada en la aplicación (Servicio Canvas).
- **Evidencia Temporal:** Estampa de tiempo aplicada criptográficamente por la TSA del Gobierno del Estado de Chihuahua y visible en el documento.
- **Hoja de Firmas:** Inclusión de una hoja anexa final que resume las firmas recolectadas, los códigos QR de verificación, el folio o identificador único del documento, y el respaldo legal avalado por la Autoridad Certificadora.

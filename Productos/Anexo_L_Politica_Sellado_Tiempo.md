# Anexo L. Política de Sellado de Tiempo (TSP)

> [!WARNING]
> *Nota: Este documento ha sido redactado con base en estándares genéricos (RFC 3161) y queda pendiente de revisión y aceptación final para su ajuste al alcance propio de la Autoridad de Certificación de Gobierno del Estado de Chihuahua.*

## 1. Alcance
Establece las reglas técnicas y operativas bajo las cuales opera la Autoridad de Sellado de Tiempo (TSA) vinculada a la Autoridad de Certificación de Gobierno del Estado de Chihuahua.

## 2. Referencia Temporal
La TSA se sincronizará utilizando servicios de tiempo de alta disponibilidad en la nube. Este servicio se respalda por una flota de relojes atómicos y satelitales redundantes, ajustados al estándar global Tiempo Universal Coordinado (UTC), ofreciendo una precisión equivalente o superior a la del Centro Nacional de Metrología (CENAM).

## 3. Emisión de Sellos de Tiempo (Time-Stamps)
- **Formato:** Acorde a RFC 3161 (`TimeStampReq` y `TimeStampResp`).
- **Gestión Criptográfica:** Las operaciones de firma de la TSA se delegan a un Módulo de Seguridad en Hardware (KMS) configurado en la nube.
- **Algoritmo de Firma de la TSA:** Se generarán firmas con `sha512RSA`. La infraestructura mantiene dos perfiles de certificados de Autoridad de Sellado:
  - **TSA 2048 (`CN=Gobierno del Estado de Chihuahua TSA 2048`):** Llave de 2048 bits para sellos operativos generales.
  - **TSA 4096 (`CN=Gobierno del Estado de Chihuahua TSA 4096`):** Llave de 4096 bits para constancias de conservación de largo plazo.
- Ambos certificados operan como entidades finales (`Subject Type=End Entity`), limitados estrictamente al uso de **Firma Digital** y **Time Stamping (1.3.6.1.5.5.7.3.8)**.

## 4. Retención de Bitácoras
Las transacciones de emisión de sellos de tiempo serán auditadas y conservadas conforme a la normativa archivística estatal aplicable.

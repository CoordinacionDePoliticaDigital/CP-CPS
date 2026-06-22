<div align="center">
  <img src="./img/logo1.png" alt="Gobierno del Estado" height="80" style="margin-right: 30px;" />
  <img src="./img/logo2.png" alt="Autoridad Certificadora" height="80" />
</div>
<br>

# Declaración de Prácticas de Certificación (CPS)
## Autoridad de Certificación de Gobierno del Estado de Chihuahua

**Clave del documento:** CPS-ACCHIH-001  
**OID:** 1.3.6.1.4.1.63888.1.2  
**Versión:** 1.2  
**Estado:** Proyecto  
**Fecha de emisión:** Octubre 2024  
**Autoridad responsable:** Coordinación de Política Digital  

---

## Índice de Contenidos

- [1. Introducción](#1-introducción)
  - [1.1. Visión general](#11-visión-general)
  - [1.2. Identificación del documento](#12-identificación-del-documento)
  - [1.3. Entidades PKI](#13-entidades-pki)
  - [1.4. Glosario y Acrónimos](#14-glosario-y-acrónimos)
- [2. Publicación y Repositorios](#2-publicación-y-repositorios)
- [3. Identificación y Autenticación](#3-identificación-y-autenticación)
  - [3.1. Registro Inicial](#31-registro-inicial)
  - [3.2. Renovación](#32-renovación)
- [4. Requisitos Operativos del Ciclo de Vida del Certificado](#4-requisitos-operativos-del-ciclo-de-vida-del-certificado)
  - [4.1. Solicitud y Emisión](#41-solicitud-y-emisión)
  - [4.2. Entrega y Aceptación](#42-entrega-y-aceptación)
  - [4.3. Revocación](#43-revocación)
- [5. Controles de Gestión, Operativos y Físicos](#5-controles-de-gestión-operativos-y-físicos)
  - [5.1. Controles Físicos](#51-controles-físicos)
  - [5.2. Auditoría y Bitácoras](#52-auditoría-y-bitácoras)
  - [5.3. Continuidad del Negocio](#53-continuidad-del-negocio)
- [6. Controles de Seguridad Técnica](#6-controles-de-seguridad-técnica)
  - [6.1. Gestión del Par de Claves (KMS)](#61-gestión-del-par-de-claves-kms)
  - [6.2. Seguridad Informática y de Red](#62-seguridad-informática-y-de-red)
- [7. Perfiles de Certificados y OCSP](#7-perfiles-de-certificados-y-ocsp)
  - [7.1. Perfil del Certificado Raíz](#71-perfil-del-certificado-raíz)
  - [7.2. Perfil de Usuario Final](#72-perfil-de-usuario-final)
  - [7.3. Perfiles de TSA](#73-perfiles-de-tsa)
- [8. Auditoría de Cumplimiento](#8-auditoría-de-cumplimiento)
- [9. Asuntos Legales y Comerciales](#9-asuntos-legales-y-comerciales)

---

## 1. Introducción
### 1.1. Visión general
Esta Declaración de Prácticas de Certificación (CPS) detalla los procedimientos técnicos, físicos, procedimentales y legales bajo los cuales opera la Autoridad de Certificación (AC) del Gobierno del Estado de Chihuahua. Este documento implementa las directrices establecidas en la Política de Certificación (CP-ACCHIH-001-v1.2).

### 1.2. Identificación del documento
**Nombre:** Declaración de Prácticas de Certificación (CPS-ACCHIH-001)  
**OID de la CPS:** 1.3.6.1.4.1.63888.1.2  
**OID de la Política (CP) asociada:** 1.3.6.1.4.1.63888.1.1  

### 1.3. Entidades PKI
- **Autoridad de Certificación (AC):** El núcleo de procesamiento alojado en la nube que emite los certificados.
- **Autoridad de Registro (AR) / Agentes:** Custodios y administradores responsables de enrolar y verificar a los usuarios.
- **Autoridad de Sellado de Tiempo (TSA):** Servicio criptográfico operado por la AC que emite estampillas de tiempo (2048 y 4096 bits).
- **Suscriptores:** Personas físicas y servidores públicos que generan firmas electrónicas.
- **Terceros Usuarios (Relying Parties):** Entidades que validan la vigencia de los certificados.

### 1.4. Glosario y Acrónimos
- **AC / CA (Autoridad de Certificación):** Entidad de confianza responsable de emitir, revocar y gestionar certificados digitales.
- **AR / RA (Autoridad de Registro):** Entidad o persona (Agente/Custodio) delegada por la AC para verificar la identidad de los solicitantes.
- **TSA (Time Stamping Authority):** Autoridad de Sellado de Tiempo. Emite constancias criptográficas que demuestran que un dato existía en un momento específico.
- **PKI (Public Key Infrastructure):** Infraestructura de Clave Pública. Conjunto de hardware, software y políticas para gestionar firmas electrónicas.
- **KMS / HSM (Módulo de Seguridad en Hardware):** Servicio en la nube o dispositivo físico seguro diseñado para custodiar claves privadas y ejecutar firmas.
- **OCSP (Online Certificate Status Protocol):** Protocolo para consultar el estado de revocación de un certificado en tiempo real.
- **CRL (Certificate Revocation List):** Lista de certificados revocados publicada periódicamente por la AC.
- **PAdES (PDF Advanced Electronic Signatures):** Estándar para firmas electrónicas avanzadas incrustadas en documentos PDF, garantizando validez a largo plazo.
- **IdP (Identity Provider):** Proveedor de Identidad. Sistema centralizado que gestiona autenticación de usuarios.

## 2. Publicación y Repositorios
La AC mantiene repositorios públicos y de alta disponibilidad desplegados sobre almacenamiento de objetos y redes de entrega de contenido (CDN) a través del sitio web oficial `autoridadcertificadora.chihuahua.gob.mx` para la distribución de la CP, CPS, Términos y Condiciones.
El estado de revocación (OCSP) se opera a través de balanceadores de carga accesibles 24/7 en `https://caservicescpd.chihuahua.gob.mx`.

## 3. Identificación y Autenticación
### 3.1. Registro Inicial
Los suscriptores deben proporcionar su identidad mediante CURP y RFC. La validación se gestiona de manera centralizada mediante un Proveedor de Identidad (IdP) que maneja sesiones seguras OAuth y tokens JWT.

### 3.2. Renovación
Los certificados vencidos requieren intervención y validación manual por parte del Agente (Custodio). Los certificados vigentes pueden renovarse de manera remota al firmar digitalmente la solicitud con el certificado actual del usuario.

## 4. Requisitos Operativos del Ciclo de Vida del Certificado
### 4.1. Solicitud y Emisión
La solicitud se ejecuta en el navegador web del usuario a través del portal de firmantes. El par de claves asimétricas se genera en el equipo local del usuario; la llave privada no viaja por la red. La solicitud pública (PKCS#10) se envía a un Agente, quien, tras validar la identidad, autoriza la emisión firmando un oficio.
La AC detecta la autorización vía Webhooks y utiliza el Módulo de Seguridad en Hardware (HSM) para emitir el certificado.

### 4.2. Entrega y Aceptación
El certificado generado es remitido al repositorio en la nube y se notifica la disponibilidad al usuario vía correo electrónico empleando servicios de mensajería institucional.

### 4.3. Revocación
La revocación puede ser motivada por `keyCompromise`, `cessationOfOperation`, entre otras. Puede ser iniciada directamente por el suscriptor (autenticándose con su certificado) o por un Custodio. La ejecución actualiza instantáneamente las bases de datos de la Autoridad para reflejar el estado en el servicio OCSP.

## 5. Controles de Gestión, Operativos y Físicos
### 5.1. Controles Físicos
Los servicios criptográficos, de orquestación y de bases de datos operan sobre infraestructura de nube, heredando certificaciones de seguridad física de centros de datos de alta clasificación (equivalente a Tier 4). A nivel operativo local, los Agentes y Custodios ingresan a portales bajo estrictos controles físicos (videovigilancia, acceso biométrico RFID) en las oficinas de la Coordinación de Política Digital.

### 5.2. Auditoría y Bitácoras
Los eventos de infraestructura se almacenan en bitácoras protegidas. En particular, la TSA mantiene registros detallados en bases de datos (`TimeStampEvent`, `TimeStampResponse`) de cada estampilla generada, referenciando la dirección IP, el hash del documento, la estampa de tiempo y la firma generada.

### 5.3. Continuidad del Negocio
Se garantiza un modelo de continuidad y tolerancia a fallos nativo en la nube mediante orquestación dinámica de contenedores que escalan horizontalmente (AutoScaling), respaldos automatizados de configuraciones y esquemas de base de datos distribuidas en múltiples Zonas de Disponibilidad (Multi-AZ).

## 6. Controles de Seguridad Técnica
### 6.1. Gestión del Par de Claves (KMS)
La clave privada de la Autoridad de Certificación y de la Autoridad de Sellado de Tiempo están resguardadas en un Módulo de Seguridad de Hardware en la nube (HSM). Toda operación de firma se realiza de manera interna en el entorno criptográfico sellado; las claves nunca son exportadas en texto claro.
### 6.2. Seguridad Informática y de Red
La red opera bajo Grupos de Seguridad (Security Groups) estrictos dentro de Redes Privadas Virtuales (VPC). Las conexiones públicas requieren HTTPS con configuraciones TLSv1.2 obligatorias mediante servicios de gestión de certificados públicos.

## 7. Perfiles de Certificados y OCSP
### 7.1. Perfil del Certificado Raíz
- **Algoritmo y Tamaño:** `sha512RSA`, 4096 bits.
- **Issuer:** `CN=Autoridad de Certificación de Gobierno del Estado de Chihuahua, E=autoridad.certificadora@chihuahua.gob.mx, O=Gobierno del Estado de Chihuahua, OU=Coordinación de Politica Digital, L=Chihuahua, S=Chihuahua, C=MX, PostalCode=31000`
- **Key Usage (Crítico):** Digital Signature, Non-Repudiation, Key Encipherment, Data Encipherment, Certificate Sign, CRL Sign
- **EKU:** Time Stamping (1.3.6.1.5.5.7.3.8)

### 7.2. Perfil de Usuario Final
- **Algoritmo y Tamaño:** `sha512RSA`, 2048 bits.
- **Subject:** `CN=[Nombre], E=[Correo], OID.2.5.4.45=[RFC/CURP], SERIALNUMBER=[CURP/RFC]`
- **Extensiones Clave:** Digital Signature, Non-Repudiation, Key Encipherment, Key Agreement. Client Authentication y Secure Email en EKU.

### 7.3. Perfiles de TSA
- **TSA 2048 (`CN=Gobierno del Estado de Chihuahua TSA 2048`)**: Empleado para estampillado operativo común.
- **TSA 4096 (`CN=Gobierno del Estado de Chihuahua TSA 4096`)**: Utilizado para constancias de conservación y retención a largo plazo.
- Las estampillas derivan su exactitud temporal de servicios de sincronización de tiempo de alta disponibilidad en la nube.

## 8. Auditoría de Cumplimiento
La infraestructura criptográfica principal (KMS) cuenta con certificaciones FIPS 140-2 de nivel 2 y 3. El Gobierno de Chihuahua realizará verificaciones periódicas para asegurar que los procesos de enrolamiento y operación sigan la Política de Certificación.

## 9. Asuntos Legales y Comerciales
Las responsabilidades de confidencialidad, propiedad de las claves, causales de recisión y manejo de datos personales se rigen estrictamente por los Términos y Condiciones vigentes y el Aviso de Privacidad Integral aplicable a los ciudadanos y servidores públicos que utilicen la plataforma.

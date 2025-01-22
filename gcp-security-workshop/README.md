
# GCP Security Workshop

## Objetivo
Ejercicio práctico para implementar y comprender los conceptos fundamentales de seguridad en Google Cloud Platform:
- Identity and Access Management (IAM)
- Identity-Aware Proxy (IAP)
- Secret Manager
- Key Management Service (KMS)
- Cloud Functions

## Estructura del Proyecto
```bash
gcp-security-workshop/
├── README.md
├── src/
│   ├── function/
│   └── app/
├── terraform/
└── scripts/
```


El ejercicio consistirá en crear una aplicación con los siguientes componentes:

1. Una Cloud Function que:
   - Lee un secreto desde Secret Manager
   - Usa KMS para descifrar información
   - Tiene permisos restringidos mediante IAM

2. Una aplicación web simple que:
   - Está protegida por IAP
   - Se comunica con la Cloud Function
   - Requiere autenticación para acceder

Pasos específicos:

1. **Configuración inicial**:
   - Crear un proyecto en GCP
   - Habilitar las APIs necesarias
   - Configurar las credenciales iniciales

2. **IAM y Service Accounts**:
   - Crear una Service Account para la Cloud Function
   - Configurar roles mínimos necesarios
   - Implementar el principio de mínimo privilegio

3. **Secret Manager y KMS**:
   - Crear una llave en Cloud KMS
   - Almacenar un secreto en Secret Manager
   - Configurar los permisos necesarios

4. **Cloud Function**:
   - Desarrollar la función que accede a los secretos
   - Implementar el cifrado/descifrado
   - Configurar la autenticación


[contenido anterior se mantiene igual...]

### Estructura de archivos
```bash
src/function/
├── main.py
├── requirements.txt
```

5. **IAP**:
   - Configurar OAuth consent screen
   - Implementar IAP en la aplicación web
   - Gestionar los accesos autorizados




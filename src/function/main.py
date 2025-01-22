from google.cloud import secretmanager
from google.cloud import kms
import os
from google.auth import default
from google.auth.transport import requests

PROJECT_ID =  os.environ.get('PROJECT_ID')
SECRET_NAME = os.environ.get('SECRET_NAME')
LOCATION = os.environ.get('LOCATION')
KEYRING_NAME = os.environ.get('KEYRING_NAME')
KEY_NAME = os.environ.get('KEY_NAME')

def access_secret(secret_id):
    """Accede a un secreto en Secret Manager"""
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def decrypt_data(ciphertext):
    """Descifra datos usando Cloud KMS"""
    client = kms.KeyManagementServiceClient()
    key_path = client.crypto_key_path(PROJECT_ID, LOCATION, KEYRING_NAME, KEY_NAME)
    decrypt_response = client.decrypt(request={"name": key_path, "ciphertext": ciphertext}).plaintext.decode("utf-8")

@functions_framework.http
def process_request(request)
   """HTTP Cloud Function que maneja las solicitudes"""
  try:
    # Acceder al secreto
    secret_value = access_secret(SECRET_NAME)

    return {
        'success': True,
        'message': f'Secreto recuperado exitosamente: {secret_value}'
    }
  except Exception as e:
    return {
        'success': False,
        'message': f'Error al procesar la solicitud: {str(e)}'
    }
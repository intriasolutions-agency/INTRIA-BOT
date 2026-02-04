import os
import pickle
import csv
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

# Configuración de OAuth2
CLIENT_CONFIG = {
    "web": {
        "client_id": "7495575792-1c7om9v9k564mffthslj6hbd1cd1a8dm.apps.googleusercontent.com",
        "project_id": "intria-bot-project",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost:8080/"]
    }
}

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1VQHlNkH-GopAPP6VP-WvLc-Bl-Lkc8jrNAuNxTgLNZg'
RANGE_NAME = 'Hoja 1!A2:AE' # Ajustar según el nombre de la pestaña

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
            # USAR CONSOLE FLOW
            auth_url, _ = flow.authorization_url(prompt='consent')
            print(f'ENTRA AQUÍ: {auth_url}')
            code = input('PEGA EL CÓDIGO AQUÍ: ')
            flow.fetch_token(code=code)
            creds = flow.credentials
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('sheets', 'v4', credentials=creds)

def extract_image_url(product_id):
    url = f"https://www.xbrisantafe.shop/productos/{product_id}/"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Buscar la imagen principal en el meta tag o estructura de mitiendanube
            img_tag = soup.find('meta', property='og:image')
            if img_tag:
                return img_tag['content'].replace('//', 'https://')
            
            # Fallback a buscar en el cuerpo si el meta falla
            for img in soup.find_all('img'):
                src = img.get('src', '')
                if 'mitiendanube.com' in src and 'products' in src and '1024-1024' in src:
                    return src.replace('//', 'https://')
    except Exception as e:
        print(f"Error extrayendo {product_id}: {e}")
    return ""

def main():
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No se encontraron datos.')
        return

    updates = []
    for i, row in enumerate(values):
        if not row: continue
        product_id = row[0] # Identificador de URL
        print(f"Procesando {i+2}: {product_id}...")
        image_url = extract_image_url(product_id)
        
        # Preparar la actualización para la columna AE (indice 30)
        updates.append({
            'range': f'Hoja 1!AE{i+2}',
            'values': [[image_url]]
        })

    if updates:
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': updates
        }
        sheet.values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
        print(f"¡Hecho! {len(updates)} filas actualizadas.")

if __name__ == '__main__':
    main()

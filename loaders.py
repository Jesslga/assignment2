import pandas as pd
import requests
import io
import json

def get_google_drive_csv_specified_columns(file_id, columns_to_keep, datatype):
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text), usecols=columns_to_keep, dtype=datatype)
    return df

def get_google_drive_csv(file_id):
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text))
    return df

def load_json_google_drive(file_id):
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url)
    response.raise_for_status()
    json_data = json.loads(response.text)
    return json_data

def get_google_drive_excel(file_id, sheet_name, columns_to_keep, skiprows):
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url)
    response.raise_for_status()
    with io.BytesIO(response.content) as bio:
        df = pd.read_excel(bio, sheet_name=sheet_name, usecols=columns_to_keep, skiprows=skiprows)
    return df

"""Loads Data from Google Drive"""
import io
import json
import pandas as pd
import requests

def get_google_drive_csv_specified_columns(file_id, columns_to_keep, datatype):
    """Loads a CSV file from Google Drive with specified columns and data types"""
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url, timeout=60)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text), usecols=columns_to_keep, dtype=datatype)
    return df

def get_google_drive_csv(file_id):
    """Loads a CSV file from Google Drive"""
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url, timeout=60)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text))
    return df

def load_json_google_drive(file_id):
    """Loads a JSON file from Google Drive"""
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url, timeout=60)
    response.raise_for_status()
    json_data = json.loads(response.text)
    return json_data

def get_google_drive_excel(file_id, sheet_name, columns_to_keep, skiprows):
    """Loads an Excel file from Google Drive with specified columns and data types"""
    download_url = f'https://drive.google.com/uc?id={file_id}'
    response = requests.get(download_url, timeout=60)
    response.raise_for_status()
    with io.BytesIO(response.content) as bio:
        df = pd.read_excel(bio, sheet_name=sheet_name, usecols=columns_to_keep, skiprows=skiprows)
    return df

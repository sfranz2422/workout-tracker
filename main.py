from dotenv import load_dotenv
import requests
import datetime
import os

load_dotenv('.env')
os.environ.get('ACCOUNT_SSID')

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
NUTRITIONIX_ENDPOINT = os.environ.get('NUTRITIONIX_ENDPOINT')
SHEETZY_AUTH = os.environ.get('SHEETZY_AUTH')
SHEETZ_ENDPOINT = os.environ.get('SHEETZ_ENDPOINT')
GENDER = os.environ.get('GENDER')
WEIGHT_KG = os.environ.get('WEIGHT_KG')
HEIGHT_CM = os.environ.get('HEIGHT_CM')
AGE = os.environ.get('AGE')

exercise_text = input("What exercise did you complete? \n")
total_date = datetime.datetime.now()
time_now = total_date.strftime("%H:%M:%S")
date_now = total_date.strftime("%d/%m/%Y")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}
response = requests.post(NUTRITIONIX_ENDPOINT, json=exercise_params, headers=exercise_headers)

data = response.json()
print(data)
print(data['exercises'][0]['user_input'])
body = {
    'workout': {
        'date': date_now,
        'time': time_now,
        'exercise': data['exercises'][0]['user_input'],
        'duration': data['exercises'][0]['duration_min'],
        'calories': data['exercises'][0]['nf_calories']
    }

}

headers = {
    'Authorization': f"Bearer {SHEETZY_AUTH}"
}
response_sheet = requests.post(SHEETZ_ENDPOINT, json=body, headers=headers)
print(response_sheet.json())

import requests
from utils.utils import save_data
from dotenv import dotenv_values

config = dotenv_values(".env")

EMSI_CLIENT_ID = config['EMSI_CLIENT_ID']
EMSI_CLIENT_SECRET = config['EMSI_CLIENT_SECRET']

URLS={
    "authentication_url": "https://auth.emsicloud.com/connect/token", 
    "data_url": "https://emsiservices.com/skills/versions/latest/skills"
}

def main():



    payload = f"client_id={EMSI_CLIENT_ID}&client_secret={EMSI_CLIENT_SECRET}&grant_type=client_credentials&scope=emsi_open"
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", URLS["authentication_url"], data=payload, headers=headers)
    if response.status_code == 200:
        json_req_object = response.json()
        token = json_req_object['access_token']
    else:
        print(f"Unable to get the EMSI token, error: {response.status_code}")

   
    if token is not None:
        querystring = {"fields":"id,name,type"}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.request("GET", URLS["data_url"], headers=headers, params=querystring)
        skills = response.json()
        skills = skills['data']    

        save_data(skills, 'hardskills.json')

if __name__ == '__main__':
    main()

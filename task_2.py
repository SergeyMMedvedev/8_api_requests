import requests
import os
from pprint import pprint
from dotenv import load_dotenv


class YaUploader:

    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    GET_FILES = '/files'
    UPLOAD_LINK = '/upload'

    def __init__(self, token) -> None:
        self.token = token

    def get_headers(self):
        headers = {
            "Authorization": self.token,
            "Content-type": "application/json"
        }
        return headers

    def get_files(self):
        url = self.BASE_URL + self.GET_FILES
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def _get_upload_link(self, params):
        url = self.BASE_URL + self.UPLOAD_LINK
        response = requests.get(url, headers=self.get_headers(), params=params)
        response.raise_for_status()
        response_body = response.json()
        href = response_body.get('href', '')
        return href

    def upload(self, filename, path_to_file):
        params = {
            "path": path_to_file,
            "overwrite": "true"
        }
        url = self._get_upload_link(params)
        response = requests.put(
            url, 
            headers=self.get_headers(), 
            params=params, 
            data=open(filename, 'rb')
        )
        response.raise_for_status()
        if response.status_code == 201:
            print(f'{params["path"]} successfully created!')


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('YA_TOKEN')
    file_name = 'test.txt'
    path_to_file = r'netology/' + file_name
    ya = YaUploader(TOKEN)
    ya.upload(file_name, path_to_file)

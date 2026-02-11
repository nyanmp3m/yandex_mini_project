import requests


def get_coord(address=None, rc=10):
    try:
        server_address = 'https://geocode-maps.yandex.ru/v1?'
        api_key = '8013b162-6b42-4997-9691-77b7074026e0'

        geocode = f'&geocode={address}'
        lang = f'&lang=ru_RU'
        format_answer = f'&format=json'
        result_count = f'&result={rc}'

        url = f'{server_address}apikey={api_key}{geocode}{lang}{format_answer}{result_count}'
        response = requests.get(url)

        if response.status_code == 200:
            return response
        else:
            print("Ошибка получения координат объекта", response.status_code, response.text)
    except Exception as exc:
        print(exc)

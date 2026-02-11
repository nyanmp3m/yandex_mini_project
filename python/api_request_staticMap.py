import requests

def get_image(coord=None, scale=14, marks=None, theme='light', maptype='map'):
    if coord in [None, []]:
        coord = [37.620070, 55.753630]

    longitude, latitude = coord
    delta = 0.01
    size = "450,450"

    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = '4a7a4d44-c5f2-4f2b-8013-584ec200248d'
    ll_spn = f'&ll={longitude},{latitude}'

    scale_api = f"&z={scale}"
    size_api = f"&size=450,450"
    theme_api = f"&theme={theme}"
    maptype_api = f"&maptype={maptype}"
    lang = f'&lang=ru_RU'

    map_request = f"{server_address}apikey={api_key}{ll_spn}{scale_api}{size_api}{theme_api}{maptype_api}{lang}"
    if marks:
        map_request += f'&pt={'~'.join(marks)}'

    response = requests.get(map_request)

    if response.status_code == 200:
        return response
    else:
        print("Ошибка получения карты", response.status_code, response.text)
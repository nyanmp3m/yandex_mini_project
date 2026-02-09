import requests

def get_image(coords, scale=14):
    api_key = '4a7a4d44-c5f2-4f2b-8013-584ec200248d'
    longitude, latitude = coords
    delta = 0.01
    size = "450,450"

    url = (
        "https://static-maps.yandex.ru/1.x/"
        f"?ll={longitude},{latitude}"
        f"&size={size}"
        f"&z={scale}"
        "&l=map"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response
    else:
        print("Ошибка получения карты", response.status_code)
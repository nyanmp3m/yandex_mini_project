import requests

def get_image(coords):
    api_key = '4a7a4d44-c5f2-4f2b-8013-584ec200248d'
    longitude = 37.620070
    latitude = 55.753630
    delta = 0.01
    size = "450,450"

    url = (
        "https://static-maps.yandex.ru/1.x/"
        f"?ll={longitude},{latitude}"
        f"&size={size}"
        "&z=14"
        "&l=map"
    )

    response = requests.get(url)

    if response.status_code == 200:
        with open("map.png", "wb") as f:
            f.write(response.content)
        print("Карта сохранена как map.png")
    else:
        print("Ошибка получения карты", response.status_code)
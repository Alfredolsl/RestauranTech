from bs4 import BeautifulSoup
import requests

walmart_sections = {"Pan": "panaderia-y-tortilleria/pan-salado/120010_2340027",
                    "Leche" : "lacteos/leche/120006_120096",
                    "Huevos": "lacteos/huevo/120006_120093",
                    "Frutas": "frutas-y-verduras/frutas/120007_120046",
                    "Verduras": "frutas-y-verduras/verduras/120007_120048",
                    "Carnes": "carnes-pescados-y-mariscos/res/120008_740037",
                    "Pescados y Mariscos": "carnes-pescados-y-mariscos/pescados-y-mariscos/120008_120043",
                    "Frutas y Verduras Congeladas": "congelados/frutas-y-verduras-congeladas/120013_120059",
                    }


def get_walmart_items(section: str):
    'returns walmart items and price from a section'
    headers = {'User-Agent': 'Mozilla/5.0'}
    URL = "https://super.walmart.com.mx/content/" + walmart_sections[section]
    response = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    walmart_first_carousel = soup.find_all("span", attrs={"data-automation-id": "product-title"}, limit=6)
    walmart_first_carousel_price = soup.find_all("div", attrs={"class": "mr1 mr2-xl b black lh-copy f5 f4-l"}, limit=6)
    price_to_float = [float(price.get_text().replace("$", "").replace("/kg", "")) for price in walmart_first_carousel_price]

    items_with_prices = [{"name": key.get_text(), "price": price} for key, price in zip(walmart_first_carousel, price_to_float)]
    print(items_with_prices)
    
    return items_with_prices
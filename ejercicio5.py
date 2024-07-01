import requests
from bs4 import BeautifulSoup

def obten_nombre_y_precio(url):

    response =requests.get(url)
    if response.status_code != 200:
        print("Error al acceder a la pagina wed. ")
        return None,None
    
    soup=BeautifulSoup(response.content,"html.parser")

    nombre = soup.find("h1",{"class" : "sc-1x0vz2r-0"})
    if nombre:
        nombre= nombre.text.strip()

    else:
        nombre = "No se pudo encontrar el nombre del producto"
    
    precio = soup.find("span",{"class : sc-ifAKCX"})
    if precio:
        precio=precio.text.strip()
    else:
        precio= "No se pudo encontrar el precio del producto"

    return nombre, precio

url = 'https://www.corotos.com.do/anuncio/vehiculos/carros/mercedes-benz-usado-en-buen-estado-7m2h3e2'

nombre, precio = obten_nombre_y_precio(url)

print(f"nombre del producto: {nombre}")
print(f"precio del producto: {precio}")

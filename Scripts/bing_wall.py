"Script que descarga la imagen del día de Bing"

from datetime import date
import json
import http.client
import urllib.request
import os

# api_url = "https://bing.biturl.top/?resolution=3840&format=json&index=0&mkt=en-US"

conn = http.client.HTTPSConnection("bing.biturl.top")
conn.request("GET", "/?resolution=3840&format=json&index=0&mkt=en-US")
response = conn.getresponse()

data = json.loads(response.read().decode())
image_url = data["url"]
image_desc = data["copyright"]
descrip_limpia = image_desc.split(',')[0].split('(')[0]

nombre_archivo = str(date.today())+".jpg"
ruta_guardado = "/Users/ernesto/Pictures/bing wallpaper/" + nombre_archivo

urllib.request.urlretrieve(image_url, ruta_guardado)

if os.path.exists(ruta_guardado):
    print(f'Imagen descargada correctamente: "{descrip_limpia}"')
else:
    print("Error al descargar la imagen")

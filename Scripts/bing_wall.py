"Script que descarga la imagen del día de Bing"

import json
import http.client
import urllib.request
import os
import re

# api_url = "https://bing.biturl.top/?resolution=3840&format=json&index=0&mkt=en-US"
CARACTERES_NO_VALIDOS = r'[\\/*?:"<>|]'

conn = http.client.HTTPSConnection("bing.biturl.top")
conn.request("GET", "/?resolution=3840&format=json&index=0&mkt=en-US")
response = conn.getresponse()

data = json.loads(response.read().decode())
image_url = data["url"]
image_desc = data["copyright"]
descrip_limpia = image_desc.split(',')[0].split('(')[0]

nombre_archivo = re.sub(CARACTERES_NO_VALIDOS, '-', descrip_limpia)
nombre_archivo = nombre_archivo + ".jpg"
ruta_guardado = "/home/eacarcasses/Pictures/Bing Wallpapers/" + nombre_archivo

if os.path.exists(ruta_guardado):
    print(f'La imagen ya existe: "{descrip_limpia}"')
elif not os.path.exists(ruta_guardado):
    urllib.request.urlretrieve(image_url, ruta_guardado)
    print(f'Imagen descargada correctamente: " {descrip_limpia}"')

import requests
from bs4 import BeautifulSoup as bs

URL_BASE = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

datos_sea = requests.get(URL_BASE)

soup = bs(datos_sea.content, "html.parser")
resultado = soup.find('div', {'id':"info_resultado"})

info = resultado.text.split('\n')

cantidad_proyectos = info[1].split(':')[1].strip()
cantidad_proyectos = int(cantidad_proyectos.replace(',',''))

cantidad_paginas = info[3].split(':')[1].strip()
cantidad_paginas = int(cantidad_paginas.replace(',',''))

print(f"Proyectos: {cantidad_proyectos}, Paginas: {cantidad_paginas}")


# DEV
cantidad_paginas = 10

for pagina in range(cantidad_paginas):
    indice = pagina + 1
    URL_compaginada = f"{URL_BASE}?_paginador_refresh=1&_paginador_fila_actual={indice}"
    print(URL_compaginada)



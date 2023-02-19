import requests
from bs4 import BeautifulSoup as bs

URL_BASE = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

def get_info_resultados():
    info_sea = requests.get(URL_BASE)
    soup = bs(info_sea.content, "html.parser")
    resultado = soup.find('div', {'id':"info_resultado"})

    info = resultado.text.split('\n')

    cantidad_proyectos = info[1].split(':')[1].strip()
    cantidad_proyectos = int(cantidad_proyectos.replace(',',''))

    cantidad_paginas = info[3].split(':')[1].strip()
    cantidad_paginas = int(cantidad_paginas.replace(',',''))
    return cantidad_paginas
    #print(f"Proyectos: {cantidad_proyectos}, Paginas: {cantidad_paginas}")


def get_data_tables(url):
    datos_sea = requests.get(url)
    soup = bs(datos_sea.content, "html.parser")
    tabla = soup.find('table', class_="tabla_datos")
    #tabla = soup.findAll('tbody')
    #tabla = soup.find('table', {'class':"tabla_datos"})
    #tabla = soup.find('table', {'class':"tabla_datos", 'summary':"datos"})
    print(tabla)


# DEV
#cantidad_paginas = get_info_resultados()
cantidad_paginas = 1

for pagina in range(cantidad_paginas):
    indice = pagina + 1
    URL_compaginada = f"{URL_BASE}?_paginador_refresh=1&_paginador_fila_actual={indice}"
    print(URL_compaginada)
    get_data_tables(URL_compaginada)



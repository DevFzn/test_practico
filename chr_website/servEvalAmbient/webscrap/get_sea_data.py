import requests
from bs4 import BeautifulSoup as bs

DEVEL = True
URL_BASE = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
session = requests.Session()

def get_info_resultados():
    """
    Obtiene y retorna cantidad de resultados, crea session válida
    para consultas posteriores.
    """
    info_sea = session.get(URL_BASE)
    soup = bs(info_sea.content, "html.parser")
    resultado = soup.find('div', {'id':"info_resultado"})

    info = resultado.text.split('\n')

    cantidad_proyectos = info[1].split(':')[1].strip()
    cantidad_proyectos = int(cantidad_proyectos.replace(',',''))

    cantidad_paginas = info[3].split(':')[1].strip()
    cantidad_paginas = int(cantidad_paginas.replace(',',''))
    return cantidad_paginas


def get_data_tables(url):
    """
    Retorna el cuerpo de la tabla, requiere de una sesión válida
    para su correcto funcionamiento
    """
    datos_sea = session.get(url)
    soup = bs(datos_sea.content, "html.parser")
    tabla = soup.find('tbody')
    return tabla


cantidad_paginas = get_info_resultados()
if DEVEL:
    cantidad_paginas = 5

for pagina in range(cantidad_paginas):
    indice = pagina + 1
    URL_compaginada = f"{URL_BASE}?_paginador_refresh=1&_paginador_fila_actual={indice}"
    table_data = get_data_tables(URL_compaginada)
    print(table_data)



import requests
from bs4 import BeautifulSoup as bs
import json

DEVEL = True
URL = "https://seia.sea.gob.cl"
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
    cantidad_paginas = 1

for pagina in range(cantidad_paginas):
    indice = pagina + 1
    URL_compaginada = f"{URL_BASE}?_paginador_refresh=1&_paginador_fila_actual={indice}"
    table_data = get_data_tables(URL_compaginada)
    for tabla in table_data.findAll('tr'):
        datos = tabla.findAll('td')
        numero = datos[0].contents[0]
        nombre = str(datos[1].contents[0]).split('title="')[1].split('"')[0]
        tipo = datos[2].contents[0]
        region = datos[3].contents[0]
        tipologia = datos[4].contents[0]
        titular = datos[5].contents[0]
        inversion = datos[6].contents[0]
        fecha = datos[7].contents[0]
        estado = datos[8].contents[0]
        mapa = str(datos[9].contents[0]).split("'")[1]
        mapa = URL+mapa
        print(f"""
                  Nro: {numero}
                  Nombre: {nombre}
                  Tipo: {tipo}
                  Region: {region}
                  Tipologia: {tipologia}
                  Titular: {titular}
                  Inversion: {inversion}
                  Fecha: {fecha}
                  Estado: {estado}
                  Mapa: {mapa}
              """)


import requests
from bs4 import BeautifulSoup as bs
import json

DEVEL = False
URL = "https://seia.sea.gob.cl"
URL_BASE = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
jsonfile = 'datos_sea.json'
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


def crea_new_json(ruta):
    with open(ruta, 'w') as file:
        init_json = []
        file.write(json.dumps(init_json, ensure_ascii=False))


crea_new_json(jsonfile)
for pagina in range(cantidad_paginas):
    print(f'Página: <[[{pagina}]]>')
    indice = pagina + 1
    URL_compaginada = f"{URL_BASE}?_paginador_refresh=1&_paginador_fila_actual={indice}"
    table_data = get_data_tables(URL_compaginada)
    cont=1
    for tabla in table_data.findAll('tr'):
        print(f'Página: [{pagina}] - Fila: {cont}')
        cont+=1
        datos = tabla.findAll('td')
        numero = datos[0].contents[0]
        try:
            nombre = str(datos[1].contents[0]).split('title="')[1].split('"')[0]
        except:
            nombre = str(datos[1].contents[0])
        tipo = datos[2].contents[0]
        region = datos[3].contents[0]
        tipologia = datos[4].contents[0]
        try:
            titular = str(datos[5].contents[0])
        except:
            titular = "N/A"
        inversion = datos[6].contents[0]
        fecha = datos[7].contents[0]
        estado = datos[8].contents[0]
        try:
            mapa = str(datos[9].contents[0]).split("'")[1]
            mapa = URL+mapa
        except Exception:
            mapa = "N/A"
        new_data = {
                'numero':numero,
                'nombre':nombre,
                'tipo':tipo,
                'region':region,
                'tipologia':tipologia,
                'titular':titular,
                'inversion':inversion,
                'fecha':fecha,
                'estado':estado,
                'mapa':mapa
                }
        with open(jsonfile, mode="r+") as file:
            file.seek(0,2)
            pos = file.tell() -1
            file.seek(pos)
            file.write( "{},]".format(json.dumps(new_data, ensure_ascii=False)))

with open(jsonfile, 'r+') as file:
    file.seek(0,2)
    pos = file.tell() -2
    file.seek(pos)
    file.write('] ')


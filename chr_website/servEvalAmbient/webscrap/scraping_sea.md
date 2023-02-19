# WebScrap

[Servicio de evaluación ambiental](https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php)

#### Sección con información relevante para el proceso

```html
<div id="info_resultado">
    Proyectos encontrados: 28,451<br>
    Monto inversión proyectos encontrados: 847.969,240 millones de dólares<br>
    Número de páginas: 2,846
</div>
```

`Páginas: 2,846` y `Proyectos: 28,451`

#### Sección con tabla de datos a extraer

Encabezados de tabla

```html
<thead>
    <tr>
        <th>N<sup>o</sup></th>
        <th>Nombre</th>
        <th>Tipo</th>
        <th>Región</th>
        <th>Tipología</th>
        <th>Titular</th>
        <th>Inversión<br>(MMU$)</th>
        <th>Fecha<br>Presentación<br>Fecha de<br>Ingreso(*)</th>
        <th>Estado</th>
        <th>Mapa</th>
    </tr>
</thead>
```

Número de columnas a mostrar por página `colspan=10`

```html
<tfoot>
    <tr><td colspan="10">&nbsp;</td></tr>
</tfoot>
```

Datos a extraer, ej.

```html
<tbody>
<tr>
    <td>1</td>
    <td>
        <a target="_proyecto"
            href="https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2158390441"
            title="NUEVA SUBESTACIÓN SECCIONADORA LOICA Y NUEVA LÍNEA 2X220 KV LOICA ? PORTEZUELO"
        >NUEVA SUBESTACIÓN SECCIONADORA LOICA Y NUEVA LÍNEA 2X220 KV LOICA ? PORTEZUELO</a>
        <a target="_new"
            href="https://seia.sea.gob.cl/expediente/expediente.php?id_expediente=2158390441&amp;modo=ficha">
            <img src="/images/nuevaVentana.jpg"
                title="Abrir en nueva ventana"
                alt="Abrir en nueva ventana"
                border="0">
        </a>
    </td>
    <td>DIA</td>
    <td>Sexta</td>
    <td align="center">b1</td>
    <td>Colbún S.A.</td>
    <td align="right">31,6785</td>
    <td align="right">17/03/2023</td>
    <td>En Admisión</td>
    <td>
        <a href="#"
            title="Ver en mapa"
            onclick="window.open('/mapa/visualizacion/PuntoRepresentativo/index.php?idExpediente=2158390441', 'mapa')">
            <img src="/template/default/images/html/map-invalid.jpg"
                alt="Ver mapa" border="0">
        </a>
    </td>
</tr>
</tbody>
```

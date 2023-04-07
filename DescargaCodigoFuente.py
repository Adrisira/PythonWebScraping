#Con ese pequeño programa podras descargar el código fuente de cualquier página web.
import urllib.request, urllib.error, urllib.parse

url = 'tu pagina'

respuesta = urllib.request.urlopen(url)
contenidoWeb = respuesta.read().decode('UTF-8')

f = open('nombre.html', "w")
f.write(contenidoWeb)
f.close
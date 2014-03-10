#encoding=utf-8
import requests
import json
provincias = {'1':'Almería','2':'Cádiz','3':'Córdoba','4':'Granada','5':'Huelva','6':'Jaén','7':'Málaga','8':'Sevilla'}
print '''
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
'''

print ''

peticion = raw_input("¿De qué ciudad quieres saber la temperatura actual? ")


respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':' %s ,spain' % provincias[peticion]})


dicc = json.loads(respuesta.text)
temperatura = dicc['main']['temp']
temperatura = round(temperatura - 273)
print 'La temperatura actual de %s es %s grados centígrados' % (provincias[peticion],temperatura)




from geopy.geocoders import Nominatim
import time
import math
import pandas as pd

excel_hospitales = pd.read_excel('C:\\ArchivosExcel\\Ubicación Hospitales\\Direcciones_Hospitales.xlsx')
lista_hospitales = pd.DataFrame(excel_hospitales)
lista_hospital = lista_hospitales['Dirección Hospital'].tolist()
Ubicacion_list = []
Latitud_list = []
Longitud_list = []
Hospital_list = []

for n in lista_hospital:
    print(n)
    geo = Nominatim(user_agent = "Myapp")
    loc = geo.geocode(n, timeout = 15)
    if loc is not None:
        latitude = loc.latitude
        longitude = loc.longitude
    else:
        latitude = longitude = "N/A"
    Hospital_list.append(n)
    Ubicacion_list.append(loc)
    Latitud_list.append(latitude)
    Longitud_list.append(longitude)
    time.sleep(7)

Hospitales_ubicacion = pd.DataFrame()
Hospitales_ubicacion.insert(loc=0, column='Hospital', value = Hospital_list)
Hospitales_ubicacion.insert(loc=1, column='Ubicación', value = Ubicacion_list)
Hospitales_ubicacion.insert(loc=2, column='Latitud', value = Latitud_list)
Hospitales_ubicacion.insert(loc=3, column='Longitud', value = Longitud_list)
print(Hospitales_ubicacion)

Hospitales_ubicacion.to_excel('C:\ArchivosExcel\Hospitales y su ubicación8.xlsx', index=False)
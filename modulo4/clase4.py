import datetime

fecha_hora_actual = datetime.datetime.now()
print("Fecha y hora actual : ",fecha_hora_actual)

#formatear una fecha y hora
formato = "%d/%m/%Y %H:%M:%S"
fecha_formato = fecha_hora_actual.strftime(formato)
print("fecha formateada : ",fecha_formato)

#fecha especifica
fecha_especifica = datetime.datetime(2022,8,12,15,30,0)
print("Fecha y Hora Específica : ",fecha_especifica.strftime(formato))

#calculos con fechas
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=23)
diff_dates = tomorrow - today
print("Mañana es  : ",tomorrow)
print("Faltan ",diff_dates.days)

#zonas horarias
import pytz

zona_horaria = pytz.timezone("America/New_York")
fecha_hora_actual = datetime.datetime.now(zona_horaria)
print("Fecha y hora en New York: ",fecha_hora_actual)

#convertir string a fecha
fecha_string = "2023-07-12 18:30:00"
fecha_objeto = datetime.datetime.strptime(fecha_string,"%Y-%m-%d %H:%M:%S")
print("Fecha y hora convertida",fecha_objeto)
print(type(fecha_objeto))
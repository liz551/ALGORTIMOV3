import urllib2
import json
import os
import ssl
import sys
import json
from datetime import date, datetime
from dbexts import dbexts
from com.ziclix.python.sql import zxJDBC
from pe.edu.upc.algorithm import algorithmService
from pe.edu.upc.repository import MovPatientRepository;


class algorithmServicePython(algorithmService):
    def __init__(self):
        self.value = "Hello from python"

    def getalgorithm(self):
        self.value = "Hola"

        #for length
        d, u, p, v = "jdbc:sqlserver://monitoreoadmin.database.windows.net:1433;database=tp2", "monitoreoadmin", "Admin123","com.mysql.cj.jdbc.Driver"
        db = zxJDBC.connect(d, u, p, v)

        c = db.cursor()
        c2=db.cursor()

        #execute para return de todos los pacientes
        c2.execute("SELECT c.name AS Nombres,c.last_name AS Apellidos,c.dni as DNI, b.ritmo_cardiaco AS RC, b.fecha AS 'Fecha Registro', 'Normal' AS Transtorno, d.Latitud,d.Longitud,0 as Estado FROM [dbo].[mobile_patient] C LEFT JOIN [dbo].[ritmo_cardiaco] B ON C.id=B.patient_id LEFT JOIN ( SELECT * FROM (select ROW_NUMBER() OVER(PARTITION BY patient_id ORDER BY fecha desc) AS particion,latitud,longitud,patient_id,fecha  from [dbo].[ubicacion])AS A WHERE A.PARTICION=1) D ON D.patient_id=c.id WHERE  b.ritmo_cardiaco is not null ")


        xlist=[]
        for x in c2.fetchall():
            xlist.append(x)

        xlistlength= len(xlist)

        #execute para return de 1 paciente

        for k in range (xlistlength):
            c.execute("SELECT c.name AS Nombres,c.last_name AS Apellidos,c.dni as DNI, b.ritmo_cardiaco AS RC, b.fecha AS 'Fecha Registro', 'Normal' AS Transtorno, d.Latitud,d.Longitud,0 as Estado FROM [dbo].[mobile_patient] C LEFT JOIN [dbo].[ritmo_cardiaco] B ON C.id=B.patient_id LEFT JOIN ( SELECT * FROM (select ROW_NUMBER() OVER(PARTITION BY patient_id ORDER BY fecha desc) AS particion,latitud,longitud,patient_id,fecha  from [dbo].[ubicacion])AS A WHERE A.PARTICION=1) D ON D.patient_id=c.id WHERE  b.ritmo_cardiaco is not null and b.fecha not in (SELECT fecha_ritmo FROM [dbo].[emergency]) and b.fecha =(select min(fecha) from [dbo].[ritmo_cardiaco])FOR JSON PATH ")
            d = eval(json.dumps(c.fetchall()))
            d=str(d)[4:-4]
            res = json.loads(d)
            #print res
            data = {
                "Inputs": {
                    "input1":
                        [res]
                },
                "GlobalParameters": {
                },
            }

            body = str.encode(json.dumps(data))
            url = 'https://ussouthcentral.services.azureml.net/workspaces/01de9b04f39d4265ad34f3c605c37538/services/4c9a43648eac4ac58482476e911b1ada/execute?api-version=2.0&format=swagger'
            api_key = '3CK3BNfpvL5W7NBnpE8Y3bmVJfTEj9eSMFLX3jpYSaYLeFP8J8yIpDyqG9/nDbibRjkztLucW5sE6cPBsiALYw=='  # Replace this with the API key for the web service
            headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
            req = urllib2.Request(url, body, headers)
            try:
                response = urllib2.urlopen(req)
                result = response.read()
                json_result = json.loads(result)
                output = json_result["Results"]["output1"][0]
                print ('Ritmo Cardiaco: {}\nResultado: {}'.format(output["RC"],
                                                                            output["Scored Labels"]))
                #c3=db.cursor()
#                 ap=res['Apellidos']
#                 dn=res['DNI']
#                 no=res['Nombres']
#                 ou=output['Scored Labels']
#                 fr=res['Fecha Registro']
#                 rc=res['RC']
#                 la=res['Latitud']
#                 lo=res['Longitud']
                #sql= "INSERT INTO dbo.emergency (apellidos, dni, nombres, transtorno, fecha_ritmo, heart_rate, latitude, lenght) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
                #val= (res['Apellidos'], res['DNI'], res['Nombres'], output['Scored Labels'], res['Fecha Registro'], res['RC'], res['Latitud'], res['Longitud'])
                #c3.execute(sql,val)
                #db.commit()
                #smt = "insert into dbo.emergency values (?,?,?,?,?,?,?,?,?)"

                #result = c3.executemany(smt,[1,'Lopez',78496785,'Juan','Normal', 0,100,1,1])
                #c3.execute("insert into dbo.emergency (apellidos, dni, nombres, transtorno, fecha_ritmo, heart_rate) values (Lopez,78496785,Juan,Normal,12/10/21,100)")


            except urllib2.HTTPError as error:
                print("The request failed with status code: " + str(error.code))

                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())
                print(json.loads(error.read()))







        

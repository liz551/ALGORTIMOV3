import urllib2
import json
import os
import ssl
import sys
import json

from com.ziclix.python.sql import zxJDBC
from pe.edu.upc.algorithm import algorithmService
from pe.edu.upc.repository import EmergencyRepository;
from pe.edu.upc.repository import MovPatientRepository;


class algorithmServicePython(algorithmService):
    def __init__(self):
        self.value = "Hello from python"

    def getalgorithm(self):
        self.value = "Hola"
        d, u, p, v = "jdbc:sqlserver://monitoreoadmin.database.windows.net:1433;database=tp2", "monitoreoadmin", "Admin123","com.mysql.cj.jdbc.Driver"
        db = zxJDBC.connect(d, u, p, v)

        c = db.cursor()
        c.execute("SELECT 101246 AS HC,c.name AS Nombres,c.last_name AS Apellidos,c.dni as DNI, b.ritmo_cardiaco AS RC, b.fecha AS 'Fecha Registro', 'Normal' AS Transtorno FROM [dbo].[mobile_patient] C LEFT JOIN [dbo].[ritmo_cardiaco] B ON C.id=B.patient_id WHERE b.ritmo_cardiaco is not null FOR JSON PATH")

        #print(c.fetchall())

        #for usuario in usuarios:
        #    print usuario

        #json_output = []
        #for a in c.fetchall():
        #    print a


            #json_output.append(a)

        #jsonx= str.encode(json.dumps(json_output,indent=4, sort_keys=True, default=str))
        #print(json_output)
        #print(json_output)
        #print c.description
        d = eval(json.dumps(c.fetchall()))
        d=str(d)[4:-4]
        res = json.loads(d)
        print res
        data = {
            "Inputs": {
                "input1":
                    [{
                            'Nombres': "Pepito",
                            'Apellidos': "Quispe",
                            'DNI': "70657000",
                            'RC': "70",   
                            'Fecha Registro': "27/05/2015",
                            'Transtorno': "Bradicardia",
                            'Latitud': '',
                            'Longitud': '',
                            'Estado': ''
                    }]
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
            return ('Ritmo Cardiaco: {}\nResultado: {}'.format(output["RC"],
                                                                           output["Scored Labels"]))
        except urllib2.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read()))






        

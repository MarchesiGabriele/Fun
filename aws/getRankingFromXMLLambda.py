
# API GATEWAY: https://8ns7c5iggh.execute-api.us-east-1.amazonaws.com/results

# GET request

# Headers: 1) "race_id", 2) "categoria"


import json
import xml.etree.ElementTree as ET
import boto3
import botocore


BUCKET_NAME = "testracesbucket"
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    try:
        classifica = []
        
        ##
        ### Recupero Headers
        ##
        
        # id della gara, corrispondente al nome del file xml nel bucket
        race_id_header = event["headers"]["race_id"] 
        # categoria di cui voglio la  classifica
        categoria_header = event["headers"]["categoria"]
        
        race_id_header = race_id_header + ".xml"
        
        
        ##
        ### Recupero File XML 
        ##

        # Creo oggetto bucket prendendo il file indicato nella header
        s3obj = s3.Object(BUCKET_NAME, race_id_header)
        
        # Leggo string dell' xml dal bucket
        xmlstring = s3obj.get()['Body'].read()
        
        # Genero albero xml
        xml = ET.fromstring(xmlstring)
        
        
        ##
        ### Recupero elementi della cateogoria desiderata
        ##
        
        # Id
        ids = xml.findall("./ClassResult/Class[Name ='" + categoria_header +  "']/../PersonResult/Person/Id")
       
        # Nome
        names = xml.findall("./ClassResult/Class[Name ='" + categoria_header +  "']/../PersonResult/Person/Name/Family")
        
        # Cognome
        surnames = xml.findall("./ClassResult/Class[Name ='" + categoria_header +  "']/../PersonResult/Person/Name/Given")
        
        # Time  Behind
        timeBehind = xml.findall("./ClassResult/Class[Name ='" + categoria_header +  "']/../PersonResult/Result/TimeBehind")
       
        # Time
        time = xml.findall("./ClassResult/Class[Name ='" + categoria_header +  "']/../PersonResult/Result/Time")
       
       
       
        for x in range(len(ids)):
            # per il primo giocatore mostro il time e non il timeBehind che tanto sarebbe sempre 0
            if x == 0:
                classifica.append({
                    "rank": x+1,
                    "id": ids[x].text,
                    "name" : names[x].text,
                    "surname" : surnames[x].text,
                    "time" : time[x].text
                })
                continue
            
            classifica.append({
                "rank": x+1,
                "id": ids[x].text,
                "name" : names[x].text,
                "surname" : surnames[x].text,
                "timeBehind" : timeBehind[x].text
            })

        return {
            'statusCode': 200,
            'body': json.dumps(classifica)
        }
        
        
    except s3.meta.client.exceptions.NoSuchKey:    
        return {
            'statusCode': 404,
            'body': json.dumps("hsahus:")
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 404,
            'body': json.dumps(str(e))
        }



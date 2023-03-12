import json
import boto3
import urllib.request
from datetime import datetime


def downloadHTML(url):

    respuesta = urllib.request.urlopen(url)
    contenidoWeb = respuesta.read().decode('UTF-8')

    return contenidoWeb


def f(event, context):

    url = 'https://casas.mitula.com.co/searchRE/tipo-Casa/q-Chapinero--Bogota'

    contenidoWeb = downloadHTML(url)

    date = datetime.now()

    client = boto3.client("s3")
    client.put_object(Body=contenidoWeb, Bucket="raw-casas",
                      Key=f'landing-casas-{date.strftime("%Y-%m-%d")}.html')

    return {
        'statusCode': 201,
        'body': json.dumps("Data scrapped successfully :3.")
    }

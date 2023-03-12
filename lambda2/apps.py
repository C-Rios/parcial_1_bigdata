import json
import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def beautiful_soup_parse(body):

    soup = BeautifulSoup(body, features="html.parser")

    data = soup.find_all('div',
                         attrs={'class': 'listing-card__information-main'})
    return data


def csv_parse(body, date):

    data = beautiful_soup_parse(body=body)

    csv_acum = "FechaDescarga, Valor, NumHabitaciones, NumBanos, mts2\n"

    words = ["habitaciones", "baños", "m²"]

    for element in data:
        matches = element.find_all('span')

        price = element.find_all('div',
                                 attrs={'class': 'price'})[0].contents[0]
        csv_acum += "{},".format(date.strftime("%Y-%m-%d"))
        price = price.replace("Price", "")
        csv_acum += "{},".format(price.replace("$", "").strip())

        for i in range(3):
            try:
                coincidence = matches[i].contents[0]
            except IndexError:
                coincidence = ""

            if words[i] in coincidence:
                csv_acum += coincidence.replace(words[i], "").strip()
            else:
                csv_acum += "-"

            if i != 2:
                csv_acum += ","

        csv_acum += "\n"

        """
        if missing == 3:
            csv_acum = csv_acum[:-5]
        else:
            csv_acum += "\n"
        """
    return csv_acum


def f(event, context):

    date = datetime.now()

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('raw-casas')
    obj = bucket.Object(f'landing-casas-{date.strftime("%Y-%m-%d")}.html')
    body = obj.get()['Body'].read()

    csv_acum = csv_parse(body=body, date=date)

    client = boto3.client('s3')
    client.put_object(Body=csv_acum, Bucket="processed-casas",
                      Key=f'casas-final-{date.strftime("%Y-%m-%d")}.csv')

    return {
        'statusCode': 201,
        'body': json.dumps("Processing done :)")
    }

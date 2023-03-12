import unittest
from apps import csv_parse, beautiful_soup_parse
from datetime import datetime


class Test_processing(unittest.TestCase):
    def test_beautiful_soup_parse(self):
        html_doc = """
        <html>
            <head>
                <title>Test Page</title>
            </head>
            <body>
                <h1>Test Heading</h1>
                <p>Test Paragraph</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <div class=
                    "listing-card__information-main">
                        <div class="listing-card__title"
                         content="Casa En Venta En Bogotá Bosque
                         Calderón">Casa En Venta En Bogotá Bosque
                         Calderón</div>
                        <div class="listing-card__price-wrapper">
                            <div class="price">$ 950.000.000</div>
                        </div>
                        <div class="listing-card__location">Bogotá,
                        Bogotá</div>
                        <div class="listing-card__properties">
                        <div class="listing-card__property">
                        <div class="card-icon card-icon__bedrooms"></div>
                            <span content="5">5 habitaciones</span>
                        </div>
                        <div class="listing-card__property">
                        <div class="card-icon card-icon__bathrooms"></div>
                            <span content="3">3 baños</span>
                        </div>
                        <div class="listing-card__property">
                        <div class="card-icon card-icon__area"></div>
                        <span>298 m²</span>
                        </div>
                    </div>
                </ul>
            </body>
        </html>
        """

        result = beautiful_soup_parse(html_doc)

        self.assertTrue(len(result) > 0)

        html_doc = """
        <html>
            <head>
                <title>Test Page</title>
            </head>
            <body>
                <div class=
                "listing-card__information-main">
                    <div class="listing-card__title"
                    content="Vendo Casa En Chapinero,
                    Bogota">Vendo Casa En Chapinero,
                    Bogota</div>
                        <div class="listing-card__price-wrapper">
                        <div class="price">$ 950.000.000</div>
                    </div>
                    <div class="listing-card__location">Bogotá, Bogotá</div>
                    <div class="listing-card__properties">
                    <div class="listing-card__property">
                        <div class="card-icon card-icon__bedrooms"></div>
                        <span content="7">7 habitaciones</span>
                    </div>
                    <div class="listing-card__property">
                    <div class="card-icon card-icon__bathrooms"></div>
                        <span content="4">4 baños</span>
                    </div>
                    <div class="listing-card__property">
                    <div class="card-icon card-icon__area"></div>
                        <span>360 m²</span>
                    </div>
                    </div>
                    <div class="listing-card__description"
                    content="Espectacular Casa comercial en venta,
                    situada en el barrio Chapinero, de interés cultural,
                    con una excelente posición privilegiada dentro de la
                    misma ciudad,con un fácil acceso a cualquier necesidad.
                    Casa de habitación de dos pisos construida con muros de
                    ladrillos y cubierta con teja de Eternit, antejardín,
                    patio y jardines interiores. PRIMER PISO  3 salones amplios
                    Cocina y Deposito 2 baños 1 estar para recepción Patio
                    interior Garaje           Jardín exterior SEGUNDO PISO 
                    3 salones amplios 1 salón de juntas           2 baños
                    USOS:HOGAR GERIATRICOJARDIN
                    INFANTILRESTAURANTEOFICINASCLINICA">
                    Espectacular Casa comercial en venta, situada en el barrio
                    <b>Chapinero</b>, de interés cultural, con una excelente
                    posición privilegiada dentro de la misma ciudad.</div>
                </div>
                <h1>Test Heading</h1>
                <p>Test Paragraph</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
        </html>
        """

        result = beautiful_soup_parse(html_doc)

        self.assertTrue(len(result) > 0)

        html_doc = """
        <html>
            <head>
                <title>Test Page</title>
            </head>
            <body>
                <h1>Test Heading</h1>
                <p>Test Paragraph</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
                <div class=
                "listing-card__information-main">
                    <div class="listing-card__title"
                    content="Venta De Casas En Bogota">
                    Venta De Casas En Bogota</div>
                        <div class="listing-card__price-wrapper">
                        <div class="price">$ 690.000.000</div>
                    </div>
                    <div class="listing-card__location">Bogotá, Bogotá</div>
                    <div class="listing-card__properties">
                    <div class="listing-card__property">
                    <div class="card-icon card-icon__bedrooms"></div>
                        <span content="8">8 habitaciones</span>
                    </div>
                    <div class="listing-card__property">
                    <div class="card-icon card-icon__bathrooms"></div>
                        <span content="6">6 baños</span>
                    </div>
                    <div class="listing-card__property">
                    <div class="card-icon card-icon__area"></div>
                        <span>247 m²</span>
                    </div>
                    </div>
                    <div class="listing-card__description"
                    content="Casa para remodelar Chapinero de 2 niveles amplia.
                    Primer nivel consta: 2 apartaestudios, 2 cuartos, baño ,
                    sala comedor, cocina, patio de ropas; 2 nivel: garaje para
                    2 carros, 4 alcobas, 3 baños, patio de ropas, cocina
                    integral. Lugares o barrios cercanos: Cra 24 con 63,
                    parque Lourdes, El Campin, 7 de Agosto.">Casa para
                    remodelar<b>Chapinero</b> de 2 niveles amplia.</div>
                </div>
            </body>
        </html>
        """

        result = beautiful_soup_parse(html_doc)

        self.assertTrue(len(result) > 0)

    def test_csv_parse(self):

        with open("web_file_test.html", "r") as archivo:
            csv_data = archivo.read()

        date = "2023-03-12"
        date = datetime.strptime(date, '%Y-%m-%d')

        result = csv_parse(csv_data, datetime.now())

        expected = "FechaDescarga, Valor, NumHabitaciones, NumBanos, mts2\n2023-03-12,950.000.000,5,3,298\n2023-03-12,8.000.000.000,3,5,594\n2023-03-12,260.000.000,3,3,100\n2023-03-12,1.600.000.000,3,4,267\n2023-03-12,690.000.000,8,6,247\n2023-03-12,520.000.000,-,2,68\n2023-03-12,950.000.000,7,4,360\n2023-03-12,1.400.000.000,-,-,-\n2023-03-12,871.000.000,6,5,450\n2023-03-12,1.360.000.000,3,4,172\n2023-03-12,1.100.000,12,8,-\n2023-03-12,2.850.000.000,13,13,500\n2023-03-12,2.250.000.000,3,5,180\n2023-03-12,5.000.000.000,4,9,851\n2023-03-12,1.600.000.000,4,4,334\n2023-03-12,3.500.000.000,4,5,530\n2023-03-12,1.200.000.000,4,3,250\n2023-03-12,17.000.000.000,3,4,843\n2023-03-12,1.150.000.000,3,3,197\n2023-03-12,780.000.000,7,4,221\n2023-03-12,3.300.000.000,10,-,-\n2023-03-12,1.695.000.000,4,4,334\n2023-03-12,1.471.000.000,6,3,248\n2023-03-12,511.915.856,25,6,134\n2023-03-12,841.680.000,6,4,448\n"
        """
        expected = ("FechaDescarga, Valor, NumHabitaciones, NumBanos, mts2\n"
                    "2023-03-12,950.000.000,5,3,298\n"
                    "2023-03-12,8.000.000.000,3,5,594\n"
                    "2023-03-12,260.000.000,3,3,100\n"
                    "2023-03-12,1.600.000.000,3,4,267\n"
                    "2023-03-12,690.000.000,8,6,247\n"
                    "2023-03-12,520.000.000,-,2,68\n"
                    "2023-03-12,950.000.000,7,4,360\n"
                    "2023-03-12,1.400.000.000,-,-,-\n"
                    "2023-03-12,871.000.000,6,5,450\n"
                    "2023-03-12,1.360.000.000,3,4,172\n"
                    "2023-03-12,1.100.000,12,8,-\n"
                    "2023-03-12,2.850.000.000,13,13,500\n"
                    "2023-03-12,2.250.000.000,3,5,180\n"
                    "2023-03-12,5.000.000.000,4,9,851\n"
                    "2023-03-12,1.600.000.000,4,4,3342,8,\n"
                    "2023-03-12,3.500.000.000,4,5,530\n"
                    "2023-03-12,1.200.000.000,4,3,250\n"
                    "2023-03-12,17.000.000.000,3,4,843\n"
                    "2023-03-12,1.150.000.000,3,3,197\n"
                    "2023-03-12,780.000.000,7,4,221\n"
                    "2023-03-12,3.300.000.000,10,-,-\n"
                    "2023-03-12,1.695.000.000,4,4,334\n"
                    "2023-03-12,1.471.000.000,6,3,248\n"
                    "2023-03-12,511.915.856,25,6,134\n"
                    "2023-03-12,841.680.000,6,4,448\n")
        """
        self.assertEqual(result, expected)

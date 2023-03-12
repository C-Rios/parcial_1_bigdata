# Parcial 1 – Big Data e Ingeniería de Datos

 

Universidad Sergio Arboleda

 

Escuela de Ciencias Exactas e Ingeniería

 

Ingeniería en Ciencias de la Computación e Inteligencia Artificial



Big Data e Ingeniería de Datos



**Presentan: Juan Camilo De Los Ríos Hernández y Roxanyffer Andreina Velasco Contreras**

 

## Introducción

Bajo la premisa del proceso realizado se utiliza AWS Lambda y Zappa para crear dos funciones que automatizan la descarga y procesamiento de información de la venta de casas en el sector de Chapinero desde la página web de Mitula. La primera función mencionada se ejecuta todos los lunes a las 9 am y realiza el proceso de descarga de la primera página de resultados en un archivo HTML, que se guarda en un bucket de S3 con un formato específico. La segunda función a la que se hace referencia se dispara cuando se agrega el archivo HTML al bucket, y utiliza Beautiful Soup para extraer la información de cada casa y crear un archivo CSV en otro bucket de S3.

Por otro lado, cabe mencionar que el proceso utiliza pruebas unitarias con pytest y un mock para probar la función de descarga, y se integra con GitHubActions para realizar una revisión de código limpio con flake8, ejecutar pruebas unitarias y desplegar automáticamente en AWS cuando se hace un push o pull request.

El proceso realizado según lo anterior proporciona una forma automatizada y eficiente de descargar y procesa información importante de la venta de casas en un área específica, lo que puede ser de gran utilidad para aquellos interesados en el mercado inmobiliario en el sector de Chapinero.

 

## Desarrollo

El proceso realizado en esta oportunidad es un ejemplo de cómo se pueden utilizar tecnologías en la nube para automatizar tareas de descarga y procesamiento de datos. En este caso específico, utilizando AWS Lambda y Zappa para crear dos funciones que permiten descargar y procesar información de venta de casas en el sector de Chapinero desde la página web de Mitula.

La utilización de tecnologías en la nube permite crear soluciones escalables y flexibles que se adaptan a las necesidades de cada usuario y organización. En este caso, se utilizó AWS Lambda, un servicio de computación sin servidor que permite ejecutar código en la nube sin la preocupación por la administración de servidores. Esto permite reducir costos y mejorar la eficiencia al no tener como preocupación la infraestructura subyacente.

Por otro lado, se ha utilizado Zappa, un marco de trabajo que permite desplegar las funciones de AWS Lambda de manera sencilla, rápida y eficiente. Lo anterior, partiendo del hecho de que Zappa permite crear y mantener dichas funciones de manera eficiente, de igual manera permitiendo integrar otras herramientas, como GitHubActions y pruebas unitarias.

En resumen, el proceso descrito es un ejemplo de cómo se pueden utilizar tecnologías en la nube para automatizar tareas de descarga y procesamiento de datos. La utilización de servicios como AWS Lambda y Zappa permite crear soluciones escalables, flexibles y altamente disponibles que se adaptan a las necesidades de cada usuario y organización.

 

## Conclusión

En la actualidad, la automatización de procesos es una herramienta clave en la eficiencia y la productividad de las empresas y organizaciones. En el caso específico del proceso que se ha realizado, se destacan los múltiples beneficios para los interesados en el mercado inmobiliario en el sector de Chapinero, como el acceso a información actualizada de manera automatizada, la reducción del tiempo y esfuerzo en la obtención de información y la posibilidad de tomar decisiones más informadas basadas en datos reales y precisos.

En conclusión, la automatización de procesos es una herramienta clave en la eficiencia y la productividad de las empresas. Como se evidenció en este caso, resulta en una solución escalable, flexible y altamente disponible que puede ser adaptada a las necesidades de distintos usuarios. Teniendo en cuenta y como se ha mencionado anteriormente, que la integración con otras tecnologías, como pruebas unitarias y GitHubActions, permite una mayor automatización del proceso y reduce la necesidad de intervención manual, lo que puede ahorrar tiempo y reducir errores.

 

Descripción repositorio:

 

Este repositorio contiene un proyecto de automatización de la descarga y procesamiento de información de venta de casas en el sector de Chapinero en Colombia desde la página web de Mitula. Lo anterior, utilizando AWS Lambda y Zappa para crear dos funciones Lambda que se ejecutan automáticamente todos los lunes a las 9 a.m. La primera función Lambda descarga la primera página de resultados de Mitula y guarda el archivo HTML en un bucket S3; mientras que la segunda procesa el archivo HTML utilizando BeautifulSoup y extrae información de cada casa en la página, creando un archivo CSV con la información de cada propiedad. Dicho proyecto incluye pruebas unitarias utilizando pytest y un mock para probar la función de descarga. Además, se creó un pipeline de despliegue continuo con GitHubActions que incluye la revisión de código limpio con flake8, la ejecución de pruebas unitarias y el despliegue automático en AWS.
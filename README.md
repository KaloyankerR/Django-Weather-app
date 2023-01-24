# Weather app
Displays the weather temperatures in different cities and saves the information.<br>
The user can add and delete cities from the home page.<br>
You can't add cities, which are already in the list or don't exists.
A message is displayed, when a city is successfully added and when an error occures.

<!-- ABOUT THE PROJECT -->
## About The Project
![Product Name Screen Shot][product-screenshot]

### Built With
* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Jinja][Jinja]][Jinja-url]

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Installation
1. Get a free API Key at [https://openweathermap.org](https://openweathermap.org/api)
2. Clone the repo
   ```sh
   git clone https://github.com/KaloyankerR/Django-Weather-app.git 
   ```
3. Install Django
   ```sh
   pip install django
   ```
4. Enter your API in `./weather/base/views.py`
   ```js
   api_key = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->
## Usage
This project can be used to monitor the temperature in different cities.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
I've included a few of my favorites to kick things off!

* [Dennis Ivanov's website](https://www.dennisivy.com/)
* [Django's documentation](https://docs.djangoproject.com/en/4.1/)
* [Jinja's documentation](https://jinja.palletsprojects.com/en/3.1.x/)
* [W3schools tutorial on Django](https://www.w3schools.com/django/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: ./screenshot.PNG
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[Jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/

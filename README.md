
## Django Weather App
This Django project allows users to view the current weather of various cities using the OpenWeatherMap API. Users can register, log in, add cities to their list, and view the weather information for those cities.

## Installation
Clone the repository:

git [clone https://github.com/your-username/django-weather-app.git](https://github.com/AarugulaVarahalu/Weather-Tracking-App/tree/main)

Install the required dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver

Access the application at http://127.0.0.1:8000/.

## Usage
Register a new account by accessing the registration page (/register) and filling out the registration form.

Log in to your account by accessing the login page (/login) and providing your username and password.

## Project Structure
views.py: Contains the views for rendering HTML templates and handling user requests.

models.py: Defines the database models for storing city and historical weather data.

forms.py: Defines forms for user authentication and registration.

urls.py: Defines URL patterns for routing user requests to appropriate views.

weather.html: HTML template for displaying weather information and allowing users to add or delete cities.

register.html: HTML template for user registration.

login.html: HTML template for user login.

## Contributing
Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.









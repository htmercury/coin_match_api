# Coin Match API

Thank you for using the coin match api. This api can be used to compare prices for various cryptocurrencies across several platforms for the purposes of price analysis, research, and logging. Coin match can also be used to compare one exchange to another, and display whatever currencies are available on those exchanges.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python3+
virtualenv
pip
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the respository to your local environment

```
git clone https://github.com/htmercury/coin_match_api.git
```

Move into the git directory

```
cd coin_match_api
```
Initialize a virtual environment
```
virtualenv djangoPy3Env
```
Activate the virtual environment
```
Windows: call djangoPy3Env/Scripts/activate
Mac/Linux: source djangoPy3Env/bin/activate
```
Install the required packages
```
pip install -r requirements.txt
```
Move into the project directory
```
cd coin_match
```
Start the django server
```
python manage.py runserver
```

Final Output:
```
Performing system checks...

System check identified no issues (0 silenced).
July 26, 2018 - 14:43:49
Django version 1.10, using settings 'coin_match.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Running the Tests

In the project folder ```coin_match_api/coin_match```,
run ```python manage.py test``` to run the given unit tests

### Break Down End to End Tests

Explain what these tests test and why

```
Give an example
```

## Deployment

This app will be deployed from github using EC2 and the Amazon Web Server. We will not be using heroku for our deployment.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](www.django-rest-framework.org/) - The api framework used
* [Python](https://www.python.org/) - Used to write logic code
* [jQuery](https://jquery.com/) - Used for diaplsy functions
* [JavaScript](JavaScript.com) - Assists in frontend display

## Contributing

Please read [CONTRIBUTING.md](https://github.com/htmercury/coin_match_api/wiki/Contributing) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ka Wong** - *Unit testing, serializers, database design - django models.* - [HTMercury](https://github.com/htmercury/)
* **Zach Verghese** - *Logical data operations and validation - django views.* - [ZachVerghese](https://github.com/zachverghese)
* **Tom Kane** - *Front and back end integration, documentation - django templates.* - [Tsk339](https://github.com/tsk339)

See also the list of [contributors](https://github.com/htmercury/coin_match_api/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgements

* Hat tip to slate API documentation boiler plate

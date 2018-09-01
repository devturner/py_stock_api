stock_api
=========
 A restful stock portfolio API that runs on python Pyramid and is hosted on AWS EC2.

 End goal: an app that consumes data from a 3rd party API and provides our users with the ability to create stock portfolios. Once we’ve built the basic functionality of the application, we’ll introduce data science, visualizations, and machine learning into the application so we can analyze and make basic predictions based on historical data!

Modules
---------------
Python 3.7
Pryamid
Response
marshmallow
SQLAlchemy
cryptacular
pytest
postgresQL


Getting Started
---------------

- Run this project locally:
    - build a stock_api database with postgres
    - start the env:
        pipenv shell
    - build out the app / db:
        initialize_py_stock_api_db development.ini
    - start the app:
        pserve development.ini --reload


Endpoints
---------------

- GET / - the base API route

- POST /api/v1/auth/register/
    - register a new account or logging in, with the post body in the form:
    {"email": "email@email.com", "password": "password"}

- POST /api/v1/portfolio/{id}/
    - for creating a user's portfolio associated with their account, with post body in the form:
    {"name": "My Portfolio"}

- POST /api/v1/stock/
    - for creating a new company record associated with a specified portfolio, with post body in the form:
{"symbol": "aapl", "portfolio_id": 1}

- GET /api/v1/portfolio/{id}/
    - for retrieving a user's portfolio

- GET /api/v1/stock/{id}/
    - for retrieving a companies information
- DELETE /api/v1/stock/{id}
    - for deleting a company record
- GET /api/v1/company/{symbol}
    - for retrieving company detail from 3rd party API, where
    {symbol} is variable

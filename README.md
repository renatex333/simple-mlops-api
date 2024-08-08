# Simple API for Machine Learning Predictions

This is a simple API project that provides a machine learning model to make predictions based on user input data. The API uses the FastAPI framework and authentication via a simple token.

## Installing Dependencies

To install the project dependencies, use the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Project Structure

- `models`: Contains the machine learning models and encoders.
- `src`: Contains the main source code of the API.
- `test`: Contains the API tests.
- `data`: Contains the data used by the model.

## Starting the API

To start the API, run the following command:

```sh
uvicorn src.main:app --host 0.0.0.0 --port 8900 --workers 1
```

## Running the Tests

To run the tests, use the following command:

```sh
python test/test_api.py
```

The unit tests verify the API responses to ensure everything is functioning correctly.
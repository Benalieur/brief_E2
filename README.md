# Real Estate Price Prediction Web App

![Real Estate Price Prediction](https://github.com/charles-42/E2_P3/blob/develop/data/screenshot.png)

## Project Description

This Django web app aims at predicting real estate prices based on house features. It provides a very basic user interface for users to input house features and get an estimated price for the property. The prediction model is trained on a dataset of real estate sales, incorporating various factors like location, area, number of rooms, etc., to make accurate predictions.

## Usage

To run the web app locally, follow these steps:

1. Change into the project directory:
```bash
cd real_estate_app
```

2. Build the Docker image for the Django app:

```bash
docker build -t django-app .
```

3. Run the Docker container with port mapping and volume mounting:

```bash
docker run -dp 8000:8000 -v "$PWD":/app django-app
```

The app will be accessible at http://0.0.0.0:8000/ in your web browser. You can now start using the app to predict real estate prices based on different house features.

# brief_E2

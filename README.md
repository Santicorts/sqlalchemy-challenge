# sqlalchemy-challenge

---

# SQLAlchemy Challenge - SurfsUp

This project is a SQLAlchemy challenge to analyze climate data using SQLAlchemy ORM and Flask API.

## Table of Contents

- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [License](#license)

## Project Description

The objective of this project is to analyze climate data using SQLAlchemy ORM and Flask API. The project includes a set of routes to query a SQLite database and return climate information in JSON format. This challenge involves:
- Setting up a SQLAlchemy engine to connect to an SQLite database.
- Reflecting tables into a new model using SQLAlchemy ORM.
- Creating a Flask application with multiple routes to query and return climate data.

## Project Structure

The project directory structure is as follows:

```
sqlalchemy-challenge/
├── Resources/
│   ├── hawaii_measurements.csv
│   ├── hawaii_stations.csv
│   └── hawaii.sqlite
├── SurfsUp/
│   ├── app.py
│   ├── climate_starter.ipynb
├── README.md
└── .gitignore
```

- **Resources/**: Contains the data files used in this challenge.
- **SurfsUp/**: Contains the main scripts for the analysis.
  - **app.py**: The Flask application file.
  - **climate_starter.ipynb**: Jupyter notebook for data analysis.
- **README.md**: Project documentation.
- **.gitignore**: Specifies files and directories to ignore in git repository.

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/<your-username>/sqlalchemy-challenge.git
    cd sqlalchemy-challenge
    ```

2. **Set up a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:
    ```sh
    export FLASK_APP=SurfsUp/app.py
    flask run
    ```

## API Endpoints

The following API endpoints are available:

1. **/** - List all available API routes.
    - Example: `http://127.0.0.1:5000/`

2. **/api/v1.0/precipitation** - Return a JSON list of precipitation data.
    - Example: `http://127.0.0.1:5000/api/v1.0/precipitation`

3. **/api/v1.0/stations** - Return a JSON list of weather stations.
    - Example: `http://127.0.0.1:5000/api/v1.0/stations`

4. **/api/v1.0/tobs** - Return a JSON list of temperature observations for the previous year.
    - Example: `http://127.0.0.1:5000/api/v1.0/tobs`

5. **/api/v1.0/<start>** - Return a JSON list of the minimum, average, and maximum temperatures for dates greater than or equal to the start date.
    - Example: `http://127.0.0.1:5000/api/v1.0/2017-01-01`

6. **/api/v1.0/<start>/<end>** - Return a JSON list of the minimum, average, and maximum temperatures for dates between the start and end dates (inclusive).
    - Example: `http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31`

## Usage

1. **Querying Precipitation Data**:
    Access `http://127.0.0.1:5000/api/v1.0/precipitation` to retrieve precipitation data in JSON format.

2. **Querying Station Data**:
    Access `http://127.0.0.1:5000/api/v1.0/stations` to retrieve a list of weather stations in JSON format.

3. **Querying Temperature Observations**:
    Access `http://127.0.0.1:5000/api/v1.0/tobs` to retrieve temperature observations for the previous year in JSON format.

4. **Querying Temperature Statistics**:
    Access `http://127.0.0.1:5000/api/v1.0/<start>` to retrieve temperature statistics from the start date onwards in JSON format.
    Access `http://127.0.0.1:5000/api/v1.0/<start>/<end>` to retrieve temperature statistics between the start and end dates (inclusive) in JSON format.


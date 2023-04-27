

# Flask Car Shop Application

This is a school project that utilizes Flask and Python to create a web application for a car shop. This application is designed to support purchasing a multitude of vehicles and utilizes sqlite3 for data storage. 

## Requirements

To run this Flask application, you will need the following:

* Python 3.x
* Flask
* sqlite3

## Installation

1. Clone this repository using the following command:
```
git clone https://github.com/your-username/flask-car-shop.git
```

2. Navigate to the project directory:
```
cd flask-car-shop
```

3. Create a virtual environment:
```
python3 -m venv env
```

4. Activate the virtual environment:
```
source env/bin/activate
```

5. Install the required packages:
```
pip install -r requirements.txt
```

6. Create the database:
```
python create_db.py
```

7. Run the application:
```
flask run
```

## Usage

Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser.

## Features

The following features are currently implemented in the application:

* Browse all available cars
* Search for a specific car
* Add a car to the cart
* View the cart
* Checkout the cart and make a purchase

## Contributing

Contributions are welcome! If you find any bugs or would like to add a new feature, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

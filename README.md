

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
git clone https://github.com/clackroe/GroupProj-3135
```

2. Navigate to the project directory:
```
cd GroupProj-3135
```

3. Create a virtual environment (optional):
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
bash setup.bash
```

7. Run the application:
```
bash run.sh
```

## Usage

Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser.

## Features

The following features are currently implemented in the application:

* Browse all available cars
* Search for a specific car
* Add a car to the cart
* Checkout the cart and make a purchase

*Checkout the Admin tools with an admin account!

## Contributing

Contributions are welcome! If you find any bugs or would like to add a new feature, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

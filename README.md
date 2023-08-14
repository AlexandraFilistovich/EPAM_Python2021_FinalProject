# EPAM Python 2022 final project - Market App



## How to build this project:


- ### Navigate to the project root folder

- ### Install the requirements:
```
pip install -r requirements.txt
```

- ### Install the app:
```
sudo python3 setup.py install
```

- ### Run migrations to create database infrastructure:
```
export FLASK_APP=execute.py
flask db upgrade
```

- ### Optionally populate the database with sample data
```
python3 populate.py
```

- ### Run the project locally:
```
python3 -m flask run
```

## Now you should be able to access the web service and web application on the following addresses:

- ### Web Service:
```
localhost:5000/home
localhost:5000/market

localhost:5000/login
localhost:5000/registration
```
### (Password from test_user: qwerty1)

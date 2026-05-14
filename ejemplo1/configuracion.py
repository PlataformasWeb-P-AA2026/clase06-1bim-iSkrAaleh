from sqlalchemy import create_engine
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

#engine = create_engine('sqlite:///demobase.db', echo=True)

# mysql
# pip install mysql-connector-python
#engine = create_engine("mysql+mysqlconnector://user:password@localhost:3310/demo100")

# postgres
# sudo apt install libpq-dev
# pip install psycopg2
engine = create_engine("postgresql+psycopg2://user:password@localhost:5435/demo100")
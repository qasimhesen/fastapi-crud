from decouple import config

DB_USER = config("DB_USER") 
DB_PASSWORD = config("DB_PASSWORD")
DB_SERVER= config("DB_SERVER") 
DB_NAME = config("DB_USER")


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
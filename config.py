import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:myella@localhost/student-api")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 

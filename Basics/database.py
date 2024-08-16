#!/usr/bin/python3
import mysql.connector as mc
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

details = {
    "user": "root",
    "password": "XXXXXXXX",
    "host": "localhost",
    "database": "test",
}

engine = mc.connection.MySQLConnection(**details)

if engine and engine.is_connected():
    print("Connected to MySQL database successfully!")
else:
    print("Failed to connect to MySQL database.")

engine.close()
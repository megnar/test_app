from website import create_app, create_database
from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import os

app = create_app()

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0', port = 5000)

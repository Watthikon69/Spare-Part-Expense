from flask import Flask, jsonify
from flask_restful import Api, Resource
import psycopg2
from psycopg2 import OperationalError
from datetime import date, datetime
# from upload_file import UploadFile
from flask import request
from dotenv import load_dotenv
load_dotenv()
import os

from resources.spe_convert import ConvertCsvToJson


app = Flask(__name__)
api = Api(app)

api.add_resource(ConvertCsvToJson, '/convertexcel')
# api.add_resource(CheckDataMySelf, '/chkdata')

if __name__ == '__main__':
    # app.run(host="172.18.55.45", port=5000, debug=True)
    app.run(host="0.0.0.0", port=5003, debug=True)
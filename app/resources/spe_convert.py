from flask_restful import Resource
from flask import make_response
import pandas as pd
import os
import json
from datetime import datetime

FOLDER_PATH = r"D:\TANAKA\Spare-Part-Expense\doc\spare part history"

class ConvertCsvToJson(Resource):
    def get(self):
        try:
            if not os.path.exists(FOLDER_PATH):
                return {"error": "Folder not found"}, 404

            files = [f for f in os.listdir(FOLDER_PATH) if f.endswith(".xlsx")]
            result = {}

            for file in files:
                file_path = os.path.join(FOLDER_PATH, file)
                try:
                    df = pd.read_excel(file_path, header=0, sheet_name="Sheet1", engine="openpyxl")
                    df = df.applymap(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, datetime) else x)
                    result[file] = df.to_dict(orient="records")
                except Exception as e:
                    result[file] = f"Error reading file: {str(e)}"

            json_str = json.dumps({
                "files": files,
                "data": result
            }, ensure_ascii=False, indent=2)

            # ✅ ส่ง response พร้อม header ชัดเจน
            response = make_response(json_str)
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return response

        except Exception as e:
            return {"error": str(e)}, 500

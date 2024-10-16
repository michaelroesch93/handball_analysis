from flask import jsonify, request
import sqlite3
from config import *

def team_api():

    if request.method == "POST":

        return team_post()
    
    elif request.method == "GET":

        return team_get()
    
def team_post():

    data = request.get_json()

    try: 

        name = data["name"]

        db_handle = sqlite3.connect(db_name)
        cursor = db_handle.cursor()
        cursor.execute("INSERT INTO teams (name) VALUES(?)", (name,))
        db_handle.commit()
    
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"})
    
    return jsonify({"message": "Team created successfully", "team": {"name": name}})

def team_get():

    try: 
        db_handle   = sqlite3.connect("database.db")
        cursor      = db_handle.cursor()
        cursor.execute("SELECT * FROM teams")
        request_data = cursor.fetchall()
        db_handle.close()

        teams = []
        for row in request_data:
            teams.append({
                "id": row[0],
                "name": row[1],
            })

        return jsonify({"teams": teams}), 200

    except Exception as e:
        return jsonify({"error": f"Database error: {e}"}), 500
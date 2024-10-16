from flask import jsonify, request
import sqlite3
from config import *

def player_api():

    if request.method == "POST":

        return player_post()

    elif request.method == "GET":

        return player_get()

def player_post():
        
    data = request.get_json()

    try:

        first_name  = data['first_name']
        last_name   = data['last_name']

        db_handle   = sqlite3.connect("database.db")
        cursor      = db_handle.cursor()
        cursor.execute("INSERT INTO players (first_name, last_name) VALUES(?,?)", (first_name, last_name))
        db_handle.commit()
        db_handle.close()

    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"})
    
    return jsonify({"message": "Player created successfully", "player": {"first_name": first_name, "last_name": last_name}}), 201

def player_get():

    try: 
        db_handle   = sqlite3.connect("database.db")
        cursor      = db_handle.cursor()
        cursor.execute("SELECT * FROM players")
        request_data = cursor.fetchall()
        db_handle.close()

        players = []
        for row in request_data:
            players.append({
                "first_name": row[0],
                "last_name": row[1]
            })

        return jsonify({"player": players}), 200

    except Exception as e:
        return jsonify({"error": f"Database error: {e}"}), 500

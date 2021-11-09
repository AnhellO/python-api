from flask import Flask, request, g
import sqlite3
import os

DATABASE = os.getenv('DB')

app = Flask(__name__)

@app.route('/')
def get():
    member_id = request.args.get("member_id")
    if member_id == None:
        return {}

    member = query_db("SELECT * FROM members WHERE id = ?", [member_id], one=True)
    return "" if member is None else member

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    
    db.row_factory = make_dicts
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
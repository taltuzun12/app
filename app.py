from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Set up database connection
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="postgres",
    user="postgres",
    password="1234"
)

# Define a route to get all table data
@app.route('/api/data')
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table1")
    table_data = cur.fetchall()
    cur.close()
    return jsonify(table_data)

# Define a route to insert data into the table
@app.route('/api/data', methods=['POST'])
def insert_data():
    data = request.get_json()
    
    if 'id' not in data or 'name' not in data or 'age' not in data:
        return jsonify({'success': False, 'error': 'Missing data'})
    
    id = data['id']
    name = data['name']
    age = data['age']
    
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO your_table1 (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
        conn.commit()
        cur.close()
        return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)

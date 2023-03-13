from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run(debug=True)

#Reads row count every second.
#Exposes an HTTP API.
#Measures query response time.


from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    db = mysql.connector.connect(
        host="mysql-slave",
        user="root",
        password="password",
        database="testdb"
    )
    cursor = db.cursor()
    
    start_time = time.time()
    cursor.execute("SELECT COUNT(*) FROM records")
    row_count = cursor.fetchone()[0]
    response_time = (time.time() - start_time) * 1000
    
    return jsonify({
        "rows": row_count,
        "response_time_ms": response_time
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="database-1.c4xws8gkeqdj.us-east-1.rds.amazonaws.com",
    user="admin",
    password="YOUR_PASSWORD",
    database="testdb"
)

@app.route("/", methods=["GET", "POST"])
def home():
    cursor = db.cursor()

    if request.method == "POST":
        name = request.form["name"]
        cursor.execute(
            "INSERT INTO users (name) VALUES (%s)",
            (name,)
        )
        db.commit()

    cursor.execute("SELECT name FROM users")
    data = cursor.fetchall()

    html = "<h1>Users List</h1>"

    html += "<form method='POST'>"
    html += "<input name='name' placeholder='Enter name'>"
    html += "<button type='submit'>Add</button>"
    html += "</form>"

    html += "<ul>"
    for row in data:
        html += f"<li>{row[0]}</li>"
    html += "</ul>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
~

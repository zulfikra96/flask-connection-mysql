from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'learn_flask'
mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect().cursor()
    conn.execute("SELECT * FROM nama")
    ex = conn.fetchall()
    return str(ex)

if __name__ == "__main__":
    app.run(debug=True)
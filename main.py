from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret'
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "leads"
app.config["MYSQL_PORT"] = 3306

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("Select * from leadsinfo")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', leads=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO leadsinfo (name, email,company, phone) VALUES (%s, %s, %s,%s)", (name, email, company,phone))
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM leadsinfo WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE leadsinfo SET name=%s, email=%s, phone=%s ,company=%s
        WHERE id=%s
        """, (name, email, phone, company, id_data))
        mysql.connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)

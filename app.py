import sqlite3

from flask import Flask, flash, jsonify, render_template, request


app = Flask(__name__)
app.secret_key = '#$%1RTY2^&3FGh4%^&*{"5)(iukVT^ioIo_\{\:DFDFHJHkjn})'

DATABASE_NAME = "flask_ajax_db"


@app.route('/read', methods=['GET', 'POST'])
def read():
    status = 0
    result = []
    message = ''

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        result = cur.execute(
            "SELECT * FROM `info` ORDER BY `id` DESC").fetchall()

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

    if result:
        status = 1

    response_object = {
        'status': status,
        'result': result
    }

    # flash(message, 'info')
    return jsonify(response_object=response_object)


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    status = 0
    result = ''
    message = "Task not deleted"

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        result = cur.execute(
            "DELETE FROM `info` WHERE `id` = ?", (id, )).rowcount

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

    if result > 0:
        status = 1
        message = "Task deleted"

    response_object = {
        'status': status,
        'result': result
    }

    flash(message, 'info')
    return jsonify(response_object=response_object)


@app.route('/insert', methods=['POST'])
def insert():

    status = 0
    result = "Provide first or last name"

    first_name = request.form.get('firstName', '')
    last_name = request.form.get('lastName', '')

    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        result = cur.execute(
            "INSERT INTO `info`(`firstname`, `lastname`) VALUES(?, ?)", (first_name, last_name)).rowcount

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)

    if first_name or last_name:
        status = 1
        result = f"{first_name} {last_name}"

    response_object = {
        'status': status,
        'result': result
    }

    return jsonify(response_object=response_object)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('app.html')


if __name__ == "__main__":
    app.run(debug=True)

import sqlite3

from flask import Flask, flash, jsonify, render_template, request

app = Flask(__name__)
DATABASE_NAME = "flask_ajax_db"


@app.route('/delete/<data>', methods=['DELETE'])
def delete(data):
    status = 0
    result = ''
    message = "Task not deleted"

    try:
        first_name, last_name = data.split(" ")

        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        result = conn.execute(
            "DELETE FROM `info` WHERE `firstname` = ? AND `lastname` = ?", (first_name, last_name)).rowcount

        conn.commit()

    except Exception as e:
        result = e
    finally:
        cur.close()
        conn.close()

    if result:
        status = 1
        message = "Task deleted"

    response_object = {
        'status': status,
        'result': result
    }

    flash(message)
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
        result = conn.execute(
            "INSERT INTO `info`(`firstname`, `lastname`) VALUES(?, ?)", (first_name, last_name)).rowcount

        conn.commit()

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

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
    app.secret_key = '#$%1RTY2^&3FGh4%^&*{"5)(iukVT^ioIo_\{\:DFDFHJHkjn})'

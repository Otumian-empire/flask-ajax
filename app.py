from flask import Flask, jsonify, render_template, request
import sqlite3


app = Flask(__name__)
DATABASE_NAME = "flask_ajax_db"


@app.route('/process', methods=['POST'])
def add_numbers():

    status = 0

    first_name = request.form.get('firstName', '')
    last_name = request.form.get('lastName', '')

    if first_name or last_name:
        status = 1
        result = f"{first_name}  {last_name}"
    else:
        result = "Provide first or last name"

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

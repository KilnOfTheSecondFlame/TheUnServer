from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return error(701)


def error(error_number):
    return render_template('error.html', error_number=error_number, error_description="Test")


if __name__ == '__main__':
    app.run(debug=True)

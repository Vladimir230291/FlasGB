from flask import Flask, request, render_template, redirect, url_for, flash, make_response
from pathlib import Path, PurePath
from markupsafe import escape
from werkzeug.utils import secure_filename
import secrets
import logging

app = Flask(__name__)
app.secret_key = secrets.token_hex()
logger = logging.getLogger(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/hello.html', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('hello.html', name=name)
    return render_template('hello.html')


@app.route('/task2/task2_img.html')
def task2_img():
    return render_template('task2/task2_img.html')


@app.route('/task2/task2_dwn.html', methods=['POST', 'GET'])
def task2_dwn():
    if request.method == 'POST':
        file = request.files['file']
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), "uploads", file_name))
        return f'Файл {file_name} успешно загружен'
    return render_template('task2/task2_dwn.html')


@app.post('/task3/task3_main.html')
def task3_auth():
    message = 'Неверный логин или пароль'
    login = request.form['login']
    password = request.form['password']
    if login == 'admin' and password == 'admin':
        message = 'Добро пожаловать!'
    return f"{message}"


@app.route('/task3/task3_main.html')
def task3():
    return render_template('task3/task3_main.html')


@app.route('/task4/task4_main.html')
def task4():
    return render_template('task4/task4_main.html')


@app.post('/task4/task4_main.html')
def task4_get():
    count = len(escape(request.form['text']))
    return render_template('task4/task4_res.html', count=count)


@app.route('/task5/calc.html')
def calc():
    return render_template('task5/calc.html')


@app.post('/task5/calc.html')
def calc_post():
    result = 'Введены не корректные данные'
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    except ValueError:
        return render_template('task5/calc.html', result=result)

    operation = request.form['operation']
    if operation == 'sum':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mult':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            result = 'На ноль делить нельзя'
        else:
            result = num1 / num2
    return render_template('task5/calc.html', result=result)


@app.route('/task6/task6_main.html')
def task6():
    return render_template('task6/task6_main.html')


@app.post('/task6/task6_main.html')
def task6_post():
    name = escape(request.form['name'])
    try:
        age = int(request.form['age'])
        if 0 < age < 100:
            return render_template('task6/task6_res.html', name=name, age=age)
    except ValueError:
        return render_template('task6/task6_error.html')


@app.route('/task7/task7_main.html')
def task7():
    return render_template('task7/task7_main.html')


@app.post('/task7/task7_res.html')
def task7_post():
    try:
        num = int(request.form['num'])
        result = pow(num, 2)
        return render_template('task7/task7_res.html', num=num, result=result)
    except ValueError:
        return render_template('task7/task7_error.html')


@app.route('/task8/task8_main.html', methods=['POST', 'GET'])
def task8():
    if request.method == 'POST':
        if not request.form['name']:
            flash(f"Введите имя", category='error')
            flash("Повторите ввод")
            return render_template(url_for('task8'))
        flash(f"Привет, {request.form['name']}", category='success')

    return render_template(url_for('task8'))


@app.route('/home_work/main.html', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Создание cookie файла с данными пользователя
        response = make_response(render_template(url_for('welcome'), name=name))
        response.set_cookie('name', name, max_age=60 * 24 * 7)
        response.set_cookie('email', email, max_age=60 * 24 * 7)
        return response
    return render_template(url_for('home'))


@app.route('/home_work/welcome.html')
def welcome():
    # Получение данных пользователя из cookie файла
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    if name and email:
        return render_template(url_for('welcome'), name=name)
    else:
        return redirect(url_for('home'))


@app.route('/home_work/logout')
def logout():
    response = make_response(url_for('home'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5001)

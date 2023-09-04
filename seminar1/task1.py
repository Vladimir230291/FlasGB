from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main/')
def hello():
    return render_template('main.html')


@app.route('/about/')
def about():
    return "About page"


@app.route('/contact/')
def contact():
    return "Contact page"


@app.route('/sum/<int:a>/<int:b>')
def sum_nums(a: int, b: int) -> str:
    return str(a + b)


@app.route('/len/<string:name>')
def len_name(name: str) -> str:
    return str(len(name))


@app.route('/students')
def students():
    head = {
        'name': 'Имя',
        "last_name": "Фамилия",
        "age": "Возраст",
        'rank': "Cредний балл"
    }
    students = [{
        'name': 'Иван',
        'last_name': 'Иванов',
        'age': 20,
        'rank': 5
    }, {
        'name': 'Петр',
        'last_name': 'Петров',
        'age': 25,
        'rank': 4
    }, {
        'name': 'Сергей',
        'last_name': 'Сергеев',
        'age': 30,
        'rank': 3
    }]
    return render_template('students.html', head=head, students=students)


@app.route('/news/')
def news():
    news_block = [{
        'title': 'Новость 1',
        'text': 'Текст новости 1',
        'date_publish': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
        {
            'title': 'Новость 2',
            'text': 'Текст новости 2',
            'date_publish': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, {
            'title': 'Новость 3',
            'text': 'Текст новости 3',
            'date_publish': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]
    return render_template('news_blog.html', news_block=news_block)


if __name__ == "__main__":
    app.run(debug=True)

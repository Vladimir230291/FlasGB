from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
import secrets
from lesson3_WTForm.form import LoginForm, RegstrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route("/form", methods=["GET", "POST"])
@csrf.exempt
def form():
    return "No csrf"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        return 'OK'
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegstrationForm()
    if request.method == 'POST' and form.validate():
        # обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

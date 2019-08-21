from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'autor': 'Everton Sousa',
        'titulo': 'Post 1',
        'publicacao': 'Prazer, meu nome é Everton!',
        'data': '18, Agosto, 2019'
    },
    {
        'autor': 'Jaqueline Santos',
        'titulo': 'Post 2',
        'publicacao': 'Prazer, meu nome é Jaqueline!',
        'data': '17, Agosto, 2019'
    },
    {
        'autor': 'Gustavo Honorato',
        'titulo': 'Post 3',
        'publicacao': 'Prazer, meu nome é Gustavo!',
        'data': '18, Agosto, 2019'
    },
    {
        'autor': 'Jorge Castro',
        'titulo': 'Post 4',
        'publicacao': 'Prazer, meu nome é Jorge!',
        'data': '17, Agosto, 2019'
    },
    {
        'autor': 'Matheus Santos',
        'titulo': 'Post 5',
        'publicacao': 'Prazer, meu nome é Matheus!',
        'data': '22, Agosto, 2019'
    },
    {
        'autor': 'Pedro Henrique',
        'titulo': 'Post 6',
        'publicacao': 'Prazer, meu nome é Pedro!',
        'data': '14, Agosto, 2019'
    },
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=posts)


@app.route("/sobre")
def sobre():
    return render_template('sobre.html', title='Sobre')


@app.route("/registro", methods=['GET', 'POST'])
def registro():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta criada para {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('registro.html', title='Registro', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data ==  'admin@gmail.com' and form.password.data == 'admin':
            flash('Logado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Email ou senha inválidos. Verifique os dados e tente novamente', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

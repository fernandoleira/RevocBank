from flask import request, redirect, session, render_template, url_for
from app import app, revoc_blockchain
from models import db, User
from forms import SignupForm, LoginForm, TransferForm


@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/index')
def index():
    if "email" not in session:
        return redirect(url_for('login'))

    else:
        usr = User.query.filter_by(email=session["email"]).first
        return render_template('index.html', title='Index', usr=usr)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'email' in session:
        return redirect(url_for('index'))

    form = SignupForm()

    if request.method == 'POST':

        if not form.validate():
            return render_template('signup.html', title='Sign Up', form=form)

        else:
            new_user = User(form.first_name.data, form.last_name.data, form.username.data, form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.email
            return redirect(url_for('index'))

    else:
        return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'email' in session:
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == "POST":
        if not form.validate():
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    else:
        return render_template('login.html', title='Log In')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'email' in session:
        return redirect(url_for('index'))

    form = TransferForm()

    if request.method == 'POST':
        from_usr = mongo.find_one({'user_id': session['user_id']})
        to_usr = mongo.find_one({'username': request.form['to_username']})
        amount = float(request.form['amount'])

        from_usr['amount'] = float(from_usr['amount']) - amount
        to_usr['amount'] = float(to_usr['amount']) + amount

        # Update database
        mongo.update({'user_id': session['user_id']}, from_usr)
        mongo.update({'username': request.form['to_username']}, to_usr)

        # Add to blockchain
        new_transaction = [{
            'from': from_usr['username'],
            'to': to_usr['username'],
            'amount': amount
        }]
        revoc_blockchain.add_block(new_transaction)

        db.session.commit()

        return redirect(url_for('index'))

    else:
        usr = mongo.find_one({'user_id': session['user_id']})
        return render_template('transfer.html', title='New Transfer', form=form)


@app.route('/blockchain')
def blockchain():
    bchain = revoc_blockchain.print_blocks()
    return render_template('blockchain.html', title='Blockchain', bchain=bchain)

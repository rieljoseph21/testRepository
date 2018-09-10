from flask import render_template, request, redirect, url_for, flash

from app.forms import SignInForm, SignUpForm

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.fullname.data))
        return redirect(url_for('index'))
    return render_template('sign_up.html', title='Sign Up', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    return render_template('sign_in.html', title='Sign In', form=form)

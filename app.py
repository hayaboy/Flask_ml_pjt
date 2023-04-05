from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app=Flask(__name__)

class HelloForm(Form):
    hdskj = TextAreaField('',[validators.DataRequired()])

# A decorator that is used to register a view function for a given URL rule. This does the same thing as add_url_rule but is intended for decorator usage:
@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)



@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['hdskj']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)




if __name__=='__main__':
    app.run(debug=True)
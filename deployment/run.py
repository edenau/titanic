# coding=utf-8

# Import libraries
from gen_html import fit_model
from flask import Flask, render_template, request
from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField, SelectField
import pickle

# Create app
app = Flask(__name__)
model_choice = 'soft'

# Define a form
class ReusableForm(Form):

    sex = SelectField('Sex:',
                      choices=[('1', 'Male'), ('0', 'Female') ],
                      validators=[validators.InputRequired()])

    title = SelectField('Title:',
                  choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Master', 'Master'),
                           ('Rare', 'Sir'), ('Rare', 'Lady'), ('Rare', 'The Reverend'), ('Rare', 'The Countess'),
                           ('Rare', 'Don'), ('Rare', 'Doña'), ('Rare', 'Dr'),
                           ('Rare', 'Captain'), ('Rare', 'Colonel'), ('Rare', 'Major')],
                  validators=[validators.InputRequired()])

    age = DecimalField('Age:',
                       default=30,
                       places=0,
                       validators=[validators.InputRequired(),
                                   validators.NumberRange(min=0.5, max=80,
                                                          message='Age must be between 0.5 and 80')])

    Pclass = SelectField('Ticket class:',
                         choices=[('1', 'First Class'), ('2', 'Second Class'), ('3', 'Third Class') ],
                         validators=[validators.InputRequired()])

    cabin = SelectField('Has cabin or not:',
                        choices=[('1', 'Yes'), ('0', 'No') ],
                        validators=[validators.InputRequired()])

    SibSp = IntegerField('Number of siblings and spouses aboard:',
                         default=0,
                         validators=[validators.InputRequired(),
                                     validators.NumberRange(min=0, max=9,
                                                            message='Number must be between 0 and 9')])

    ParCh = IntegerField('Number of parents and children aboard:',
                         default=0,
                         validators=[validators.InputRequired(),
                                     validators.NumberRange(min=0, max=9,
                                                            message='Number must be between 0 and 9')])

    fare = DecimalField('Passenger Fare:',
                        default=33,
                        places=1,
                        validators=[validators.InputRequired(),
                                    validators.NumberRange(min=0, max=512,
                                                           message='Fare must be between 0 and 512')])
    embarked = SelectField('Port of Embarkation:',
                         choices=[('S', 'Southampton, England'), ('C', 'Cherbourg, France'), ('Q', 'Queenstown, Ireland') ],
                         validators=[validators.InputRequired()])


    submit = SubmitField('Predict')


# load pre-trained models and setups
def load_model():
    global model
    with open('model_{}.pkl'.format(model_choice), 'rb') as f:
        model = pickle.load(f)
    global scaler
    with open('scaler_{}.pkl'.format(model_choice), 'rb') as f:
        scaler = pickle.load(f)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # Create form
    form = ReusableForm(request.form)

    # On form entry and all entries validated
    if request.method == 'POST' and form.validate():
        # Extract information
        sex = int(request.form['sex'])
        title = request.form['title']
        age = float(request.form['age'])
        Pclass = int(request.form['Pclass'])
        cabin = int(request.form['Pclass'])
        SibSp = int(request.form['SibSp'])
        ParCh = int(request.form['ParCh'])
        fare = float(request.form['fare'])
        embarked = request.form['embarked']
        # Send information to template
        return render_template('predict.html',
                               input=fit_model(sex=sex,
                                               title=title,
                                               age=age,
                                               Pclass=Pclass,
                                               cabin=cabin,
                                               SibSp=SibSp,
                                               ParCh=ParCh,
                                               fare=fare,
                                               embarked=embarked,
                                               model=model,
                                               scaler=scaler))

    return render_template('index.html',
                           form=form)


if __name__ == '__main__':
    print((' * Loading model and Flask starting server...\n * Please wait until server has fully started'))
    load_model()
    # Run app
    app.run(host='0.0.0.0', port=80)

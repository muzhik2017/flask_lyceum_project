from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class SignForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    patronymic = StringField('Отчество', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[DataRequired()])
    date = DateField('Дата осмотра', format='%Y-%m-%d', validators=[DataRequired(), ], id='datepick')
    submit = SubmitField('Подтвердить')

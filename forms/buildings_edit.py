from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class BuildingForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    about = TextAreaField("Содержание")
    tags = TextAreaField("Краткое описание")
    price = IntegerField("Цена")
    address = StringField('Адрес')
    image_link = TextAreaField('Ссылка на картинки(через пробел)')
    submit = SubmitField('Применить')

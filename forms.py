from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ColorNameForm(FlaskForm):
    color_name = StringField('Color', validators=[DataRequired()])
    submit = SubmitField('Submit Color String')
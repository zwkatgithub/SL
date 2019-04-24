from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ClauseForm(FlaskForm):
    clauses = TextAreaField(label='条款',validators=[DataRequired('请输入条款')])
    submit = SubmitField("提交")



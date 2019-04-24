from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HtNameForm(FlaskForm):
    name = StringField(label='合同名称',validators=[DataRequired('请输入合同名称')])
    submit = SubmitField("提交")

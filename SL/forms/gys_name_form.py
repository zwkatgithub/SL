from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GysNameForm(FlaskForm):
    gys_name = StringField(label='合同主体A',validators=[DataRequired('请输入名称')])
    str_name = StringField(label='合同主体B', validators=[DataRequired('请输入名称')])
    submit = SubmitField("提交")


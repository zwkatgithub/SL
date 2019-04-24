from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class PayConditionsForm(FlaskForm):
    conditions = StringField(label='支付条件',validators=[DataRequired('请输入支付条件')])
    submit = SubmitField("提交")


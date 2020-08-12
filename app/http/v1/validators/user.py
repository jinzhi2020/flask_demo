from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.http.v1.enums.user import UserFromEnum


class UserRegister(Form):
    username = StringField(validators=[DataRequired(), length(
        min=5, max=32
    )])
    password = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            user_from = UserFromEnum(value.data)
        except ValueError as error:
            raise error
        self.type = user_from

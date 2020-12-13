from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField(
        label="Email",
        validators=[DataRequired(message="Dit veld is verplicht")],
    )
    password = PasswordField(
        label="Wachtwoord",
        validators=[
            DataRequired(message="Dit veld is verplicht"),
            Length(
                min=8,
                message="Wachtwoord moet uit minimaal 8 karakters bestaan!",
            ),
        ],
    )
    confirm_password = PasswordField(
        label="Bevestig wachtwoord",
        validators=[
            DataRequired(message="Dit veld is verplicht"),
            EqualTo(
                "password",
                message="Wachtwoorden zijn niet gelijk!",
            ),
        ],
    )
    submit = SubmitField(label="Registreer")


class LoginForm(FlaskForm):
    email = EmailField(
        label="Email",
        validators=[DataRequired(message="Dit veld is verplicht")],
    )
    password = PasswordField(
        label="Wachtwoord",
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Wachtwoord moet uit minimaal 8 karakters bestaan!",
            ),
        ],
    )
    remember = BooleanField(label="Ingelogd blijven")
    submit = SubmitField(label="Registreer")

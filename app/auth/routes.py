from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user

from app import db
from .models import User
from .forms import RegisterForm


bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["GET", "POST"])
def register():
    """
    Registers new users by submitting their email address and a password
    """
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.hash_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(
            f"Account for {user.full_name()} has been created and you're logged in",
            "success",
        )
        return redirect(url_for("home"))
    return render_template(
        "auth/register.html",
        form=form,
        title="Registreer je account",
    )

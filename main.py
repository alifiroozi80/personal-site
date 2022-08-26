from flask import Flask, render_template, redirect, url_for, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import datetime
import smtplib
import os

SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap(app)


class ContactUsForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = StringField(label="Your Email", validators=[DataRequired(), Email()])
    content = CKEditorField(label="Your message", validators=[DataRequired()])
    submit = SubmitField(label="Send!")


def send_emil(name: str, email: str, message: str) -> None:
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="alifiroozizamani@gmail.com",
            msg=email_message
        )


@app.route("/", methods=["GET", "POST"])
def home():
    contact_form = ContactUsForm()
    year = datetime.now().strftime("%Y")
    if contact_form.validate_on_submit():
        send_emil(name=contact_form.name.data, email=contact_form.email.data, message=contact_form.content.data)
        return redirect(url_for("home"))
    return render_template("index.html", form=contact_form, year=year)


@app.route("/download-resume", methods=["GET", "POST"])
def download():
    path = "static/downloadable/Resume.pdf"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

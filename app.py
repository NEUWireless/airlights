from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
import logging
from forms import ColorNameForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-neu'
Bootstrap(app)
colorpicker(app)

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def index():
    color_name_form = ColorNameForm()
    if color_name_form.validate_on_submit():
        flash('Color String POST: {}'.format(color_name_form.color_name))
        logging.debug("Color entered: %s", color_name_form.color_name)
    # logging.debug("RGB: %s", request.form)
    return render_template("index.html", form=color_name_form)


if __name__ == "__main__":
    app.run()
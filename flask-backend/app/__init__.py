from flask import Flask, render_template, redirect
from .config import Config
# from .shipping_form import ShippingForm
from flask_migrate import Migrate
from .route.items import items
from .route.pokemon import pokemon
from .models import db

# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


app.register_blueprint(items, url_prefix='/items')
app.register_blueprint(pokemon, url_prefix='/pokemon')

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching in development

from app import routes

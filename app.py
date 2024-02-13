from flask import Flask

import contact
import home
import others
import rate_limits
import todos

app = Flask(__name__)
PATH = '/flaskapi/v1'

app.register_blueprint(home.home_bp, url_prefix=PATH+'/home')
app.register_blueprint(contact.contact_bp, url_prefix=PATH+'/contact')
app.register_blueprint(rate_limits.rate_limits_bp, url_prefix=PATH+'/ratelimits')
app.register_blueprint(others.others_bp, url_prefix=PATH+'/others')
app.register_blueprint(todos.bp, url_prefix=PATH+'/todos')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5909"))

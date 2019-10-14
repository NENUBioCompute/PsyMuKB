from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'nenu204'


app.register_blueprint(app_Index, url_prefix="")
app.register_blueprint(app_Search, url_prefix="")
app.register_blueprint(app_Browser, url_prefix="/Browse")
app.register_blueprint(app_Document, url_prefix="/Document")
app.register_blueprint(app_Contact, url_prefix="/Contact")
app.register_blueprint(app_Download, url_prefix="/Download")


@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

if __name__ == '__main__':
	app.run(debug=True, threaded=True)

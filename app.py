from flask import Flask
from config import Config
from extensions import db,migrate
from routes import main
from admin import admin
from tracking import tracking
from api import api
app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app);migrate.init_app(app,db)
app.register_blueprint(main);app.register_blueprint(admin,url_prefix='/admin');app.register_blueprint(tracking,url_prefix='/tracking');app.register_blueprint(api,url_prefix='/api')
with app.app_context(): db.create_all()
if __name__=='__main__': app.run(debug=True)

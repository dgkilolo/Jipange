import os

class Config:


    SECRET_KEY = '1234'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dkg:boot@localhost/jipange'  
                ### remeber to change to your own local database
                # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'yourdatabase':'yourpassword'@localhost/jipange'  
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:12345@localhost/jipange'  
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,


}
import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mercy:shii@localhost/jipange'  
                ### remeber to change to your own local database
                # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'yourdatabase':'yourpassword'@localhost/jipange'  
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    


class DevConfig(Config):
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,


}
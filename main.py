from data.config import DevelopmentConfig
from data.server import create_app

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run()

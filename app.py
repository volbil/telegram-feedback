from service import create_app
import config

app = create_app()

if __name__ == "__main__":
    app.run(**config.params)

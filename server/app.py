from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """Return a welcome message for the default route."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def car_model(model):
    """Return a message based on whether the requested model exists."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(debug=True)

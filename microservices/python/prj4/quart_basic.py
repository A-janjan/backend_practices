from quart import Quart


app = Quart(__name__)


@app.route('/api')
def my_microservice():
    return {'Hello': 'World!'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
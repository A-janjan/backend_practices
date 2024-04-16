from quart import Quart
import yaml


def yamlify(data, status=200, headers=None):
    _headers = {"Content-Type": "application/x-yaml"}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data), status, _headers



app = Quart(__name__)


@app.route("/api")
def my_microservice():
    return yamlify("Hello", "world", "with", "YAML")


if __name__ == "__main__":
    app.run()
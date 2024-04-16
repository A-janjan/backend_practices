from quart import Quart, jsonify, abort
from werkzeug.exceptions import HTTPException, default_exceptions


def jsonify_errors(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {
                "code": error.code,
                "description": error.description,
                "message": str(error),
            }
        else:
            description = abort.mapping[error.code].description
            result = {"code": error.code, "description": description, "message": str(error)}

        resp = jsonify(result)
        resp.status_code = result["code"]
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)
    return app


app = Quart(__name__)
app = jsonify_errors(app)


@app.route("/api")
def my_microservice():
    raise TypeError("some exception")


if __name__ == "__main__":
    app.run()

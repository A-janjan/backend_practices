from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found", "message": "The requested URL was not found on the server."}), 404

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad Request", "message": "The server could not understand the request due to invalid syntax."}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": "The server encountered an unexpected condition which prevented it from fulfilling the request."}), 500



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
    
    
@app.route("/api/endpoint1", methods=["GET"])
def endpoint1():
    msg = {"msg": "this is endpoint 1"}
    return jsonify(msg)
    
@app.route("/api/endpoint2", methods=["POST"])
def endpoint2():
    msg_req = request.get_json()
    if not msg_req:
        return jsonify({"error": "Bad Request", "message": "JSON data not provided in request."}), 400
    return jsonify({"received data": msg_req})


@app.route("/api/endpoint3", methods=["POST"])
def endpoint3():
    try:
        data = request.get_json()
        radius = data['radius']
        area = radius**2 *3.14
        return jsonify({"area is : ": area})
    except KeyError:
        return jsonify({"error": "Bad Request", "message": "Missing 'radius' parameter in JSON data."}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
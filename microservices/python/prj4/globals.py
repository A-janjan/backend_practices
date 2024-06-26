from quart import Quart, g, request

app = Quart(__name__)



@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization["username"]
    else:
        g.user = "Anonymous"
        
        
@app.route("/api")
async def my_microservice():
    return {"hello": g.user}


if __name__ == "__main__":
    app.run()
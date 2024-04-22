# Tips


Routing is an essential part of building a web application. Routing in FastAPI is flexible
and hassle-free. Routing is the process of handling HTTP requests sent from a client to
the server. HTTP requests are sent to defined routes, which have defined handlers for
processing the requests and responding. These handlers are called route handlers.


A route is defined to accept requests from an HTTP request method and optionally take
parameters. When a request is sent to a route, the application checks whether the route
is defined before processing the request in the route handler. On the other hand, a route
handler is a function that processes the request sent to the server. An example of a route
handler is a function that retrieves records from a database when a request is sent to
a router via a route.


Traditionally, the FastAPI() instance can be used for routing operations, as seen
previously. However, this method is commonly used in applications that require a single
path during routing. In a situation where a separate route performing a unique function is
created using the FastAPI() instance, the application will be unable to run both routes,
as uvicorn can only run one entry point.

===

The APIRouter class belongs to the FastAPI package and creates path operations for
multiple routes. The APIRouter class encourages modularity and organization of
application routing and logic.


=== 


run server:

(venv)$ uvicorn api:app --port 8000 --reload

execute:

(venv)$ curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 2,
"item": "Validation models help with input types"
}'


execute:

(venv)$ curl -X 'GET' \
'http://127.0.0.1:8000/todo/1' \
-H 'accept: application/json'


===


Path parameters are parameters included in an API route to identify resources. These
parameters serve as an identifier and, sometimes, a bridge to enable further operations in
a web application.


===

FastAPI also provides a Path class that distinguishes path parameters from other
arguments present in the route function. The Path class also helps give route parameters
more context during the documentation automatically provided by OpenAPI via Swagger
and ReDoc and acts as a validator.


===

### FAST API automatic docs


swagger -> http://127.0.0.1:8000/docs

ReDoc -> http://127.0.0.1:8000/redoc


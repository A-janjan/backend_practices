# Todo App

## Representation
![todo_app](https://github.com/A-janjan/backend_practices/assets/62621376/a95f79e1-ed58-4d8f-8d12-6aa35e28afd1)


## Tips

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
or
(venv)$ uvicorn api:app --host=0.0.0.0 --port 8000 --reload

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


==========================


Response status codes are grouped into five categories, each denoting a different response:
• 1XX: Request has been received.
• 2XX: The request was successful.
• 3XX: Request redirected.
• 4XX: There’s an error from the client.
• 5XX: There’s an error from the server.


============================

Errors from requests can result from attempting to access non-existent resources,
protected pages without sufficient permissions, and even server errors. Errors in FastAPI
are handled by raising an exception using FastAPI’s HTTPException class.

What Is an HTTP Exception?
- An HTTP exception is an event that is used to indicate a fault or issue in the
request flow.

The HTTPException class takes three arguments:
• status_code: The status code to be returned for this disruption
• detail: Accompanying message to be sent to the client
• headers: An optional parameter for responses requiring headers



=============================


we can declare the HTTP status code to override the default status code for
successful operations by adding the status_code argument to the decorator function:

-> @todo_router.post("/todo", status_code=201)


=============================

## Templating in FastAPI

Templating is the process of displaying the data gotten from the API in various formats.
Templates act as a frontend component in web applications.


Jinja is a templating engine written in Python designed to help the rendering process of
API responses. In every templating language, there are variables that get replaced with the
actual values passed to them when the template is rendered, and there are tags that control
the logic of the template.

The three common syntax blocks used in the Jinja templating language include
the following:

• {% … %} – This syntax is used for statements such as control structures.

• {{ todo.item }} – This syntax is used to print out the values of the expressions
passed to it.

• {# This is a great API book! #} – This syntax is used when writing
comments and is not displayed on the web page.


A filter is separated from the variable by a pipe symbol (|) and may entertain optional
arguments in parentheses. A filter is defined in this format:

{{ variable | filter_name(*args) }}


* If there are no arguments, the definition becomes the following:

{{ variable | filter_name }}

* The default filter variable is used to replace the output of the passed value if it turns out
to be None:

{{ todo.item | default('This is a default todo item') }}
This is a default todo item


* This filter is used to render raw HTML output:
{{ "<title>Todo Application</title>" | escape }}
<title>Todo Application</title>



* These filters include int and float filters used to convert from one data type to another:
{{ 3.142 | int }}
3
{{ 31 | float }}
31.0


* This filter is used to join elements in a list into a string as in Python:
{{ ['Packt', 'produces', 'great', 'books!'] | join(' ') }}
Packt produces great books!


* This filter is used to return the length of the object passed. It fulfills the same role as
len() in Python:
Todo count: {{ todos | length }}
Todo count: 4


* The usage of if statements in Jinja is similar to their usage in Python. if statements are
used in the {% %} control blocks. Let’s look at an example:
{% if todo | length < 5 %}
You don't have much items on your todo list!
{% else %}
You have a busy day it seems!
{% endif %}



A macro in Jinja is a function that return an HTML string. The main use case for
macros is to avoid the repetition of code and instead use a single function call.
{% macro input(name, value='', type='text', size=20) %}
<div class="form">
    <input type="{{ type }}" name="{{ name }}" value="{{ value|escape }}" size="{{ size }}">
</div>
{% endmacro %}
Now, to quickly create an input in your form, the macro is called:
{{ input('item') }}
This will return the following:
<div class="form">
    <input type="text" name="item" value="" size="20">
</div>

=========================


from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime


def render_email(**data):
    with open("email_template.j2") as f:
        template = Template(f.read())
    return template.render(**data)


data = {
    "date": format_datetime(datetime.now()),
    "to": "ali@example.com",
    "from": "shopping@example-shop.com",
    "subject": "Your Burger order",
    "name": "Ali",
    "items": [
        {"name": "Chicken", "price": 4.5},
        {"name": "Fries", "price": 2.0},
        {"name": "Root Beer", "price": 3.0},
    ],
}


print(render_email(**data))

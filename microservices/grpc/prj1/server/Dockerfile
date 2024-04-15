FROM python3
WORKDIR /app
COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]
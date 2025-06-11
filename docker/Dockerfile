FROM python:3.11-bookworm
RUN pip install pipenv
WORKDIR /app
COPY Pipfile* ./
COPY ./apps ./apps
COPY ./oreplay ./oreplay
COPY ./manage.py .
RUN pipenv install
#RUN pipenv shell
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8888"]

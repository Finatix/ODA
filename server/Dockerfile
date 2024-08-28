FROM public.ecr.aws/docker/library/python:3.12
WORKDIR /oda-python-backend
COPY . /oda-python-backend
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["fastapi", "run","main.py"]

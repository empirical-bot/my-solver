# Start from a base image
FROM python:2.7-alpine

# Install empirical library
RUN apk add --update build-base 
# TODO: These should be replaced by pip install empirical
RUN pip install zerorpc 

# Add solver
COPY . /solver
WORKDIR /solver
ENTRYPOINT ["python", "solver.py"]

FROM rothnic/tinyconda:latest

COPY ./requirements.yaml /app/requirements.yaml
COPY ./fabfile.py /app/fabfile.py
WORKDIR /app
RUN conda install fabric && \
    fab install_run && \
    fab clean_conda

COPY ./example_conda_app /app/example_conda_app
COPY ./setup.py /app/setup.py
RUN python setup.py install

CMD ["run-the-app"]

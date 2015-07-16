FROM rothnic/tinyconda:latest

COPY ./requirements.txt /app/requirements.txt
RUN conda install --file /app/requirements.txt && \
    conda clean --yes --tarballs --packages

COPY . /app
WORKDIR /app
RUN python setup.py install

CMD ["run-the-app"]

FROM rothnic/tinyconda:latest

COPY . /app
WORKDIR /app
RUN conda build ./conda.recipe && \
    conda install --use-local example_conda_app && \
    conda clean --yes --tarballs --packages --source-cache

CMD ["run-the-app"]

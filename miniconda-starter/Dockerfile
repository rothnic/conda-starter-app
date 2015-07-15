FROM continuumio/miniconda

# COPY requirements file here
# would like to install app requirements here to use docker caching.
# would only run if the requirements file changes
# RUN conda install --file ./conda.recipe/meta.yaml
RUN conda install conda-build

COPY . /app
WORKDIR /app
RUN conda build ./conda.recipe && \
    conda install --use-local example_conda_app

CMD ["run-the-app"]

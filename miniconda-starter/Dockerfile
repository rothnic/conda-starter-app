FROM debian:jessie

# COPY requirements file here
# would like to install app requirements here to use docker caching.
# would only run if the requirements file changes
# RUN conda install --file ./conda.recipe/meta.yaml

RUN apt-get update && apt-get install -y --no-install-recommends wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 && \
    rm -rf /var/lib/apt/lists/*

ENV PATH=/opt/conda/bin:$PATH
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda-3.10.1-Linux-x86_64.sh && \
    /bin/bash /Miniconda-3.10.1-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda-3.10.1-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.14.1 && \
    find /opt/conda \
  		\( -type d -a -name test -o -name tests \) \
  		-o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
  		-exec rm -rf '{}' + && \
    conda install conda-build

COPY . /app
WORKDIR /app
RUN conda build ./conda.recipe && \
    conda install --use-local example_conda_app

CMD ["run-the-app"]

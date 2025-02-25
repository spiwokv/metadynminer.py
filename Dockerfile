FROM jupyter/base-notebook

RUN mkdir /tmp/build
COPY README.md meta.yaml setup.py /tmp/build/
COPY metadynminer/ /tmp/build/metadynminer/

RUN pip3 install /tmp/build

COPY python_metadynminer.ipynb /home/jovyan

RUN mamba install --yes ipywidgets ipympl 

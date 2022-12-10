FROM amazonlinux


RUN update-ca-certificates -f \
  && yum update \
  && yum upgrade -y \
  && yum install -y \
    software-properties-common \
    wget \
    git \
    libatlas3-base \
    libopenblas-base \
    libatlas-base-dev \
    build-essential \
  && yum clean



##### Install  rust



#### Install gcc



#### Install kubctl
https://hub.docker.com/r/bitnami/kubectl




#####################################################################################################
# Miniconda
ENV CONDA_DIR=/opt/miniconda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    chmod a+x miniconda.sh && \
    ./miniconda.sh -b -p $CONDA_DIR && \
    rm ./miniconda.sh && \
    conda install python=3.8.13


###### work folder  #############################################
WORKDIR /opt/work/ 


# RUN pip install --upgrade pip \
# RUN conda  install -c conda-forge -y 


COPY ./py38.txt   /opt/work/
RUN pip  install -r /opt/work/py38.txt



#####  Entry Point
# COPY bin/entrypoint.sh /usr/local/bin/
# COPY bin/vscode.sh /usr/local/bin/

#EXPOSE 8888
#VOLUME /notebooks
#WORKDIR /notebooks
ENTRYPOINT ["/bin/bash"]

\








FROM catthehacker/ubuntu:act-latest

# Install miniconda; act runner doesn't have it yet
ENV CONDA /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p $CONDA

# Put conda in path so we can use conda activate
ENV PATH=$CONDA/bin:$PATH


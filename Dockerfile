FROM ubuntu

RUN apt-get update \
    && apt-get -y install joe less python-pip


RUN pip install factom-api

WORKDIR /root
COPY python-scripts/* ./

ENV PATH="/root:${PATH}"

CMD ["/root/add_entry.py"]

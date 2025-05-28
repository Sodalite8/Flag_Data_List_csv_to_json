FROM python:latest

WORKDIR /workspace

COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt \
    && rm ./requirements.txt

CMD [ "/bin/bash" ]

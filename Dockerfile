FROM ubuntu:focal
WORKDIR /allwaves
RUN virtualenv -p /usr/bin/python3 .venv && . ./.venv/bin/activate
CMD [ "bash" ]
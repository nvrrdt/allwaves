### allwaves

#### Howto test

- Start eerst de servers op de 4 rpi
- Start dan de client op de 5de rpi

#### Files

- usage: python server.py: luistert op poort 10000
- usage: python client.py server_ip_1 server_ip_2 server_ip_3 server_ip_4: maakt connectie met servers op poort 10000, elk in een eigen process
- test files: voor als je op één commputer wil testen

#### Varia

sudo docker-compose run onzecurrency bash
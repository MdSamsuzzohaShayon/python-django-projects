# Django meet-up
 - [tutorial](https://www.youtube.com/watch?v=rDnWnQzTvGo),
[Install postgres on linux mint](https://www.tecmint.com/install-postgresql-with-pgadmin4-on-linux-mint/)
  ```
  sudo apt-get update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl status postgres
  sudo systemctl status postgresql
  sudo pg_isready
  sudo su postgres
  psql
  CREATE USER shayon WITH PASSWORD 'shayon';
  ```

 - [Install pgadmin](https://www.pgadmin.org/download/pgadmin-4-apt/)
  ```
  sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
  sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
  ls /etc/apt/sources.list.d
  sudo nano /etc/apt/sources.list.d/pgadmin4.list # CHANGE LINUX VERSION TO FOCAL
  sudo apt update
  sudo apt install pgadmin4
  sudo apt update && sudo apt upgrade -y
  ```
 - For the first time we need to set master password from postgres admin (pgadmin)
 - From pgadmin -> create a server -> name anything, connection give localhost -> 


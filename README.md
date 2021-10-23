## About The Project

Just wanted to do a simple Django App.

### Built With

* [Django](https://www.djangoproject.com/)
* [Postgres](https://www.postgresql.org/)
* [Redis](https://redis.io/)
* [Docker](https://www.docker.com/)
* [Spectre.css](https://picturepan2.github.io/spectre/)
* [Javascript Vanilla](http://vanilla-js.com/)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow the next instructions to run this project locally.

### Prerequisites

* python3
  ```sh
  sudo yum install python3
  ```

* pip
  ```sh
  sudo yum install --assumeyes python3-pip
  ```

* virtualenv
  ```sh
  sudo pip3 install virtualenv 
  ```

* docker

_Check instructions for your system: https://docs.docker.com/engine/install/_
_for Docker Composer: https://docs.docker.com/compose/install/_

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ArthurSStrong/djangochat.git
   ```
3. Install the needed containers
   ```sh
   docker-compose up -d
   ```
4. Create virtualenv
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
5. Install python dependencies
   ```sh
   pip3 install -r requirements.txt
   ```
6. Run DB migrations
   ```sh
   cd chat_app
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
7. Run Django App
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


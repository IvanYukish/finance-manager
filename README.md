###(branch 'dev' is actual branch for this app)
### Setup development environment
### Create Development Environment for finance-manager

#### Preparation 
Clone repository:

```bash
git clone https://github.com/IvanYukish/finance-manager.git
```

Go to the project folder:

```bash
cd finance_manager
```

Install Docker, 
instruction for [Mac](https://docs.docker.com/docker-for-mac/install/)
and [Ubuntu](https://docs.docker.com/engine/install/ubuntu/).
For Ubuntu you must install [docker-compose](https://docs.docker.com/compose/install/) separately.

Install PostgresSQL client, on Mac:
```bash
brew install libpq
```

Install PostgresSQL client, on Ubuntu:

```bash
sudo apt install -y postgresql-client
```


### First Launch
Create environment variables file:
```bash
cp env.example .env
```
Edit this file according to your needs.

Launch docker-compose:
```bash
docker-compose up -d --build
```

```bash
docker-compose exec django python manage.py migrate
```

Restart project:
```bash
docker-compose down
docker-compose up -d
```

Finance-Manager project is going to be available on http://127.0.0.1:8000

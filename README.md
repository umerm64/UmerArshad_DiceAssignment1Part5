# UmerArshad_DiceAssignment1Part5
Multi-Container Application Deployment using Docker Compose

# Step 1
Dockerfileweb is created for the web application.
`docker build -f Dockerfileweb -t web .`

# Step 2
Dockerfilepostgres is created for postgres database.

# Step 3
docker-compose.yml file is created with web and db services.

# Step 4
`docker-compose up -d`
The web app is accessible on `localhost:5000`

# Step 5
Dockerfileweb is changes and instead of running app.py I printed the value of env variable and verified in logs.

# Step 6
volume `db-data` is added in docker-compose.yml and mounted within the db container.

# Step 7
The scaling is done by using nginx as a load balancer.
The dockerfile and conf files are present under nginx folder.

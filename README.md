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


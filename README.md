# IAG Benefits, LLC Maintenane Container (iagllctech/devops-challenge-postgresql-backend)

PostgreSQL backend for IAG's devops challenge.

## Getting Started

This container provides a PostgreSQL python backend used as part of IAG's devops interview process.  The container is to be paired with its [frontend container](https://hub.docker.com/repository/docker/iagllctech/devops-challenge-frontend).

The container provides a backend that listens on port 8000 and connects to a PostgreSQL database (connection controlled via environment variables described below). If you wish to see the application, you can clone the repository, and run the docker-compose file located in the repositories root.

### Prerequisities

In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Environment Variables

| Variable Name | Description | Default |
| --- | --- | --- |
| DB_NAME | The name of the database we are connecting to. | `postgres` |
| DB_USER | The username to connect to the database with. | `postgres` |
| DB_PASS | The password to connect to the database with | `password` |
| DB_HOST | The DNS name or IP address of the database server. | `localhost` |
| DB_PORT | The port the database listens on. | `5432` |

## Built With

* nginx:alpine (latest at time of build)

## Find Us

* [Github](https://github.com/iagtech/devops-challenge-postgresql)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/iagtech/devops-challenge-postgresql/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/iagtech/devops-challenge-postgresql/tags). 

## Authors

* **Ethan McGee** - *Initial work* - [bulletshot60](https://github.com/bulletshot60)

See also the list of [contributors](https://github.com/iagtech/devops-challenge-postgresql/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/iagtech/devops-challenge-postgresql/blob/main/LICENSE.md) file for details.

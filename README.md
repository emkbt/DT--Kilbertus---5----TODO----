# Todo List Application

A simple console-based Todo List application where you can add, delete, complete tasks.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.12
- datetime library for Python

### Installing

A step-by-step guide to getting a development environment running:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/emkbt/DT--Kilbertus--5--ToDoList--

2. Navigate to the project directory.

   ```bash
   cd DT--Kilbertus--5--ToDoList--

3. Run the project.

   ```bash
   python todo_app.py

## Running the tests

Currently, this project does not have automated tests. However, you can manually test the functionality by running the application and checking if the basic operations (adding, deleting, completing tasks) work as expected.

### Break down into end to end tests

The manual tests cover the following scenarios:

- **Adding a Task:**
  - Enter a task, and verify that it is added to the list.

- **Deleting a Task:**
  - Enter an existing task, and verify that it is removed from the list.

- **Completing a Task:**
  - Enter an existing task, and verify that it is marked as complete.

## API Usage

A REST API was implemented into this project by [waternewt](https://github.com/waternewt). This API was built using the Flask framework. All of the routes take in the `api_key` paramater.

### Importing into Postman

You can use the postman json (`Todo List.postman_collection.json`) in the *Testing* folder, to import this project into Postman. This postman json will include example usages on each of the routes/methods.

### Authenticate

This route tests if the API key is a valid one. Here is an example:

***Example Input***
```bash
curl --location 'http://127.0.0.1:8000/auth?api_key=83a426cd48bdbae86c217bf2217bd038'
```

***Example Output***
```json
{
    "status": 200,
    "success": true,
    "username": "demo"
}
```

### Adding a task

The route `/add` only accepts the method `PUT` request method. It takes in one required `description` header, and one optional `due_date` header.

***Example Input***
```bash
curl --location --request PUT 'http://127.0.0.1:8000/add?api_key=83a426cd48bdbae86c217bf2217bd038' \
--header 'description: Study' \
```

***Example Output***
```json
{
    "completed": false,
    "description": "Study",
    "due_date": null,
    "status": 200,
    "success": true
}
```

### Get tasks

The route `/tasks` only accepts the `GET` request method. It (just like all the other routes), takes in the `api_key` paramater.

***Example Input***
```bash
curl --location 'http://127.0.0.1:8000/tasks?api_key=83a426cd48bdbae86c217bf2217bd038'
```

***Example Output***
```json
{
    "status": 200,
    "success": true,
    "tasks": [
        {
            "completed": true,
            "description": "Study",
            "due_date": null
        },
        {
            "completed": false,
            "description": "Homework",
            "due_date": null
        }
    ]
}
```

### Delete task

The route `/delete` only accepts the `DELETE` request type.

***Example Request***

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/delete?api_key=83a426cd48bdbae86c217bf2217bd038' \
--header 'description: Study'
```

***Example Response***

```json
{
    "status": 200,
    "success": true
}
```

### Completing a task

The route `/complete` only accepts `POST` request method. It accepts the required `description` header, and the optional `due_date` header.

***Example Request***

```bash
curl --location --request POST 'http://127.0.0.1:8000/complete?api_key=83a426cd48bdbae86c217bf2217bd038' \
--header 'description: Study'
```

***Example Response***

```json
{
    "status": 200,
    "success": true
}
```

### Coding style tests

Since this is a simple console application, formal coding style tests may not be necessary. However, it's a good practice to follow PEP 8 or other relevant style guides.

## Built With

* [Python](https://docs.python.org/release/3.12.1/) - The programming language used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/emkbt/DT--Kilbertus--5--ToDoList--/tags). 

## Authors

* **Emma Kilbertus** - *Initial work* - [emkbt](https://github.com/emkbt)
* **Raphael Michon** - *Added features*
* **Yunus Ruzmetov** - *Created the REST API*

See also the list of [contributors](https://github.com/emkbt/DT--Kilbertus--5--ToDoList--/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 

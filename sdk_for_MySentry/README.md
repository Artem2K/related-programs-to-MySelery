This library is designed to interact with the MySentry project.
To work with this package, you need to register your application in the MySentry project and get your unique "id" and "token".
Install this library in the virtual environment of your project
Create the file "MySentrySettings" in the root folder of your project and fill it in the format:

settings = dict(
    id='your unique id'->int,
    token='your unique token'->str,
)

To start collecting error statistics in the MySentry project database, use the "@error_searcher" decorator in the places you need
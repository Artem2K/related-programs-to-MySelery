To work with this package, you need to register your application in the MySentry project and get your unique "id" 
and "token". Install this library in the virtual environment of your project:

1. python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps MySentry-pkg-Artem2k==0.0.3 

2. Create the file "MySentrySettings" in the root folder of your project and fill it in the format:

3. Settings = dict( 
    id='your unique id'->int, 
    token='your unique token'->str, 
   )

4. To start collecting error statistics in the MySentry project database, use the "@error_searcher" decorator in the 
places you need.

5. use the "pytest tests/test_sdk.py" to run the tests
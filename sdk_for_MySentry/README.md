# sdk_for_MySentry

# Overview
    Python 3.6.8
    
# Install

    $ git clone https://github.com/Artem2K/related-programs-to-MySelery/tree/master/sdk_for_MySentry
    
# Usage
    
    $ cd ProjectName
    
    $ pipenv install
    
    $ pipenv shell
    
    $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps For-MySentry-pkg-Artem2k==0.0.1
    
    $ http://127.0.0.1:8000/signup/ - registration

    $ http://127.0.0.1:8000/users/login/ - login
    
    $ http://127.0.0.1:8000/apps/register_app/ - register your app
    
    $ http://127.0.0.1:8000/apps/ - save "id' and "token"
 
    $ pipenv touch MySentrySettings.py - example:
        
        https://github.com/Artem2K/related-programs-to-MySelery/blob/master/test_error_scripts/MySentrySettings.py
    
    $ .py: from sdk_for_MySentry_pgk.sdk import error_searcher - use the "@error_searcher" decorator in the 

        places you need.
        
    



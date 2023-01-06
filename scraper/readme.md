What is Localhost (IP 127.0 0.1)? Localhost is the default name of the computer you are working on. The term is a pseudo name for 127.0. 0.1, the IP address of the local computer. This IP address allows the machine to connect to and communicate with itself.

Views and URLS
When someone types a url on the web, it goes to the urls.py and looks at the paths (the first arguement in path is the urls name ex. ...com/home or home and the 2nd arguement is the name of the function in views.py) and the the matching path will send them to views.py function, views.home and return whatever is written under that function.
When a web request is made to the application, Django's URL configuration takes care of routing the request to the appropriate view function to process the request.
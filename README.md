# Internet of Utilities

Internet of Utilities (which will be shortented to IoU from now on) is a tool for a variety of utilities, including
Roundbottom (or `Rndb`), a WIP flask extension and IDL, a very simple tool similar to `wget`.

## Using Roundbottom
To make a simple roundbottom program, run the following code:
```
rndb = Rndb()
Rndb().run_app(torun=Rndb.helloworld)

# or, for all the arguments

rndb = Rndb()

rndb.run_app(host="localhost", port=8000, route="/")

```

compared to the longer
```
from flask import Flask

app = Flask(__name__)



@app.route('/')

def hello_world():

    return 'Hello, World!'
	
```

The `Rndb.helloworld` is an example program ran if no function to run was given, and is defined as:
```
def helloworld():

    return 'Hello, World!'
	
```

If you want to use a custom function that *you* defined, use the following:
```

def test123():

    return 'Hello, other world!'
	

rndb = Rndb()

rndb.run_app(host="localhost", port=8000, torun=test123, route="/")

```

Let's step through the program.

```
rndb = Rndb()
rndb.run_app(host="localhost", port=8000, torun=Rndb.helloworld, route="/")

```


`rndb = Rndb()` instantiates Roundbottom, for the use of `run_app`

`rndb.run_app` runs an application with the following arguments:

`host="localhost"` is used to define the host. For a local webserver, use `localhost`. For a repl-like website, (e.g. [repl.it](https://repl.it/))
use something like `0.0.0.0`

`port=8000` defines the port. You can have 8080, 8000, 6000, etc.

`torun=Rndb.helloworld` defines which function to run. In this case, it runs the example program `Rndb.helloworld`, which just
does `return "Hello, World"`.

`route="/"` simply puts @app.route(route) before the function you provided with `torun`.

## Using IDL

IDL is a simple function with one argument using one library; `urllib`.
The function is like `idl(url)`.
Replace `url` with a URL, and you will get the text content for the URL's page.



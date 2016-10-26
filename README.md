# Onshape Robot Tools
Robot tools for use with the Onshape CAD program.


# Installation

Download the onshape apikey library and setup a virtualenv as described here: https://github.com/onshape-public/apikey/tree/master/python

Too make that work on ubuntu 16.04, I first had to run:
```
sudo apt-get install libncurses5
```

This package uses the `requests` library.

```
sudo apt-get install python-requests
```

In order to get permission to read your documents, an API key is needed. In the
onshape developer portal, create an API key that has read access to documents.
Then create a file called `~/.config/onshape_robot_tools/config.yml` with the
following contents.

```
api_access_key: <access key>
api_secret_key: <secret key>
```


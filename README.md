# Mongo Copy

## Setup

The setup is straightforward. Clone the project, install the packages, and you are ready. Please consider using a virtual
environment to keep clean your local environment.

```commandline
pip install -r requirements.txt
```

## Usage

First four input arguments are required:

1. MongoDB hostname
2. MongoDB port
3. MongoDB database
4. MongoDB collection

The fifth is optional:

5. String containing a `dict` for filtering the collection

## Examples

### Return the whole collection

If you are trying to access a collection named `collection` in a database named `database` you can use the following:

```commandline
python main.py localhost 27017 database collection
```

The output is a sequence of documents, one for each line. You can pipe the output and save it to a file, if you prefer.

### Filter the collection

If you want to filter the content of a collection, getting only elements with `{"id": 1}`, use the following syntax:

```shell
python main.py localhost 27017 database collection "{\"id\": 1}"
```

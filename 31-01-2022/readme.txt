*To add default value to query parameters we have to enclose the function in a second decorator
and pass the default values of the query parameters as a dictionary with the variable names and
their values as keys and values of the dictionary.

*request.args.get() - to be used when trying to access query string variable
*request.form[] - to be used when trying to pass data in a form
*request.get_json - to be used when trying to pass data in json format in body of request

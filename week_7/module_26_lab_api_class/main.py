from flask import Flask, request

app = Flask(__name__)

database = {"sayem" : "25", "rafik" : "35"}

@app.route("/", methods=["GET"])
def home() :
    return "welcome to the home page"

@app.route("/getdata", methods=["GET"])
def get_data() :
    return database

# https://www.google.com/search?

@app.route("/adddata/", methods=["GET", "PUT"])
def add_data() :
    key, value = list(request.args.items())[0]
    if key in database :
        return f"this {key} username is already exist"
    database[key] = value
    return database

@app.route("/updatedata/", methods=["GET", "PUT"])
def update_data() :
    key, value = list(request.args.items())[0]
    if key in database :
        database[key] = value
        return database
    return f"sorry, this {key} user is not exist in our database"


@app.route("/deletedata/", methods=["GET", "DELETE"])
def delete_data() :
    key, value = list(request.args.items())[0]
    if value in database :
        database.pop(value)
        return database
    return f"this {value} doesn't exist in our database. Hence, you can't delete the user."



if __name__ == "__main__" :
    app.run()
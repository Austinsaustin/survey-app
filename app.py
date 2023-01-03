from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3



app = Flask(__name__)
# con = sqlite3.connect("tutorial.db",check_same_thread=False)
# cur = con.cursor()

#variables for testing sqlite3 syntax
# b = "cool"
# w = 12
# d = 5
# k = "wow"

app.debug = True

def create_table(column_list, data_type):
    # Create a connection to the database
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    # Create a string for the column definitions
    column_defs = ", ".join([f"{column} {data_type[i]}" for i, column in enumerate(column_list)])

    # Create the table
    c.execute(f"CREATE TABLE wowzaaa ({column_defs})")

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
# create using table name, and columns as a variable
# cur.execute("CREATE TABLE" + " " + k + "(" + "" +  b + "," + " year, score)")


 
# insert using table name as a variable
# cur.execute("INSERT INTO" + " " + k  + " " + "VALUES(?,?,?)", (b, w , d))

# insert using column values as variables
# cur.execute("INSERT INTO wow VALUES(?,?,?)", (b, w , d))



@app.route("/" ,methods=["GET", "POST"])
def render():
        return render_template("index.html")

@app.route("/table", methods=["GET", "POST"])
def render2():

    if request.method == "POST":
        col_list = request.form.getlist("name")
        col_list = list(filter(None, col_list))
        data_type = request.form.getlist("data")
        create_table(col_list, data_type)
       
        return render_template("test.html")
        
    else:
        return render_template("table.html")





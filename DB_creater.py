import sqlite3
import json
import re

handle = open('GetEdge.json')
contents = handle.read()
handle.close

data_object = json.loads(contents)

# getting the Schema
def get_all_the_attributes(data_object: dict) -> list:
    Schema = []
    for i in data_object:
        for j in i:
            if j not in Schema:
                Schema.append(j)
    return Schema

def get_type(t):
    Dict = {int: "integer", str: "text", type(None): "text", bool: "boolean"}
    return Dict[t]

# making the connection
conn = sqlite3.connect("VM-wareDB.db")

# making the table
if conn:
    cursor = conn.cursor()

    # making the SQL query
    middle = ""
    Schema = get_all_the_attributes(data_object)
    for i in Schema:
        middle += f"    {i} {get_type(type(data_object[0][i]))} NOT NULL,\n"
    whole = re.sub(",\n$", "\n", middle) + ");"
    whole = "CREATE TABLE IF NOT EXISTS EDGES (\n" + whole
    try:
        cursor.execute(whole)
    except:
        print("something went wrong:\n")
        print(whole)


# going through and populating the tables
if conn:
    for i in data_object:
        question_marks = "("
        Satisfies = []
        # makes a list out of the elements of the current edge
        for j in Schema:
            question_marks += "?,"
            if j in i and i[j]:
                Satisfies.append(i[j])
            else:
                Satisfies.append("")

        # makes a tuple of the list
        Data = [tuple(x for x in Satisfies)]
        
        # finishes the query statement
        question_marks = re.sub(",$", ")", question_marks)
        question_marks = "INSERT INTO EDGES VALUES " + question_marks
        conn.executemany(question_marks, Data)
        conn.commit()
    conn.close()
        


The purpose of this script is simple.

This script called DB_creater.py takes a json file as input
    (the source of the json file is a request made by the Postman App to VMware SD-WAN by VeloCloud)    
    (the json file must be renamed GetEdge.json)

and uses sqlite to make an SQL Database with the filename VeloCloudDB.db

The ChangeValue.py script changes the values of the dictionaries
stored in the GetEdge json file



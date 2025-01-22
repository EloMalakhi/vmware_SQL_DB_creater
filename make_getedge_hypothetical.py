
import random, json, re, time, string
# GetEdge was sensitive data, so this script changed the confidential values to hypothetical values




characters = string.ascii_letters + string.digits + "-_:;" # choose characters allowed in the word
random_word = ''.join(random.choices(characters, k=20)) # randomize 20 of them to make a word



def randomstring():
    characters = string.ascii_letters + string.digits + "-_:;" # choose characters allowed in the word
    return ''.join(random.choices(characters, k=20)) # randomize 20 of them to make a word

handle1 = open('GetEdge.json') # open json file
content = handle1.read() # read it
handle1.close() # close it
data_obj = json.loads(content) # load data structure






time.sleep(.1) # sleep to make sure reading is finished before writing
handle2 = open("GetEdge.json", 'w') # writing



localDict = {int:random.randint(1,99999), str:randomstring(), bool:random.choice([True, False])} # data replacement Dict
for i in data_obj: # going through data structure
    for j in i: 
        i[j] = localDict[type(i[j])] if i[j] else None # replacing data with random values of correct data type


contents2 = json.dumps(data_obj, indent=2)
handle2.write(contents2)
handle2.close()
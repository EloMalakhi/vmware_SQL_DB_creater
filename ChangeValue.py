
import random
import json
import re
import time

def randomstring():
    stir = ""
    for i in range(20):
        stir += random.choice("a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 - _ : ;".split())
    return stir



handle1 = open('GetEdge.json')
content = handle1.read()

handle1.close()
data_obj = json.loads(content)

def replace(string):
    numberType = [
    "MainframeId",
    "API_isLive",
    "problematicCaptions",
    "errorMSG",
    "isLiveId",
    "enterpriseId"
    ]

    characterType = [
    "deviceSpecificInfo",
    "last_osUpdate",
    "firewall_connection",
    "IssuedSerNumber",
    "MFlast_Tech_supported",
    "lastConnCondition",
    "currentConn",
    "MF_pki_mode",
    "TechSupportType",
    "last_Tech_supported",
    "days_since_TechSupp",
    "days_since_reboot",
    "time_since_creation",
    "first_IP_Conn",
    "date_created",
    "operationSymbol",
    "operationSymbolExpires",
    "sessionType",
    "sessionInterval",
    "DjangoRunning",
    "hardwareId",
    "Mainframe_version",
    "CPU_company_Id",
    "Azure_version",
    "os_type",
    "Api_Retrieval_version",
    "IP",
    "PossibleUpdates",
    "IP_addr",
    "itshost",
    "rationalNumber",
    "serialNumber",
    "modelNumber",
    "averageDataClass",
    "deviceName",
    "definingText"
    ]

    boolType = [
    "maskSequence"
    ]

    nullType = [
    "AzureSystem",
    "currentGlobalPosition"
    ]

    if string in numberType:
        return random.randint(1, 99999)
    elif string in characterType:
        return randomstring()
    elif string in boolType:
        return random.choice([True, False])
    elif string in nullType:
        return None

time.sleep(.1)



handle2 = open("GetEdge.json", 'w')




for i in data_obj:
    for j in i:
        i[j] = replace(j)

contents2 = json.dumps(data_obj, indent=2)
handle2.write(contents2)
handle2.close()
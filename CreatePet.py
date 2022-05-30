from utilities.configurations import *

def addpet(id):
    createpet = {
        "id": id,
        "name": "tom",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    return createpet
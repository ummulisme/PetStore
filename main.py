import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *



#url = 'https://petstore3.swagger.io/api/v3/pet/1'
req = requests.get(getConfig()['API']['url']+'/1',verify=True)
print(req.status_code)


## add a new pet to the store
#url = 'https://petstore3.swagger.io/api/v3/pet'
headers = {'Content-Type' : 'application/json'}
NewPetReqBody = {
  "id": 99,
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
NewPetReq =  requests.post(getConfig()['API']['url'],headers=headers, json = NewPetReqBody,)

assert NewPetReq.status_code == 200
print(NewPetReq.status_code, NewPetReq.text)

##Update an existing Pet

import requests
import json

#url = 'https://petstore3.swagger.io/api/v3/pet'
#headers = {'Content-Type' : 'application/json'}
NewPetReqBody_update = {
  "id": 99,
  "name": "harry",
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
NewPetReq =  requests.put(getConfig()['API']['url'],headers=headers, json = NewPetReqBody_update,)





##deleting a pet
import requests
import json

#url = 'https://petstore3.swagger.io/api/v3/pet/99'
#headers = {'Content-Type' : 'application/json'}
Del_Pet =  requests.delete(getConfig()['API']['url']+ '/99',headers=headers,)
Del_Pet_Response = "Pet deleted"
print(Del_Pet.status_code,Del_Pet.text)
assert Del_Pet.status_code == 200
assert Del_Pet.text == Del_Pet_Response

##access url and return pet inventories by status



#upload image of  a pet

#url ='https://petstore3.swagger.io/api/v3/pet/1/uploadImage'
imageparams = {'additionalMetadata' : 'phototoest'}
image = {'file': open('pet.png' , 'rb')}
UploadImage = requests.post(getConfig()['API']['url']+ '/1/uploadImage',params=imageparams, files = image)
print(UploadImage.status_code)
##get pet by availabale status
import requests
import json

#url = 'https://petstore3.swagger.io/api/v3/pet/findByStatus'
params = {'status':'available'}
#headers = {'Content-Type' : 'application/json'}
Get_by_status =  requests.get(getConfig()['API']['url']+ PetResource.petbyStatus,params =params)
print(Get_by_status.status_code,Get_by_status.text)

##get pet by id
import requests
import json

#url = 'https://petstore3.swagger.io/api/v3/pet/99'
headers = {'Content-Type' : 'application/json'}
Get_by_id =  requests.get(getConfig()['API']['url'] + '99')
print(Get_by_id.status_code,Get_by_id.text)



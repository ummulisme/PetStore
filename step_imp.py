import requests
from utilities.CreatePet import addpet
from utilities.resources import *
from utilities.configurations import *


@when('A New Pet is added to the Store')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json'}
    context.NewPetReqBody = {
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
    context.NewPetReq = requests.post(getConfig()['API']['url'], headers=context.headers, json=context.NewPetReqBody, )

@then('Pet is Successfully created')
def step_impl(context):
    assert context.NewPetReq.status_code == 200
    print(context.NewPetReq.status_code, context.NewPetReq.text)
@then('Add an image of the Pet')
def step_impl(context):
    context.imageparams = {'additionalMetadata' : 'phototoest'}
    context.image = {'file': open('pet.png' , 'rb')}
    context.UploadImage = requests.post(getConfig()['API']['url']+ '/1/uploadImage',params=context.imageparams, files = context.image)
    print(context.UploadImage.status_code)
@then('Verify the Pet using the Status')
def step_impl(context):
    context.params = {'status':'available'}
    #headers = {'Content-Type' : 'application/json'}
    context.Get_by_status =  requests.get(getConfig()['API']['url']+ PetResource.petbyStatus,params =context.params)
    print(context.Get_by_status.status_code,context.Get_by_status.text)
@given('Pet {id} is created using form')
def step_impl(context,id):
    context.form_headers = {'Content-Type' : 'application/x-www-form-urlencoded"'}
    context.NewPetMoreReqBody =addpet(id)
    context.Addpet_Resp = requests.post(getConfig()['API']['url'], headers = context.form_headers,json = context.NewPetMoreReqBody)
    context.tagsname = context.NewPetMoreReqBody["tagname"]
@when('find pet by tag name and validate the data')
def step_impl(context):
    context.tagsparam = {'tags': context.tagsname["name"]}
    context.Get_by_Tags = requests.get(getConfig()['API']['url'] + PetResource.petbyTags, headers=context.headers,
                                       params=context.tagsparams)
    print(context.Get_by_Tags.status_code, context.Get_by_Tags.text)
    assert context.Get_by_Tags.status_code == 200

@then('Delete the pet by using pet id')
def step_impl(context):
    context.Del_Pet =  requests.delete(getConfig()['API']['url']+ '/99',headers=context.headers,)
    context.Del_Pet_Response = "Pet deleted"
    print(context.Del_Pet.status_code,context.Del_Pet.text)
    assert context.Del_Pet.status_code == 200
    assert context.Del_Pet.text == context.Del_Pet_Response
@when ('Update Pet Update url is accessed and invalid pet is passed')
def step_impl(context):
    context.NewPetReqBody_update = {
    "id": 99999,
    "name": "winnies",
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
    "status": "available"         }

    context.NewPetReq =  requests.put(getConfig()['API']['url'],headers=context.headers, json = context.NewPetReqBody_update,)
    #NewPetReq =  requests.put(url, json = NewPetReqBody,)
    print(context.NewPetReq.status_code, context.NewPetReq.text)

@when('Pet doesnot exist error 400 should be found')
def step_impl(context):
  assert context.NewPetReq.status_code == 404

@when('User finds invalid tag value to find the pet')
def step_impl(context):
    context.tagsparams = {'tags':'valuedoesnotexistdatatest'}
    context.Get_by_Tags=  requests.get(getConfig()['API']['url']+ PetResource.petbyTags,headers = context.headers, params = context.tagsparams)
    print(context.Get_by_Tags.status_code,context.Get_by_Tags.text)

@then('Give 400 Error Tag value doesnot exist')
def step_impl(context):
    assert context.Get_by_Tags.status_code ==400

@given('User is login with valid credentials')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json'}
    context.auth ={'username':'user1','password':getpassword()}
    context.userloginres = requests.post(getConfig()['LOGIN']['loginurl'], auth=context.auth, headers=context.headersheaders, verify=False, )
    assert context.userloginres.status_code == 200

@when('User access pet store and finds pet inventories by status')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json'}
    context.AccessPetStore = requests.get(getConfig()['PETSTORE']['petstore_url'] + '/inventory',headers = context.headers)
	assert context.AccessPetStore.status_code ==200
	print(context.AccessPetStore.status_code,context.AccessPetStore.text)

@then('Post a New Order for Pet')
def step_impl(context):
    context.OrderBody = {
        "id": 10,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2022-05-29T15:56:28.310Z",
        "status": "approved",
        "complete": True
    }
    PetOrderResponse = requests.post(getConfig()['PETSTORE']['petstore_url'] + '/order', headers=headers, json=context.OrderBody, )
    assert context.PetOrderResponse.status_code == 200

@then('User Get the purchase order by passing invalid order id')
def step_impl(context):
    context.orderid = context.OrderBody["id"]
    context.PetOrderidResponse = requests.get(getConfig()['PETSTORE']['petstore_url'] + '/order' + '/9999', headers=context.headers)

@then('Give Error Order not found')
def step_impl(context):
    assert context.PetOrderidResponse.status_code == 404
    assert context.PetOrderidResponse.text  == 'Order not found'

@then('Delete the valid purchase order')
def step_impl(context):
    context.orderid = context.OrderBody["id"]
    context.PetOrderidResponse = requests.delete(getConfig()['PETSTORE']['petstore_url'] + '/order' + '/context.orderid', headers=context.headers)
    assert context.PetOrderidResponse.status_code == 200

@then('And User logs out')
def step_impl(context):
    context.userlogout = requests.get(getConfig()['LOGIN']['logout'], headers=context.headers, )
    assert context.userlogout.status_code == 200

@('Admin update user using username that doesnot exist')
def step_impl(context):
context.userbody = {
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
updateresponse = requests.put(getConfig()['LOGIN']['modifyuserurl'] + '/tilak',json = context.userbody)


@then('Assert error Response')
def step_impl(context):
    assert updateresponse.status_code== 404
    assert updateresponse.text == 'User not found'

@then('Delete User that doesnot exist, validate the error')
def step_impl(context):
    context.deleteuser = requests.delete(getConfig()['LOGIN']['modifyuserurl'] + '/tilak',)

@then('validate asserting message user doesnot exist')
def step_impl(context):
    assert updateresponse.status_code== 404
    assert updateresponse.text == 'User not found'


@when('User tries to login using invalid credentials')
def step_impl(context):
    context.headers = {'Content-Type': 'application/json'}
    context.auth ={'username':'userdoesnotexist','password':getpassword()}
    context.userloginres = requests.post(getConfig()['LOGIN']['loginurl'], auth=context.auth, headers=context.headersheaders, verify=False, )
@then('Invalid username/password supplied message')
def step_impl(context):
    assert context.userloginres.status_code == 400
    assert context.userloginres.text == 'Invalid username/password supplied'
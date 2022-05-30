About PetStore Application

PetStore is an application that is used to Manage  Pet details , Pet Store Inventory and User Access Management 

Reference Swagger  : 
 https://petstore3.swagger.io/
 
### Pet data management
 Description : Create, Upload image, Search or Delete Pet profile 
* POST / Add an new pet to the store
*PUT /Update an existing Pet by ID
* GET /pet/{petId} Find pet by ID
* DELETE /pet/{petId} Delete a pet by ID
* POST /put/{petId}/uploadImage upload an Image

### Pet Store Inventory
  Description : Place New Order for Pet and Delete Order
* POST /store/order Place an order for a pet
* GET /store/order/{orderid} Find purchase order by ID
* DELETE /store/order/{orderId} Delete purcahse order by ID
* GET /store/inventory Return pet inventories by status

### User Access Management
  Description : Managing User data
* POST /user Create user
* GET /user/{username} Get user by username
* PUT /user{username} Updated user
* DELETE /user/{username} Delete User
* GET /user/login - Logs user into the system
* GET /user/logout - Logs out current logged in user session

### Prerequisite : 
> Python 3
> 
> Behave
> 
> IDE : Pycharm
> 
### How to write new tests ?

1. Create new feature file in an existing feature file with Valid Data
2. Add new methods with Given, When and Then Annotation in  Step Definition class file.

### How to run the feature files ?

1.To run a specific scenario: behave -n "scenario name"

2.To run a feature file: behave "feature name.feature"

3.To run multiple feature file behave "feature name one .feature" "feature name two .feature"

### Project Structure

+ feature 

  + steps
    + step definition file
  + feature files
+ utilities
  + configurations
  + properties
  + resources
  + Testdata

About PetStore Application

PetStore is an application that is used to Manage  Pet details , Pet Store Inventory and User Access Management 

Reference Swagger  : 
 https://petstore3.swagger.io/

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
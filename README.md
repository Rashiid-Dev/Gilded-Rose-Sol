
# Gilded-Rose-Sol (pre-refactoring)
> This will explain the steps I took to solve this Kata

## Why does this code need to be changed?
At it's current state the program is inflexible as all the bussiness rules were in one class and it was difficult to read because of the multiple "if then else" statements and all the nestings. Any introduction of a new product would require the modificication of the class because the product names are mentioned in the "if" statements, this could break the existing logic.

I have refactored the code by creating classes that inherit the "Items" class and apply the bussiness rules in those classes. This leads to the code being more readable and easy to understand. Any new product that follows the existing business rules can make use of the existing classes and new products that require new bussiness rules can be easily introduced by creating a new class which inherits the "Item" class. This leads to the exisiting code requiring no modification and eliminates the possibility to breaking code used by previous products.

## gilded_rose.py

I have added 3 classes to this file:

#### Generic_depriciate
Which handles the depreciation of all the normal items 

#### Cheese_appriciate
Which handles the appreciation of products such as "Aged Brie"

#### Pass_appriciate
Which handles appreciation of the "Backstage passes"

## texttest_fixture
I have modified the "items" list so that the products use the proper class

## test_gilded_rose.py
I have added several tests to test the new product throughout several days

Golden_Master.txt and New_Output.txt were created to test the output of before the code refactoring and after.

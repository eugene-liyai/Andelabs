# Andelabs
Andela Lab exercises. The lab tests are meant to tests ones comprehension of the basic python skills while observing particular development practices.

## Car Class Lab
The car lab challange requires defaults when initializing the `Car()` class. Defaults consists of the car name and model. Using this parameters, the class is able to instantiate other parameters such as the number of dorrs, number of wheels and the car type.

```python
def __init__(self, name='General', model='GM', _type=None):
        # default speed of a parked car
        self.name = name
        self.model = model
        self.speed = 0
        self.num_of_doors = 4
        self.model = model
```

The code passes all test and execute as expected.

## Data Types Lab

The data type exercise simply checks the input variables are members of the intended data type

```python
  
  isinstance(True, bool)
  isinstance(8, int)
  isinstance([1, 2, 3], list)
  
```
The code passes all test and execute as expected.

## Find Minimum and Maximum values

The exercise tests ones programming logic and the best way to face a particular programming problem. The code is expected to loop through a list and retrive both the minimum and maximum value, which is later returned as a list.

```python

  def find_min_max(num_list):
    ...
    return [min, max]
```
The code passes all test and execute as expected.

## Fizz-Buzz Challange

The task also assesses the programming logic. The code is expected to check is an input (which has to be an integer), is divisible by three, five or both. The code returns fizz if number is divisible by 3, Buzz if divisible by 5 and fizzbuzz if its divisible by both

```python
  
  def divisible_by_three_and_five():
    return 'fizzbuzz'
  def divisible_by_three():
    return 'fizz'
  def divisible_by_five():
    return 'buzz'

```


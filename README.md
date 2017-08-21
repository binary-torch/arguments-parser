# Binary Torch Sdn. Bhd.

## ArgumentsParser

> Content

Custom ArgumentsParser to make the process of adding terminal args fast and easy.

> Usage

```python
# step 1: import statement
from ArgumentsParser import ArgumentsParser

# step 2: Define your arguments
args = [
	{
		"name" : "traning",
		"help" : "Path to traning data",
		"required" : True
	},
	{
		"name" : "testing",
		"help" : "Path to testing data",
		"required" : True
	}
]

# step 3: create the object and call setup method
argumentsParser = ArgumentsParser()
argumentsParser.setup(args)

```
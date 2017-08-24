# Binary Torch Sdn. Bhd.

## ArgumentsParser

> Content

Custom ArgumentsParser to make the process of adding terminal args fast and easy.

> Usage

- step 1: import statement

```python
from ArgumentsParser import ArgumentsParser
```

- step 2: Define your arguments

```python
args = [
	{
		"name" : "traning",
		"help" : "Path to traning data",
		"required" : True
	},
	{
		"name" : "testing",
		"help" : "Path to testing data",
		"required" : False
	}
]
```

- step 3: create the object and call setup method

```python
argumentsParser = ArgumentsParser()
data = argumentsParser.setup(args)
```

- step 4: run from terminal:

```python
python filename.py --traning traningpath --testing testingpath
```

- step 5: accessing data
```python
print(data["traning"])
```
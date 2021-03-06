# DeDuplicator

### Overview
You can see how the `deduplicate_list()` is used in `main.py` but function definitions
can be found in `utils.py`. If you want to see the generated original list with duplicate
emails and the deduplicated list you can go to `main.py` and uncomment the following lines

```
# print(emails)
# print(utils.deduplicate_list(emails))
```

you can also set the `cycles=1` to reduce the test cycles. Unit Tests can be found inside `tests`
folder

### Prerequisites on MacOs
You need to have pipenv & pyenv installed which is the dependency manager and python version manager respectively.
To install pipenv run the following command
```
brew install pipenv
```

To install pyenv run the following command
```
brew install pyenv
```

When you have pyenv successfully installed you need to setup python version 3.8.6. on your system. Please
run the following commands to install & set specific python version on your machine

```
pyenv install 3.8.6
```

The command above will install the specific python version. But you need to run another command
to use that specific python version. Run the below command to
set 3.8.6 version of python on your terminal

```
pyenv global 3.8.6
```

You can now clone this git repo
```
git clone https://github.com/kyleoropesa/deduplicator.git
```

And then run the following command to install it's dependencies and a sandbox
environment of your project
```
pipenv install
```

### Running the tests
Unit Tests are found inside the `tests` directory you can run them by just running
```
pipenv run pytest
```

### Running the script
The function `deduplicate_list()` accepts a list of items that removes duplicates but
retains the first instance of the duplicate and maintains the order of the original list. 
It is defined inside `utils.py` but the benchmarks of the function can be obtained
by running `main.py`. To run the script, execute the following command on your terminal

```
pipenv run python ./main.py
```

This will output the execution time of the function in milliseconds for the defined cycles

```
deduplicate_list function took 19.502 ms to execute
```

### Results
Here's the benchmark of the function when executed on my two machines. Both
having the same list size of 100,000 and duplicate percentage of 50%

On Macbook
```
Macbook Pro 2019
2.8 GHz Quad-Core Intel Core i7
16 GB 2133 MHz LPDDR3

5 test iteration
deduplicate_list function took 19.502 ms to execute
deduplicate_list function took 18.530 ms to execute
deduplicate_list function took 18.323 ms to execute
deduplicate_list function took 19.037 ms to execute
deduplicate_list function took 17.819 ms to execute
```

On Thinkpad
```
Lenovo Thinkpad X270
Corei5-7200U @ 2.5GGHz
8gb Memory

5 test iteration
deduplicate_list function took 23.062 ms to execute
deduplicate_list function took 22.717 ms to execute
deduplicate_list function took 22.130 ms to execute
deduplicate_list function took 21.941 ms to execute
deduplicate_list function took 21.772 ms to execute
deduplicate_list function took 21.823 ms to execute
```

# Security-Device
## Device
This program will take a string as user input, then will print the action taken (lock or unlock).
To run the program, type the following command in the terminal:
``` $ make run ```
For unit testing, type the following command in the terminal:
``` $ make test ```
## Test for device
To run the test, type the following command in the terminal:
``` $ make stats ```
The test will allow the input of a number between 1-100. Which will be how many iterations will be run for the data sampling. 50 iterations may take more than a minute to run.
The test will return the minimum, maximum, and average symbols generated to unlock the device.
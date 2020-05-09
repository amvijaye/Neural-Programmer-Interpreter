# Neural-Programmer-Interpreter
Neural-Programmer-Interpreter implementation based on the original paper by Scott Reed and Nando De Freitas

## Overview of Neural-Programmer-Interpreter
The architecure of NPI consists of:

* **Program Termination Network**: A feed forward network generates the probability of terminating execution using LSTM Controller hidden state ht.
* **Subroutine Lookup Network**: A feed forward network generates a key that points to the next subroutine invoked. This too uses the LSTM Controller hidden state ht to generate the required output.
* **Argument Network**: A feed forward network generated the required arguments for the next invoked subroutine. This uses the LSTM Controller hidden state ht to generate the required output as well. 
* **State Encoder**:A generator network that produces encoded inputs by merging the previous subroutine arguments and environment.
* **Core**:Dual-layer LSTM which has been trained to check which subroutine is called next.
* **Program End-Predictor**:This network shows the hidden state of the LSTM and tells us the timestemp of the terminating execution.
* **Next Predictor**:This network tells us exactly which program in the encoded input will be executed.

## Tasks
### Card Pattern Matching
* main.py ==> executable task which will generate traces
* trace_card_matching.py ==>  it shows the traces for the given set of data

## Execution Results
Example 1:card1=5 of diamonds and card2=5 of diamonds
![example1](https://user-images.githubusercontent.com/65048509/81460030-b8bd4d80-9170-11ea-8cf4-c7c93eadc4a5.JPG)


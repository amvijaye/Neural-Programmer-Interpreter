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

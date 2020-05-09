# Neural-Programmer-Interpreter
Neural-Programmer-Interpreter implementation based on the original paper by Scott Reed and Nando De Freitas

# Overview of Neural-Programmer-Interpreter
The architecure of NPI consists of:

a.	Program Termination Network: A feed forward network generates the probability of terminating execution using LSTM Controller hidden state ht.
b.	Subroutine Lookup Network: A feed forward network generates a key that points to the next subroutine invoked. This too uses the LSTM Controller hidden state ht to generate the required output.
c.	Argument Network: A feed forward network generated the required arguments for the next invoked subroutine. This uses the LSTM Controller hidden state ht to generate the required output as well. 


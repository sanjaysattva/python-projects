# circuit solver

the code replicates what the LT spice can do , ie , slove circuits

The input is a netlist file , given in the commandline arguments . The netlist file has data in a specific format.

The data starts with ".circuit" and ends with ".end". 

".ac" gives the AC voltage source frequency.

After the .circuit line , the following lines have the data of circuital components

eg netlist file:

.circuit

V1 GND 1 ac 1 0

R1 1 2 4.5e3

L1 2 3 80.96e-6

C1 3 GND 2.485e-12

L1 3 4 80.96e-6

R2 4 GND 4e3

.end

.ac V1 1e6 

R1 denotes resisitor , 1 and 2 are nodes ,the last element is the value.

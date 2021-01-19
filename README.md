Netlist Simulator
========


Simulator
----------

###I - Installation 


Please note that you can find all the code relative to this project on my github repo : https://github.com/JulienMalka/sysnum

As suggested in the project description, here is a website dedicated to my project : http://julienmalka.me/sysnum-simulateur.html

Before running the simulator, please perform this command :
```pip install -r requirements.txt```

###II - Usage 


To run the simulator run the command :
```python simulator.py --netlist netlist.net --inputs inputs.txt --steps n```
where netlist.net is the file containing the netlist, inputs.txt (optionnal) is the file containing the values of the inputs at each step (one line per input and per step), and n is the number of steps you want to simulate.

###III - Tests


You'll find tests located under the "tests" folder. 


Processor
--------

### Run the processor

To create the processor go in the processeur folder and run make.

Then cd in the simulator folder and run

```python simulator.py --netlist processeur.net --inputs inputs.txt --steps n --ROM ROM.hex```

You have to specify a ROM initialisation file and an input file.
Some examples can be found in processeur/examples.

Scheduling of a 40k line file is pretty long so after the first run you can add the option --scheduled program.save to avoid this time.

The output of the simulator is the content of the register t0.

### The clock

The clock ROM initialisation file can be found in processor/ROM_clock.hex
please run the simulator with --clock to have a nice formating.

The assembly file for the clock can be found in the example folder too.






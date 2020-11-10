Netlist Simulator
========

I - Installation 
---

Please note that you can find all the code relative to this project on my github repo : https://github.com/JulienMalka/sysnum

Before running the simulator, please perform this command :
```pip install -r requirements.txt```

II - Usage 
--

To run the simulator run the command :
```python simulator.py --netlist netlist.net --inputs inputs.txt --steps n```
where netlist.net is the file containing the netlist, inputs.txt (optionnal) is the file containing the values of the inputs at each step (one line per input and per step), and n is the number of steps you want to simulate.

III - Tests
---

You'll find tests located under the "tests" folder. 



# project-one-t2
project-one-t2 created by Amma Agyei and Tina Guo
## Pendulum Project
The purpose of this project was to create a code to simulate data for the acceleration, velocity and position of a pendulum and then graph the data, create a code to collect
real world data using a microbit and then graph the theta vs time, acceleration vs time and find the period. The real world data was then compared to the simulation data.
## Instructions
Make sure Spyder is downloaded on computer in order to use matlibplot. Run `SimulationCode.py` on Spyder to obtain simulation data with graphs. To log data, connect
microbit to computer and flash `DataLoggingCode.py` onto microbit on Mu Connect microbit to pendulum and collect data. After collecting data,
make sure to connect microbit to computer without flashind data. Copy file from microbit onto computer. A sample file `Experiment1.txt` was included 
in the Github folder to test the code. To parse data and graph theta vs time, acceleration vs time, find peaks and period, run `ParsingData_Graphing_And_CalculatingPeriod.py` on Spyder. In this code, is also including median filtering for noisy data.
The period could be determined by analyzing the peaks of the acceleration vs time graphs. From one peak to a consecutive peak, that was one "sample" of a period. The final period was calculated by taking the mean of the samples. To analyze the relationship between the pendulum length and the period for the real world data and the simulation data, a list of the periods for each experiment and a list of the length of pendulum for each experiment was created. Run `AnalyzingRelationships.py` to plot a logarithmic graph showing the relationship between length of pendulum and period.


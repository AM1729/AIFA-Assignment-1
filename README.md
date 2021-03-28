# AIFA-Assignment-1

# Electric Vehicle Problem
### There is a pdf along with the source code where we have shown how we approached the problem and what assumptions are made.

This is a ipynb file.
When you run the file in jupyter notebook you will be asked to enter some data as follows:
You will be asked to enter the number of EVs.
For each EV the following information should be provided -
(a) Sr - source node
(b) Dr - destination node
(c) Br - battery charge status initially
(d) cr - charging rate for battery at a charging station (energy per unit time)
(e) dr - discharging rate of battery while traveling (distance travel per unit charge)
(f) Mr - maximum battery capacity
(g) sr - average traveling speed (distance per unit time).
in the same order as specified above.

There are two helper functions-
a). all_pairs_shortest_path
        parameter: adjacency matrix of 'n' cities.
        Returns the array for all pairs shortest path
 
b). min_time
        parameter:  tuple of EVs data entered.
                    adjacency matrix of 'n' cities.
                    visited cities
                    Distance Matrix
        Returns the Minimum time to reach the destination
        Also returns the path to be followed by the EV

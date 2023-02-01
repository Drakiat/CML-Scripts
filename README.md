# CML-Scripts
A collection of CML automation scripts for making CML easier to submit for classes.

## Setup:

(was built for Python 3.x)

`pip install paramiko`

``CML_nodes.py``

### Usage:
This script takes in a CML (virl2) IP address, the login information and the lab ID (found in the address of the lab you're running this for). Then it will run `sh run` on each node (make sure that the only nodes that are on are compatible with this command; don't use the computer nodes with this). This will output into a text file for each node.

Make sure to also have each terminal open on the `R1>` mode. (Press enter in each router before running.)


#!/usr/bin/python3 

# NASA CEA Automated Calculation Script
# Accepts input data in the input.txt file in the input directory
# with the format shown in the template 
#
# Input data includes Max/Min chamber pressures, pressure increment,
# Max/Min OF Ratio, and OF ratio step. 
#
# Program is organized into three sections: 
# 
# 1. Parse Input Data and organize into data groupings that CEA can handle
#
# 2. Automate entering the data into the CEA forms
#
# 3. Parse the Data in the output file
#
# Library Files: 
#
# -- calculate: Enters data into CEA
# -- inputParse: Parse the input Data
# -- outputParse: Parse the output Data
#
# Import Modules 
from selenium import webdriver
import os, sys

# File Location of Custom Python Libraries
libDir = "./lib"

# Include Library Files 
sys.path.append(libDir)
import inputParse, autoCEA

# Input/Output File Locations
inputFilename = os.path.join("input","input.txt")
outputFilename = os.path.join("output","output.txt")

# Load Input Data from file 
inputs = inputParse.inputData(inputFilename)
inputs.loadinputData()
inputs.parseInputs()

# Assign CEA Inputs to variables
pressLims = inputs.pressLims
ofLims = inputs.ofLims
OX = inputs.oxnumb
fuel = inputs.fuelnumb
pressStep = inputs.pressStep
ofStep = inputs.of_step

# Run the CEA Simulation
for pressLim in pressLims:
   for ofLim in ofLims:
      autoCEA.runCEA(outputFilename, pressLim, ofLim, fuel, OX, pressStep, ofStep)

# Close the browser
autoCEA.quitBrowser()

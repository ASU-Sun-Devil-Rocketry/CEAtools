#!/usr/bin/python3 

# inputParse: Read Files from the input folder and organize into data chunks 
# that NASA CEA can handle 

# Modules 
import os, math

# Fuel Dictionary 
fuelDic = {
    "CH4": 0,
    "CH4_L": 1,
    "H2": 2,
    "H2_L": 3,
    "RP1": 4
}

# Oxidizer Dictionary
oxDic = {
   "AIR": 0,
   "CL2": 1,
   "CL2_L": 2,
   "F2": 3,
   "F2_L": 4,
   "H2O2_L": 5,
   "N2H4_L": 6,
   "N2O": 7,
   "NH4NO3": 8,
   "O2": 9, 
   "LOX": 10
}

# class for structuring input data
class inputData:
   def __init__(self, filename):
      self.inputFilename = filename

   # Method for Reading Data from the input file
   def loadinputData(self):
      # read values from input text file 
      self.inputfile = open(self.inputFilename)
      self.inputdata = self.inputfile.read().split()
      self.inputfile.close()
       
      # pressure range (24 values max)
      self.presslow = float(self.inputdata[0])
      self.presshigh = float(self.inputdata[1])
      self.presspoints = float(self.inputdata[2])
       
      # OF ratio range (30 points max) 
      self.of_low = float(self.inputdata[3]) 
      self.of_high = float(self.inputdata[4]) 
      self.of_points = float(self.inputdata[5])
      self.of_step = (self.of_high - self.of_low)/self.of_points
       
      # propellant choice
      self.fuel = self.inputdata[6]
      self.ox = self.inputdata[7]

      # Convert Propellant choice to an integer
      self.fuelnumb = fuelDic[self.fuel]
      self.oxnumb = oxDic[self.ox] 

   # Method for Organizing the data into a list of inputs
   # Each element in the output list is a range of values to be entered into 
   # the NASA CEA form
   def parseInputs(self):

      # Determine number of Pressure and OF blocks
      # CEA can only run 24 datapoints at once
      # and 30 OF ratios
      self.numbPressBlocks = int(self.presspoints/24)
      self.pressExtra = self.presspoints%24 
      self.numbOFBlocks = int(self.of_points/30)
      self.OFextra = self.of_points%30

      # Determine Step size for subsequent calculations
      self.pressStep = (self.presshigh - self.presslow)/self.presspoints
      self.of_step = (self.of_high - self.of_low)/self.of_points

      # Determine Input values for CEA
      # Note that if there is only one data point the low and high pressure will be the same
      # Pressures
      self.pressLims = []
      pressHigh = self.presslow - self.pressStep
      for i in range(self.numbPressBlocks):
         pressLow = self.presslow + 24*self.pressStep*i
         pressHigh = pressLow + 23*self.pressStep
         self.pressLims.append([pressLow, pressHigh]) 

      self.pressLims.append([(pressHigh+self.pressStep) , self.presshigh])

      # OF Ratios
      self.ofLims = []
      ofHigh = self.of_low - self.of_step
      for i in range(self.numbOFBlocks):
         ofLow = self.of_low + 30*self.of_step*i
         ofHigh = ofLow + 29*self.of_step
         self.ofLims.append([ofLow, ofHigh])
          
      self.ofLims.append([(ofHigh+self.of_step) , self.of_high])   

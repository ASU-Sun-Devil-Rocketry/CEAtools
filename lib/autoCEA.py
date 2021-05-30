#!/usr/bin/python3

# Calculate.py: Custom Python module to use Selenium to automate the 
# process of filling out the NASA CEA Form

# Modules to import 
from selenium import webdriver
import os

# Declare Webrowser
browser = webdriver.Chrome()

# Function for clicking the submit button
def submit():
   # Click Submit button to start Rocket Propulsion Analysis
   try:
      submitButton = browser.find_element_by_name(".submit")
   except:
      submitButton = browser.find_element_by_name("Submit")
   submitButton.click()

def runCEA(outputFile, press, OF, fuel, ox, pressStep, ofStep):

   # URL of page to be downloaded
   url = "https://cearun.grc.nasa.gov/"

   # Open Chrome to NASA CEA
   browser.get(url)

   # Choice Rocket Propulsion Analysis
   submit()

   # Enter the pressure range in CEA
   P_Low = browser.find_element_by_name("P_low")
   P_Low.send_keys(str(press[0]))
   P_High = browser.find_element_by_name("P_hi")
   P_High.send_keys(str(press[1]))
   P_Step = browser.find_element_by_name("P_int")
   P_Step.send_keys(str(pressStep))

   # Enter the pressure Units (psia)
   P_units = browser.find_elements_by_name("P_unit")
   P_units[3].click()
   
   # Submit Range of Pressures
   submit()
   
   # Choose RP-1 Fuel
   fuelEntry = browser.find_elements_by_name("fuchoice")
   fuelEntry[fuel].click()
   submit()
   
   # Choose LOX
   oxEntry = browser.find_elements_by_name("oxchoice")
   oxEntry[ox].click()
   submit()
   
   
   # Set OF Ratio Range 
   OFR_Low = browser.find_element_by_name("OFP_low")
   OFR_Low.send_keys(str(OF[0]))
   OFR_High = browser.find_element_by_name("OFP_hi")
   OFR_High.send_keys(str(OF[1]))
   OFR_Step = browser.find_element_by_name("OFP_int")
   OFR_Step.send_keys(str(ofStep))
   submit()
   
   # Skip Exit Conditions
   submit()
   
   # Perform CEA Analysis
   submit()
   
   # Copy All Text From output to a text file 
   output = browser.find_element_by_class_name("outputContent")
   outputFile = open(outputFile, "a")
   outputFile.write(output.text)
   outputFile.close() 

def quitBrowser():
   browser.quit()

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

   # Choose Rocket Propulsion Analysis
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
   
   # Choose Fuel
   fuelEntry = browser.find_elements_by_name("fuchoice")
   fuelEntry[fuel].click()
   submit()
   
   # Choose Oxidizer
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
   
   # Select Tabulate Results Option
   tabulateOption = browser.find_elements_by_name("doThis")
   tabulateOption[1].click()
   submit()

   # Setup Table Entries
   parameter1 = browser.find_element_by_name("plt1")
   parameter1.send_keys("t")
   parameter2 = browser.find_element_by_name("plt2")
   parameter2.send_keys("gam")
   parameter3 = browser.find_element_by_name("plt3")
   parameter3.send_keys("cp")
   parameter4 = browser.find_element_by_name("plt4")
   parameter4.send_keys("p")
  
   # Perform CEA Analysis
   submit()
   
   # Copy All Text From output to a text file 
   output = browser.find_element_by_link_text("Tabulation")
   output.click()
   outputdata = browser.find_element_by_tag_name("pre")

   # Get rid of column labels
   outputlines = outputdata.text.splitlines()[1:]
   outputFile = open(outputFile, "a")
   for line in outputlines:
      outputFile.write(line)
      outputFile.write("\n")
   outputFile.close() 

def quitBrowser():
   browser.quit()

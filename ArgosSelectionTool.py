#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------

# Copy and paste a line of data as the lineString variable value
lineString = '10186609166,true,2019-05-16 22:20:59.000,-76.51420999999999,31.75682,,0.0,-129.0,4.0167961104E8,853.0,226,"46",31.75682,31.75682,"1",-76.51420999999999,-76.51420999999999,11,0,3,167.0,546.0,989.0,734.0,5,5,0,1,"1",,,"argos-doppler-shift","Pterodroma hasitata","174441","HA09","Satellite tracking of black-capped petrels, 2019"'
    
# Use the split command to parse the items in lineString into a list object
line_data = lineString.split(",")
  
# Assign variables to specfic items in the list
event_id = line_data[0]   # Argos tracking event ID ("event-id")
timestamp = line_data[2]  # Observation date ("timestamp")
lat = float(line_data[3])        # Observation latitude  ("location-lat")
lon = float(line_data[4])        # Observation longitude ("location-lon")
lc  = line_data[31]        # Observation location class ("argos:lc")
tag_id = line_data[-3]     # Tag identifier ("tag-local-identifier")
  
# Print information to the use
#print (f"Record {event_id} indicates {tag_id} was seen at {lat}N and {lon}W on {timestamp}")

# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}

#Evaluate latitude and longitude conditions
lat_condition = the_box['y_min'] < lat < the_box['y_max']
lon_condition = the_box['x_min'] < lon < the_box['x_max']

#Report the status of the points
if lat_condition & lon_condition:
    print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
else:
    print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')

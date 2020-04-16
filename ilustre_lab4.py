#Kirsten Ilustre
#April 20, 2020
#GEOG 682 Lab 4
import processing
crime = "S:/682/Spring20/kilustre/Lab4/Crime_Incidents_in_2017/Crime_Incidents_in_2017.shp"
iface.addVectorLayer(crime,"crime","ogr")
districts = "S:/682/Spring20/kilustre/Lab4/Police_Districts/Police_Districts.shp"
iface.addVectorLayer(districts,"districts","ogr")
processing.run("qgis:joinbylocationsummary",{'INPUT':districts,'JOIN':crime,'PREDICATE':1,'SUMMARIES':0,'OUTPUT':"S:/682/Spring20/kilustre/Lab4/join.shp"})
join = "S:/682/Spring20/kilustre/Lab4/join.shp"
iface.addVectorLayer(join,"join","ogr")
#Police district 3 had the most crimes in 2017
#A total of 5970 crimes occurred in the district
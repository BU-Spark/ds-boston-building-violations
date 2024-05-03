Carlos Contreras - Class of 2025 - team lead 
Xudong Wang - Class of 2025
Jeffrey Zhao - Class of 2024 
Julian Shyu - Class of 2025

Build_prop.ipynb: 
This note is focused on how to analyze the Building and Property Violations, which is the work we have done in the early insight part.
-Are there certain landlords/ management companies that have repeated violations?
-Are there common features of certain buildings (same build year, etc)?
-What neighborhoods/ communities are affected most?
-What kinds of building complaints are people making around the city?

Code_enforcement.ipynb:
This is also for the early insight part, to analyze the Public Works Violations, also try to figure out the question as the same as the Build_prop.

Merged_data.ipynb:
We merge the Live_management.csv to the Building and Property Violations, also merge it to the Public Works Violations. Analyzing the property assessment and also the works we have done.

Violation Features & Owners.ipynb:
This uses the merged_data to filter by features or owners and create tables for them. The file is set up in such a way that you only need to import in the dataset and the whole program should work. It will build each table for each respective feature and should get the graphs. Note: The datasets for these are so large that they exceed the github allowed amount so they aren’t in the data folder, apologies. The same is true for the 311 datasets. Assuming that you have the Code [Enforcement Violations](https://data.boston.gov/dataset/public-works-violations), [Building and Property Violations](https://data.boston.gov/dataset/building-and-property-violations1), the [2024 Property Assessment](https://data.boston.gov/dataset/property-assessment), and the [SAM dataset](https://data.boston.gov/dataset/live-street-address-management-sam-addresses/resource/6d6cfc99-6f26-4974-bbb3-17b5dbad49a9) all properly labeled like in the code and in the data folder, it should work.

311 Service Call Trends.ipynb:
This code imports in a series of 311 datasets (2024-2020) and creates the graph. There should not be anything that needs to be changed unless you need to specify a path to the datasets. This data needs to be imported into the data folder as well like the above datasets because of size restrictions, and can be found [here](https://data.boston.gov/dataset/311-service-requests).



Project Extension Analysis.ipyn 
The code imports the attribute table that maps Boston Neighborhoods and cleans it so that it is useful for merging with GEOID DATASETS. The code also imports two datasets for educational attainment and racial demographics. The racial demograhics dataset is included in the repo as 2020 census Boston. The Educational dataset cannot be legally redistributed but getting access to it is simple by visiting IPUMS and selecting the dataset “2022 American Community Survey: 5-Year Data [2018-2022, Block Groups & Larger Areas]” and selecting the table “1. Educational Attainment for the Population 25 Years and Over
   Universe:    Population 25 years and over
   Source code: B15003
   NHGIS code:  AQPK
“. The file then cleans these datasets, merges them with neighborhoods table and conducts a basic analysis of racial and educational attainment analysis. 

Project Extension Spatial Data for Spatial Datasets folder:

The folder contains the necessary files to map group blocks to boston neighborhoods in QGIS by doing a spatial join. The files contain a boston neighborhoods boundaries map, a Tiger join shapeline file needed to do the intersection map in QGIs. 
Running the file Block Groups Mapping will open the map with tree layers including the intersection from which the attribute table of GEOIDS can be extracted and exported as CSV.
The file GEOIDAreas is the csv file we use for merging GEOIDs and Neighborhoods. 

# ds-boston-building-violations-team-c

## Overview

Welcome to Team C's repository!  This repository contains all the necessary files and scripts used in our data analysis project.  Here, we provide detailed information on how to navigate the repository, including guides to each raw data file, descriptions of the notebooks or scripts used for data processing, and summaries of the cleaned datasets. 

Due to GitHub's file size limitations, the uploads on GitHub are not complete. The full version is available on our Google Drive.

## Repository Structure

### Raw Data

The raw data folder contains all the initial data files as received from the data source. These files have not been modified or processed. If the dataset is too large or sensitive to be hosted on GitHub, it is available through the provided Google Drive link.

- **Location**: `Raw_Data/`

- **Access via Google Drive**: [Google Drive Link](https://drive.google.com/drive/folders/1AS7prGQ4yZpof_l0HBD3dzvcveJl0HT-)


- **Data Files**:
  - `311_Service_Requests_2024.csv`: This data set includes all channels of engagement in which a service request is created.
  - `BUILDING_AND_PROPERTY_VIOLATIONS.csv` and `PUBLIC_WORKS_VIOLATIONS.csv`: Reports of property violations from different departments, including detailed information about the time, location, and cause of each violation.
  - `PROPERTY_ASSESSMENT.csv`: Compile detailed indoor and outdoor conditions for each property in Boston.
  - `demographic.csv`: Data on the total population and racial demographics of each neighborhood in Boston for the year 2020.

### Data Processing/Transformation Scripts
This folder contains all scripts and notebooks used for data processing and transformation. Each file is thoroughly documented to detail its specific functions and the transformations it applies to the raw data or cleaned data.

- **Location**: `Code/`
- **Access via Google Drive**: [Google Drive Link](https://drive.google.com/drive/folders/1kSTbgCOEQgn4KCKbdrZb12U017L6S_c-)

- **Notebooks**:
  - `complain.ipynb`: Analyze the categories of violations after clustering, and use the Folium library to create real maps and bar charts to display their numerical distribution.
  
  - `housing_relation.ipynb`: Explore the ratio of the number of properties to the number of properties with violations in each neighborhood, and generate textual ratios and visual bar chart results.
  
  - `potential_factors.ipynb`: Investigate whether the population size, bachelor's degree rate, and number of individuals with bachelor's degrees in each neighborhood are related to the number of violations, using mathematical methods such as regression analysis.
  
  - `potential_factors_yearly_build.ipynb` and `potential_factors_yearly_pub.ipynb`: Two notebooks explore the relationship between reported violations in the BUILDING_AND_PROPERTY_VIOLATIONS and PUBLIC_WORKS_VIOLATIONS datasets and time (year and quarter).
  
  - `property.ipynb`: Analyze Boston properties from four perspectives: property type, property view, indoor and outdoor conditions, year built, and year renovated. Output interactive maps to display geographic distribution and histograms to show quantity distribution.
  
  - `trend_pub.ipynb`: Plot the annual quarterly trends for each neighborhood in the PUBLIC_WORKS_VIOLATIONS dataset to identify any seasonal trends or characteristics.
  
  - `ttop.ipynb`: Plot annual histograms for the top ten types of violations by number in both the BUILDING_AND_PROPERTY_VIOLATIONS and PUBLIC_WORKS_VIOLATIONS datasets.

  - `economic.ipynb`: Analyzed the relationship between some economic factors and violation frequency.
  
- **Scripts**:
  - `assessment_stat.py`: Utilize the Folium library to display clusters of each property type in every block on an interactive map.
  - `data_helper.py`: Used for data cleaning operations such as removing empty rows.
  - `heatmap_type.py`: Generate a heatmap depicting the relationship between streets and violation types, allowing identification of which types of violations occur most frequently or which streets have a higher number of violations.
  - `language.py`: Encode the descriptions of violations using a variant of BERT, then classify the results using K-means clustering. Finally, use the most relevant statement to the cluster as its category name.
  - `multiple_violations.py`: Plot a histogram showing the number of violations that occurred on each street.
  - `radar_api.py` and `temp_zip.py`: Utilize the Radar API and GoogleMap API to convert specific textual addresses into latitude and longitude coordinates.
  - `real_map.py`: Test whether the boundary GeoJSON file functions correctly and produce a visual map for validation.
  - `real_map_heatmap.py`: Visualize a heatmap of PUBLIC_WORKS_VIOLATIONS based on the latitude and longitude coordinates of the violations.
  - `temp_map_mark.py`: Preprocessing to convert specific addresses into latitude and longitude coordinates involves combining different columns to form complete addresses.
  - `top_10.py`: Get the top 20 streets with the most violations in the BUILDING_AND_PROPERTY_VIOLATIONS and PUBLIC_WORKS_VIOLATIONS datasets.    

### Cleaned Data

This section includes Completed Files and In-progress Files. The former consists of complete versions of datasets, while the latter comprises datasets generated during the processing phase, which may be less comprehensive. Both are included as they have been utilized in the analysis process. 

- **Location**: `Cleaned_Data/`

- **Access via Google Drive**: [Google Drive Link](https://drive.google.com/drive/folders/11GZBnKaRP8WO4LKtOYUtz5ig4Z4jvt0S)

- **Completed Files**:
  - `Boston_Neighborhood_Education_Rate_2020.csv`: The bachelor's degree attainment rate in each neighborhood for the year 2020.
  - `cleaned_311_Service_Requests_2024.csv`: The 311_Service_Requests_2024.csv file after undergoing data cleaning.
  - `cleaned_PROPERTY_ASSESSMENT.csv`: The PROPERTY_ASSESSMENT.csv file after undergoing data cleaning.
  - `cleaned2_BUILDING_AND_PROPERTY_VIOLATIONS.csv`: The BUILDING_AND_PROPERTY_VIOLATIONS.csv file after undergoing data cleaning.
  - `cleaned2_PUBLIC_WORKS_VIOLATIONS.csv`: The PUBLIC_WORKS_VIOLATIONS.csv file after undergoing data cleaning.
  - `clustered_results_with_categories.csv`: Utilize NLP techniques to cluster violation types, obtaining categories, and then add them to the dataset.
  - `Neighborhood_Violation_Ratios_BUILDING.csv` and `Neighborhood_Violation_Ratios_PUBLIC`: The ratio of properties with violations to the total number of properties in both the BUILDING_AND_PROPERTY_VIOLATIONS and PUBLIC_WORKS_VIOLATIONS datasets.
  - `PROPERTY_ASSESSMENT_WITH_NEIGHBORHOODS.csv`: Added the following columns to the original PROPERTY_ASSESSMENT dataset: specific address column, latitude and longitude coordinates, neighborhood where the address is located, and indoor/outdoor condition rating.
  - `updated_BUILDING_AND_PROPERTY_VIOLATIONS.csv` and `updated_PUBLIC_WORKS_VIOLATIONS.csv`: Retrieve the neighborhood where each property with a violation occurred based on its latitude and longitude information.
  - `Updated_Violations_with_Population.csv`: The number of occurrences and total occurrences of violations in each neighborhood in both the BUILDING_AND_PROPERTY_VIOLATIONS and PUBLIC_WORKS_VIOLATIONS datasets, along with the population count of each neighborhood.
  - `Zip_zori_uc_sfrcondomfr_sm_month`: The data of rental price from zillow, the rent is represented by an index.
  - `incode_by_zip`: The data of household income collected from incomebyzipcode.com, the data represents the median household income of zip code areas in Boston.

- **In-progress Files**:
  
  The following files are also located in this folder, but they are all works in progress of the datasets mentioned above. Their contents are duplicated but not as enriched. 
  
  - `clustered_results_with_representatives.csv`
  - `PROPERTY_ASSESSMENT_addr.csv`
  - `PROPERTY_ASSESSMENT_COORDINATES_FULLY_MERGED.csv`
  - `PROPERTY_ASSESSMENT_WITH_COORDINATES.csv`
  - `PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED.csv`
  - `PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED_2.csv`
  - `PROPERTY_ASSESSMENT_WITH_SCORES.csv`
  - `Total_Violations_by_Neighborhood_2020.csv`

### Data Visualizations

This folder contains all our generated interactive maps and two separately generated visualization results. Other visualization images are all kept within notebooks, and we have preserved all execution results. If the dataset is too large or sensitive to be hosted on GitHub, it is available through the provided Google Drive link.

- **Location**: `Data_Visualizations/`

- **Access via Google Drive**: [Google Drive Link](https://drive.google.com/drive/folders/1Q12TwbLUARHoHpaT0S2cNip6ESJQOYv0)

- `boston_issues_circle_markers.html`: This map illustrates the distribution of the 7 types of violations we have identified in Boston. We have marked the location of each property with a violation using red circles.

- `boston_issues_heatmaps.html`: This map displays the heat distribution of the 7 types of violations we have identified in Boston, making it easier to observe areas with a higher density of distribution.

- `boston_prop_view_map.html`: This map illustrates the distribution of property view clusters based on different tiers.

- `boston_properties_map_LU.html`: This map displays the distribution of property clusters by type in each neighborhood.

- `boston_violations_map_boundary.html`: This map displays the distribution of properties appearing in the PUBLIC_WORKS_VIOLATIONS dataset, marked with red circles.

- `boston_violations_map2.html` and `boston_violations_map111.html`: These two maps respectively depict the distribution of violations in the PUBLIC_WORKS_VIOLATIONS and BUILDING_AND_PROPERTY_VIOLATIONS datasets. Since these are early-stage exploration maps, neighborhood boundaries are not yet displayed. However, they serve as a milestone in our analytical journey, hence they are retained.

- `boston_year_heatmap.html` and `boston_year_remodel_heatmap.html`: Each interval represents 25 years, displaying the density of property construction and remodels over time, measured in yearly increments.

- `heatmap.png`: Heatmap depicting the relationship between streets and violation types.

- `streets_with_multiple_violations.png`: The histogram in this image displays the number of violations that occurred on each street, ordered from most to least occurrences.

### Slides

This folder contains our PowerPoint slides for the three project presentations.

- **Location**: `Slides/`

- **Access via Google Drive**: [Google Drive Link](https://drive.google.com/drive/folders/1CPhN-p9Z2W_OnBwqXqAFhsrxjTErfja-)


  - `506 Building Violations Team C Early Insights Slides.pptx`
  - `506 Building Violations Team C Mid-semester Slides.pptx`
  - `506 Building Violations Team C Final Presentation Slides.pptx`
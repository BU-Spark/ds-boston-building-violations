# Boston Building Violations Project

## What the project is

This project explores building violations in Boston, analyzing patterns related to landlords, building characteristics, neighborhood demographics, and types of complaints. The team of John, Paul, Farzaan, Chloe, and Michael aim to identify critical areas with high violation rates, assess the impact on different communities, and propose solutions to improve housing standards. By integrating data analysis with legislative and community-focused approaches, the project seeks to enhance living conditions and enforce higher compliance among property owners across Boston.

## What the team did

We created a geographical map to visualize clusters of communities and neighborhoods in Boston with the highest number of building violations, which helped in identifying areas that need the most attention. We also researched the demographics (race, age, socioeconomic class) of these neighborhoods to determine if certain communities are being disproportionately affected by building violations or external factors.

Key Questions Addressed:
- We examined if certain landlords or management companies are responsible for repeated violations.
- We looked at common features of buildings that might contribute to violations, such as age and build year.
- We analyzed which neighborhoods and communities are most affected by violations.
- We investigated the types of building complaints made throughout the city.

We combined the 2020 neighborhood census data with our building violations dataset after cleaning it to include all relevant neighborhoods.

We gathered income data for each neighborhood to see if there is a correlation between income levels and frequency of violations, using median income for this purpose and finding average median income figures for each neighborhood.

Based on our findings, we proposed solutions to improve Boston’s housing quality and reduce violations. Some solutions we proposed included setting higher standards and increasing penalties for landlords with repeated violations, creating incentives for residents to report violations, and increasing accountability by having city employees more closely monitor properties.

## Repository Navigation

In the `ds-boston-building-violations`, navigate to `sp24-team-b` which is where the results for our team are located. In the `data` folder you will find two separate folders called `code` and `notebooks`. In the `code` folder, you can find the python scripts used to parse the various datasets we used throughout the project. In the `notebooks` folder you can explore and add on to the various techniques implemented in this project.

## Datasets used and where to find them

- **Public works violations:** Utilized the datasets from 2019 to 2024. (https://data.boston.gov/dataset/public-works-violations)
- **Building and property violations:** Utilized the datasets from 2019 to 2024. (https://data.boston.gov/dataset/building-and-property-violations1)
- **Boston 311 requests:** Utilized the datasets from 2019 to 2024. (https://data.boston.gov/dataset/311-service-requests)
- **Property Assessment:** Utilized the datasets from 2019 to 2024. (https://data.boston.gov/dataset/property-assessment)
- **2020 Census for Boston:** Utilized the 2020 Census Boston neighborhood data. (https://data.boston.gov/dataset/2020-census-for-boston)
- **Income Data:** Utilized this website in our research of Boston neighborhood income data. (https://www.point2homes.com/US/Neighborhood/MA/Boston-Demographics.html)

## Getting Started

After cloning into our repository, run `pip install -r requirements.txt`, this contains all of the python packages that we used in our python notebooks, and scripts.

Once you have downloaded all the datasets, in our `code` folder there is a file named `CSVCombiner.py'. To combine the files you will need to change the names of the csv files you want to combine. For example, if you want to combine your 311 request datasets, you need to rename the start of the filename as ‘311_’. 

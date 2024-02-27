#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:49:44 2024

@author: chloe
"""

import pandas as pd


# Load the data
file_path = '/Users/chloe/Desktop/311_SERVICE REQUESTS-2013.csv'
data = pd.read_csv(file_path)

# Normalize the city names to ensure consistent counting
data['timing'] = data['on_time'].str.lower().str.strip()

# Count the number of violations by normalized city
normalized_violation_counts = data['timing'].value_counts()

# Display the count of violations by normalized city
print(normalized_violation_counts)


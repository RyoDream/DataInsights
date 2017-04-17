# NYC Crime DataInsights
`NYC Crime DataInsights` is a project developed for the `DS1004 Big Data Analytics` at NYU, aming at process and analysis [NYC Crime Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i) of the latest 10 years (2006 - 2015).

## Project Structure

### Overview
DataInsights is a Python and Shell combined project, utilizing several components to meet the needs. 

* **Linux Shell**: provide cmdline user interface for interaction.
* **Spark**: process the massive dataset and generate output.
* **Matplotlib**: plot the output from Spark and generate graphs and charts.

The structure of DataInsights is:   
.   
├── README.md   
├── output   
├── plot   
└── scripts   

### Scripts
This directory contains all python (for Spark) and shell scripts.   
Scripts with different logical functions were divided into several sub-directories.   

.   
├── **cleaning**: Aim to examine the dataset and to find invalid records.    
├── **cmdline**: Contains all shell scripts that could automatically invoke the Spark job and fetch result from HDFS.     
├── **datatype**: Aim to recognize the data type and semantic of every cell in the dataset (based on domain konwledge of the dataset).   
├── **datetime**: Statistics based on datetime information.   
├── **locations**: Statistics based on geo-location information.   
└── **statistics**: Statistics based on mathmatical knowledge.  

### Output
Contains all output files for further process.

### Plot
Contains all ploting scripts to draw charts and graphs.

## Usage

### Data Exploring
```
$ cd DataInsights/scripts/cmdlines
$ bash run_datatype.sh
$ bash statistics_datatype.sh
```

### Data Cleaning
```
$ cd DataInsights/scripts/cmdlines
$ bash run_datacleaning.sh
```

### Data Analysis
```
$ cd DataInsights/scripts/cmdlines
$ bash run_scripts.sh
```

### Data Visualization
```
$ cd DataInsights/plot/
$ bash draw_all_plots.sh
```

## Current Outcome
All result and outcome will be published after the end of this course.
# What are the primary indicators of patient readmission?

Hospital readmission has become such an issue in recent years that Centers for Medicare and Medicaid Services (CMS) has begun to impose fines on hospitals excessive readmissions. Despite this, the percentage of hospitals fined for readmissions has increased every year. CMS reports 78% of hospitals received such fines in fiscal year 2015. [***source***] Our goal is to determine if there is a pattern among patients who are readmitted so that we can detect early on if a patient has a high readmission risk and take steps to combat it.

# The Dataset

Our data consist of 10,000 patient records with 50 features. The features can be sub-divided into the following categories: 

1. Patient Demographics
2. Patient Health
3. Visit details
4. Patient Survey results

## Patient Demographics

These features give us basic demographical imformation about the patient. They are as follows:

- **City**: City of residence as listed on the billing statement
- **State**: Patient state of residence as listed on the billing statement
- **County**: Patient county of residence as listed on the billing statement
- **Zip**: Patient zip code of residence as listed on the billing statement
- **Lat, Lng**: GPS coordinates of patient residence as listed on the billing statement
- **Population**: Population within a mile radius of patient, based on census data
- **Area**: Area type (rural, urban, suburban), based on unofficial census data
- **TimeZone**: Time zone of patient residence based on patient’s sign-up information 
- **Job**: Job of the patient (or primary insurance holder) as reported in the admissions
information
- **Children**: Number of children in the patient’s household as reported in the admissions information
- **Age**: Age of the patient as reported in admissions information
- **Education**: Highest earned degree of patient as reported in admissions information 
- **Employment**: Employment status of patient as reported in admissions information 
- **Income**: Annual income of the patient (or primary insurance holder) as reported at
time of admission
- **Marital**: Marital status of the patient (or primary insurance holder) as reported on
admission information
- **Gender**: Customer self-identification as male, female, or nonbinary

## Patient Health


- **VitD_levels**: The patient’s vitamin D levels as measured in ng/mL
- **Full_meals_eaten**: Number of full meals the patient ate while hospitalized (partial
meals count as 0, and some patients had more than three meals in a day if requested)
- **VitD_supp**: The number of times that vitamin D supplements were administered to the
patient
- **Soft_drink**: Whether the patient habitually drinks three or more sodas in a day (yes, no)
- **Complication_risk**: Level of complication risk for the patient as assessed by a primary
patient assessment (high, medium, low)
- **HighBlood**: Whether the patient has high blood pressure (yes, no)
- **Stroke**: Whether the patient has had a stroke (yes, no)
- **Overweight**: Whether the patient is considered overweight based on age, gender, and
height (yes, no)
- **Arthritis**: Whether the patient has arthritis (yes, no)
- **Diabetes**: Whether the patient has diabetes (yes, no)
- **Hyperlipidemia**z: Whether the patient has hyperlipidemia (yes, no)
- **BackPain**: Whether the patient has chronic back pain (yes, no)
Anxiety: Whether the patient has an anxiety disorder (yes, no)
- **Allergic_rhinitis**: Whether the patient has allergic rhinitis (yes, no)
- **Reflux_esophagitis**: Whether the patient has reflux esophagitis (yes, no)
- **Asthma**: Whether the patient has asthma (yes, no)


## Visit Details

- **Doc_visits**: Number of times the primary physician visited the patient during the initial
hospitalization
- **ReAdmis**: Whether the patient was readmitted within a month of release or not (yes, no). 
- **Initial_admin**: The means by which the patient was admitted into the hospital initially (emergency admission, elective admission, observation)

## Patient Survey Results

Patients are given an eight queston survey in which they are asked to rate the importance of several factors/surfaces on a scale of 1 to 8 (1 = most important, 8 = least important)

- **Item1**: Timely Admission
- **Item2**: Timely treatment
- **Item3**: Timely visits
- **Item4**: Reliability
- **Item5**: Options
- **Item6**: Hours of treatment
- **Item7**: Courteous staff
- **Item8**: Evidence of active listening from doctor

# Cleaning The Data: The Process

## Finding Anomolies

In order to find outliers we will be calculating *z-values* (or *z-scores*) as described in *Data Science using Python and R* [***source***]. A *z-value* for a given feature is a scaled value aimed to simplify the data. A typical scale used is -3 to 3 for regular values, and anything greater than 3 or less than -3 is considered an outlier. It can be thought of as similar to a bell curve on a graph, but expressed in only numerics. We'll be using this approach because it is an effective way to standardize data and makes spotting outliers trivial. 

Once we have standardized z-scores we'll use graphs such as histrograms and boxplots to visualize them.

## Tools Used

R will be the language of choice for this project, purely because it is the scientific language that I am most familiar with. It's extensive *tidyverse* library, in particular the *dplyr* and *ggplot2* packages, makes many of the calculations and analysis we plan to do possible in only a few lines of code. For example, as we will see in the next section, the *dplyr* package from *tidyverse* allows us to calculate *z-values* and add them to our dataset in only one line of code! 

## Code



# Cleaning Results

## Findings

## Mitigation 

### Methods

### Code

## Summary of outcomes

## Limitations

# PCA




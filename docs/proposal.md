## 1. Title and Author

- Project Title: Predictive Modeling for Health Inspections
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author Name: Abhishek Goud Thamatam 
- [GitHub](https://github.com/abhishekgoud23)
- [LinkedIn](https://www.linkedin.com/in/t-abhishek-goud/)
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background


- Using data science and machine learning, predictive modeling for health inspections helps predict which restaurants might fail health inspections done by local health departments. It uses past inspection info, restaurant details, and more to find places that might have food safety issues.By doing so, it aims to assist health departments in allocating their inspection resources more effectively and improving public health by reducing foodborne illnesses.
- Food safety is a critical public health concern, and restaurants play a significant role in ensuring the safety of the food they serve to the public. The usual health inspections take a lot of time and might not happen often enough to stop problems. Predictive modeling for health inspections is important for a few reasons:

  *Resource Allocation:* It helps health departments decide which places to inspect more often based on how risky they are. Risky places get checked more, and safer ones get checked less. This way, resources are used well.

  *Early Intervention:* By identifying establishments with a higher likelihood of violations, health departments can step in early to help them follow the rules and keep food safe.

  *Public Health:* Doing inspections this way can lead to a reduction in foodborne illnesses and related hospitalizations, ultimately improving public health outcomes.
- Research questions
1. Can we predict the outcome of a restaurant's health inspection based on historical data and restaurant attributes?
2. What are the key factors that influence the likelihood of a restaurant failing an inspection?
3. Can we develop an early warning system that identifies restaurants at risk of failing inspections well in advance of the actual inspection date?
4. How early can we predict potential issues to allow for proactive intervention?
5. How can predictive modeling be used to allocate inspection resources more efficiently? For example, can we prioritize inspections for high-risk establishments while reducing the frequency of inspections for low-risk ones?
6. What is the trade-off between inspection frequency and public safety, and how can it be optimized?
7, How can geospatial information be incorporated into the predictive model?
8. What is the relationship between specific types of violations (e.g., critical vs. non-critical) and the overall inspection outcome?
9. Can we identify which types of violations are most strongly correlated with inspection failure?
10. Are there potential biases in the data or model predictions that need to be addressed to ensure fairness in inspection processes?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- Data sources: NYC OpenData
- Data size: 92 MB
- Data shape: # of rows - 205K and # columns - 27
- Time period: 2014 - 2023
- **What does each row represent?(a patient, a school, a crime, etc.)** - Inspection
- Data dictionary
  
| Column Name           | Description                                                   | Type             |
| ----------------------| ------------------------------------------------------------- | ----------------- |
| CAMIS                 | Unique identifier for the restaurant                          | Plain Text       |
| DBA                   | Name of the restaurant                                        | Plain Text       |
| BORO                  | Borough in which the entity (restaurant) is located.;• 1 = MANHATTAN • 2 = BRONX • 3 = BROOKLYN • 4 = QUEENS • 5 = STATEN ISLAND • Missing;                        | Plain Text       |
| BUILDING              | Building number for the restaurant location                   | Plain Text       |
| STREET                | Street name for the restaurant location                       | Plain Text       |
| ZIPCODE               | Zip code of the restaurant location                            | Plain Text       |
| PHONE                 | Phone number provided by the restaurant owner/manager         | Plain Text       |
| CUISINE DESCRIPTION   | Description of the restaurant's cuisine                        | Plain Text       |
| INSPECTION DATE       | This field represents the date of inspection; NOTE: Inspection dates of 1/1/1900 mean an establishment has not yet had an inspection                                            | Date & Time      |
| ACTION                | Actions associated with each restaurant inspection             | Plain Text       |
| VIOLATION CODE        | Violation code associated with an inspection                    | Plain Text       |
| VIOLATION DESCRIPTION | Description of the violation                                    | Plain Text       |
| CRITICAL FLAG         | Indicator of the critical violation; "• Critical • Not Critical • Not Applicable"; Critical violations are those most likely to contribute to food-borne illness                               | Plain Text       |
| SCORE                 | Total score for a particular inspection                        | Number           |
| GRADE                 | Grade associated with the inspection; • N = Not Yet Graded• A = Grade A• B = Grade B• C = Grade C• Z = Grade Pending• P= Grade Pending issued on re-opening following an initial inspection that resulted in a closure                          | Plain Text       |
| GRADE DATE            | Date when the current grade was issued                         | Date & Time      |
| RECORD DATE           | Date when the extract was produced                             | Date & Time      |
| INSPECTION TYPE       | A combination of the inspection program and the type of inspection performed; See Data Dictionary for full list of expected values   | Plain Text       |
| Latitude              | Latitude coordinate of the location                            | Number           |
| Longitude             | Longitude coordinate of the location                           | Number           |
| Community Board       | Community board information                                    | Plain Text       |
| Council District      | Council district information                                   | Plain Text       |
| Census Tract          | Census tract information                                       | Plain Text       |
| BIN                   | BIN (Building Identification Number)                           | Plain Text       |
| BBL                   | BBL (Borough, Block, and Lot) information                      | Plain Text       |
| NTA                   | NTA (Neighborhood Tabulation Area) information                  | Plain Text       |
| Location Point1       | Location Point1 information                                    | Point            |

*Potential values:*

1. BORO (Borough):

1 = MANHATTAN
2 = BRONX
3 = BROOKLYN
4 = QUEENS
5 = STATEN ISLAND

2. ACTION (Actions associated with inspections):

Violations were cited in the following area(s).
No violations were recorded at the time of this inspection.
Establishment re-opened by DOHMH
Establishment re-closed by DOHMH
Establishment Closed by DOHMH. Violations were cited in the following area(s) and those requiring immediate action were addressed.
"Missing" = Not yet inspected.

3. CRITICAL FLAG (Indicator of critical violation):

Critical
Not Critical
Not Applicable

4. GRADE (Grade associated with the inspection):

N = Not Yet Graded
A = Grade A
B = Grade B
C = Grade C
Z = Grade Pending
P = Grade Pending issued on re-opening following an initial inspection that resulted in a closure

5. INSPECTION TYPE (Combination of inspection program and type):

Various types of inspection programs and types. Specific values may vary.

- I have to do more research on selecting the target variable. few possibilities:
GRADE, VIOLATION CODE, CRITICAL FLAG, SCORE, ACTION

- Potential Features:
CUISINE DESCRIPTION, BORO, ZIPCODE, VIOLATION CODE and VIOLATION DESCRIPTION, CRITICAL FLAG, Latitude and Longitude, Previous Inspection Scores or Grades

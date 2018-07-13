# Tool_Python_Data-Preprocess
This repository is created for easily data preparation, according to categories of your project.

## Motivation?
In any machine learning project, data cleaning and preparation is the most time-consuming part in the whole project. However, bunch of workloads would be alleviated if the repetitive code could be coped with only one function or one package. Therefore, data scientists can focus on collecting more related data, as well as on building more efficient models.

## Content.
The scripts are organized by categories of tasks.

- The Recommendation System:
  - Rating_Matrix: Convert rating dataframe into UxM-Matrix.
    The input data structure should be as following:
    
            eg.
                
            |   user_id   |  item_id   |   score   |
            |      1      |     3      |    6.5    |
    
    The output matrix should be:
    
            eg.
            |  user_id/item_id  |  123  |  125  |
            |        001        |  6.5  |   8   |
            |        007        |   8   |   9   |

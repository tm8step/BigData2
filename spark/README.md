# Apache Spark MLlib — Distributed Machine Learning

## Role in the Pipeline

Apache Spark MLlib provides the distributed processing and machine learning layer for this project. The PySpark application reads project data from Hive, prepares the data for modeling, trains and evaluates a machine learning model, and generates model-performance metrics that are written into HBase.

## Hive Input

**Hive table:** `econdata_ilwi`

Explain what data Spark reads from Hive and which fields are used by the machine learning workflow.

Spark reads the feature columns 'housing', 'min_wage', 'taxes', and 'metro_level' to develop a formula for the target value 'total_cost' via linear regression. 

## Data Preparation & Transformations

Describe the important preprocessing or transformation steps performed before model training.

Out of the 8 columns in the data, I chose the 4 relevant features since they all affect the cost of living in a particular county in different ways.  They are the mean cost of housing, the minimum wage, the mean taxes paid and the metropolitan level of the county.

There were no missing values in the data.

The data was split into training and testing data.  70% of the data was used to train, and 30% of the data was used to test the algorithm.

## MLlib Algorithm

**Algorithm:** `Linear Regression`

Explain:

Linear Regression was appropriate for this data because it is numerical data where the features contribute to the cost of living in the county in complex ways.

- why this algorithm was appropriate for the selected dataset;
- what prediction or modeling task it performs;
- which features and target/label are used.

## Training & Evaluation

Summarize the training process and explain the evaluation metric or metrics used.

**Primary evaluation metric(s):** `r2: coefficient of determination
RMSE: Root Mean Square Error`

RMSE:  263.04 - This shows that the average error of the prediction is 255.09$, which, since we're examining cost of living, with most figures ranging in 5 digits, is a small margin of error and quite accurate.

R^2:  0.9937 - This shows that over 99.37% of the variation in the data is explained by the given features.  This is quite accurate. 

### Training Output

![Spark Training Output](screenshots/spark-training-output.png)

### Model Evaluation

This shows the output being written to HBase

![Spark ML Evaluation](screenshots/spark-ml-evaluation.png)

## Spark Submit / YARN Execution

Document the exact `spark-submit` command used to submit the PySpark application through YARN.

```bash
spark-submit \
  --master yarn \
  --deploy-mode client \
  --name econ_metrics \
  processing.py
```

My Spark job was successful.  In my case it produced this log:  `tracking URL: http://master:8088/proxy/application_1787506831922_0004/`

![Spark Submit Output](screenshots/spark-submit-output.png)

## Spark Log

I verified the YARN logs with this command:

```bash
yarn logs -applicationId application_1787506831922_0004
```

![Spark Submit Log](screenshots/spark-submit-logs.png)

## HBase Output

List the model-performance metrics written by Spark into HBase and explain how the application connects the machine learning stage to the final persistence layer.

**PySpark source files:** [`processing.py`](processing.py)

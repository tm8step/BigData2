"""
DSC 650 Portfolio Starter

Replace this file with the Spark processing script from your final project.

Recommended portfolio comments:
- What input does the script read?
- What transformations does it perform?
- What output does it create?
- Why was Spark appropriate for this task?
"""

def main():
    from pyspark.sql import SparkSession
    from pyspark.ml.feature import VectorAssembler
    from pyspark.ml.regression import LinearRegression
    import happybase

    # Step 1: Create a Spark session
    spark = SparkSession.builder.appName("MLlib CostofLiving Est").enableHiveSupport().getOrCreate()

    # Step 2: Load the data from the Hive table 'gradesml' into a Spark DataFrame
    econdata_df = spark.sql("SELECT case_id, state_abv, county, "
                            "housing, total_cost, min_wage,"
                            "taxes, metro_level FROM econdata_ilwi")

    # Step 3: Handle null values by either dropping or filling them
    econdata_df = econdata_df.na.drop()  # Drop rows with null values

    # Step 4: Prepare the data for MLlib by assembling features into a vector
    assembler = VectorAssembler(
        inputCols=["housing", "min_wage", "taxes", "metro_level"],
        outputCol="features",
        handleInvalid="skip"  # Skip rows with null values
    )
    assembled_df = assembler.transform(econdata_df).select("features", "total_cost")

    # Step 5: Split the data into training and testing sets
    train_data, test_data = assembled_df.randomSplit([0.7, 0.3])

    # Step 6: Initialize and train a Linear Regression model
    lr = LinearRegression(labelCol="total_cost")
    lr_model = lr.fit(train_data)

    # Step 7: Evaluate the model on the test data
    test_results = lr_model.evaluate(test_data)

    # Step 8: Print the model performance metrics
    print(f"RMSE: {test_results.rootMeanSquaredError}")
    print(f"R^2: {test_results.r2}")

    # ---- Write metrics to HBase with happybase (using the provided pattern) ----
    # Example data (row_key, column_family:column, value) populated with the metrics
    data = [
        ('metrics1', 'cf:rmse', str(test_results.rootMeanSquaredError)),
        ('metrics1', 'cf:r2', str(test_results.r2)),
    ]

    # Function to write data to HBase inside each partition
    def write_to_hbase_partition(partition):
        connection = happybase.Connection('master')
        connection.open()
        table = connection.table('econ_metrics')  # Update table name
        for row in partition:
            row_key, column, value = row
            table.put(row_key, {column: value})
        connection.close()

    # Parallelize data and apply the function with foreachPartition
    rdd = spark.sparkContext.parallelize(data)
    rdd.foreachPartition(write_to_hbase_partition)

    # Step 9: Stop the Spark session
    spark.stop()


if __name__ == "__main__":
    main()

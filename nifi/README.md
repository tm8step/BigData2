# Apache NiFi — Data Ingestion into HDFS

## Role in the Pipeline

Apache NiFi provides the ingestion and orchestration layer for this project. The completed flow retrieves the project dataset and writes it into HDFS for downstream processing.

## Source Dataset

**Dataset:** [econdata_ilwi.csv]  
**GitHub direct URL:** [https://raw.githubusercontent.com/tm8step/BigData2/refs/heads/main/sample-data/econdata_ilwi.csv]

The data contains economic data for 174 counties across Illinois and Wisconsin.

It has 3 id columns:  'case_id' INT, 'state_abv' STR and 'county' STR
It has 5 economic descriptive indicators, 'housing' FLOAT, 'total_cost' FLOAT, 'min_wage' FLOAT, 'taxes' FLOAT and 'metro_level' INT


Citation and Data Source:

Economic Policy Institute. (2026, July 1). The Economic Policy Institute Minimum Wage Tracker. Economic Policy Institute. Retrieved August 23, 2026, from https://www.epi.org/minimum-wage-tracker/

National Center for Health Statistics. (2024, September 17). NCHS Urban-Rural Classification Scheme for Counties | National Center for Health Statistics. CDC. Retrieved August 23, 2026, from https://www.cdc.gov/nchs/data-analysis-tools/urban-rural.html

## Flow Design

Describe the important processors used in the final NiFi flow and the role each processor performs.

| Processor / Process Group | Role in the Flow |
|---|---|
| Download File | Downloads the file from the Github repository and starts it in the Nifi data Flow|
| Update File Name | Renames the filename to the given filename in the parameter context.  In this case, the output filename is 'econdata_ilwi.csv' |
| Write File to HDFS | Writes the data to the HDFS folder given in the parameter context.  In this case, the folder is '/data' |

Explain how data moves from the source URL through NiFi and into HDFS.

## HDFS Destination

**HDFS path:** `/data`

Explain where NiFi writes the dataset and how the destination is used by the next stage of the pipeline.

Nifi writes the dataset to my HDFS drive, in the /data folder.  Here it can be read by other data programs such as Hive for querying.

## Execution Evidence

### Final NiFi Flow

![NiFi Flow](screenshots/nifi-flow.png)

### Running Flow / Queue Activity

![NiFi Running](screenshots/nifi-running.png)

### HDFS Ingestion Verification

![HDFS Verification](screenshots/hdfs-ingestion-verification.png)

The HDFS screenshot should show the `hdfs dfs -ls` output confirming that the project dataset was successfully written into HDFS.

Pipeline Flow:

Data Generator → Simulates banking transactions, accounts & customers (via Faker).
Kafka + Debezium → Streams change data (CDC) into MinIO (S3-compatible storage).
Airflow → Orchestrates data ingestion & snapshots into Snowflake.
Snowflake → Cloud Data Warehouse (Bronze → Silver → Gold).
DBT → Applies transformations, builds marts & snapshots (SCD Type-2).

Pipeline Flow:

1. Data Generator → Simulates banking transactions, accounts & customers (via Faker).
2. Kafka + Debezium → Streams change data (CDC) into MinIO (S3-compatible storage).
3. Airflow → Orchestrates data ingestion & snapshots into Snowflake.
4. Snowflake → Cloud Data Warehouse (raw storage (variant) -> staging -> final table).
5. DBT → Applies transformations, builds marts & snapshots (SCD Type-2).


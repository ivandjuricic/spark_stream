STREAM_NAME = "testSparkStreaming"
ENDPOINT_URL = 'https://kinesis.us-west-2.amazonaws.com'
AWS_REGION = 'us-west-2'
AWS_ROLE_ARN = "arn:aws:iam::027642465353:role/DatabricksDevCrossAccountRole"
PARQUET_LOCATION = "streamingData"
CHECKPOINT_LOCATION = "_streamingDataCheckPoint"
B = "datapipe-dev-slots"

KINESIS_INITIAL_POSITION = "latest"
KINESIS_SHARDS_PER_TASK = 5
KINESIS_MIN_FETCH_PERIOD = "400ms" #"210ms"
KINESIS_MAX_FETCH_DURATION = "10s"  #"200ms"
KINESIS_RETENTION_PERIOD = 24  # IN HOURS
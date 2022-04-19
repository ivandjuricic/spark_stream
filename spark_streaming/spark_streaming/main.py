from spark_streaming.utils.const import STREAM_NAME, AWS_REGION, AWS_ROLE_ARN, KINESIS_INITIAL_POSITION, B
from pyspark.sql import SparkSession


spark = SparkSession.builder.master(
    "local[*, 4]"
).appName(
    "StructureStream"
).enableHiveSupport(
).getOrCreate()


def foreach_batch_function(df, epoch_id):
    if len(df.head(1)) != 0:
        df.write.mode(
            "append"
        ).parquet("s3a://{B}/data_test_package_table")


def main():
    kinesis = spark.readStream \
        .format("kinesis") \
        .option("streamName", STREAM_NAME) \
        .option("region", AWS_REGION) \
        .option("roleArn", AWS_ROLE_ARN) \
        .option("initialPosition", KINESIS_INITIAL_POSITION) \
        .load()

    df = kinesis.selectExpr(
        "CAST(data as STRING) as json_data"
    )

    df.writeStream \
        .trigger(processingTime="5 seconds") \
        .option("checkpointLocation", f"s3a://{B}/test_package_checkpoint") \
        .foreachBatch(foreach_batch_function) \
        .start()

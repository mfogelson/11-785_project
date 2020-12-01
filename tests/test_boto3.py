import boto3


def test_project_s3_bucket_exists(bucket_name="youshen"):
    s3 = boto3.resource("s3")
    buckets = [bucket.name for bucket in s3.buckets.all()]
    assert(bucket_name in buckets)

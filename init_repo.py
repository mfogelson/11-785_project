import multiprocessing
import os
import boto3
import botocore
import fire
from typing import List
from settings import settings
from util import create_directories

# make a per process s3 client and bucket
s3 = None
bucket_name = settings.AWS_BUCKET_NAME
bucket = None


def initialize():
    # adapted from senderle: https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
    global s3
    global bucket
    s3 = boto3.resource(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    bucket = s3.Bucket(bucket_name)


# the work function of each process which will fetch something from s3
def download(job):
    # adapted from senderle: https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
    bucket_name, key, filename = job
    print(f"Downloading from {bucket_name}: {key}")
    bucket.download_file(key, filename)


def download_data_files(
    *args: str,
):
    """
    Parameters
    ----------
    *args: Str
        Names of remote directories to download

    Returns
    ----------
    None

    Examples
    ----------
    Use by calling the function
    >>> from init_repo import download_data_files
    >>> dirs = ["samples", "corpuses"]
    >>> download_data_files(*dirs)
    Or use as a cli
    >>> python init_repo.py samples corpuses
    """

    if len(args) == 0:
        remote_directories = settings.DATA_DIRECTORIES
        print(f"No directories provided as input args. Using DATA_DIRECTORIES in .env")
    else:
        remote_directories = list(args)
    print(remote_directories)

    remote_directories = [
        name if str(name).endswith("/") else f"{name}/" for name in remote_directories
    ]
    create_directories(remote_directories)

    initialize()
    file_keys = []
    for remote_directory in remote_directories:
        remote_directory_file_keys = [
            obj.key
            for obj in bucket.objects.filter(Prefix=remote_directory)
            if not os.path.isdir(obj.key)
        ]
        if len(remote_directory_file_keys) == 0:
            print(
                f"There aren't valid files to retrieve in the remote folder {remote_directory}. Perhaps you're using a wrong folder name?"
            )
        else:
            file_keys.extend(remote_directory_file_keys)

    jobs = [(bucket_name, file_key, file_key) for file_key in file_keys]

    # make a process pool to do the work
    pool = multiprocessing.Pool(multiprocessing.cpu_count(), initialize)
    pool.map(download, jobs)
    pool.close()
    pool.join()


if __name__ == "__main__":
    fire.Fire(download_data_files)

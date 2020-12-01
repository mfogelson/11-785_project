import ast
import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel


class Settings(BaseModel):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_BUCKET_NAME: str
    DATA_DIRECTORIES: List


load_dotenv()
settings = {
    "AWS_USER": os.environ["AWS_USER"],
    "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
    "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"],
    "AWS_BUCKET_NAME": os.environ["AWS_BUCKET_NAME"],
    "DATA_DIRECTORIES": ast.literal_eval(os.environ["DATA_DIRECTORIES"]),
}
settings = Settings(**settings)

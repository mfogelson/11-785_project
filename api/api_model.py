"""The :mod:`api.api_model` module provides functions data classes 
for modelling poems and input from users 
"""
# Author: Christopher Dare
from pydantic import BaseModel


class KeyGen(BaseModel):
    user_input: str

import logging
from typing import List

from fastapi import FastAPI
import numpy as np
from api.api_model import KeyGen
import requests
from requests.exceptions import ConnectionError


app = FastAPI()
# model = None  # TODO: initialize some object that will serve as a wrapper for the model
limerick_path = 'corpuses/limericks.txt'
sample_path = 'corpuses/rhyming_AABB.txt'


def parse_limerick(limerick_path):
    limerick = ""
    limericks = []
    with open(limerick_path, 'r') as f:
        for line in f.readlines():
            if line != "\n":
                limerick += line + "\n"
            else:
                limericks.append(limerick)
                limerick = ""
    return limericks


def parse_sample(sample_path):
    samples = []
    sample = ""
    with open(sample_path, 'r') as f:
        for line in f.readlines():
            if "<|endoftext|>" not in line:
                first = line.split('|$|')[0] + "\n\n"
                sample += first
                second = line.split('|$|')[1] + "\n\n"
                sample += second
            else:
                samples.append(sample)
                sample = ""
    return samples


def get_random_limerick(limericks):
    '''
    Args:
    limericks (list) -> list of limericks

    Returns:
    limerick (list) -> random limerick
    '''

    ind = np.random.randint(0, len(limericks), 1)

    return limericks[ind.item()], ind.item()



@app.get("/")
def root():
    """Root endpoint for detection by load balancers.
    """
    return {"message": "API running."}


@app.post("/generate")
async def generate(keyGen: KeyGen):
    user_input = keyGen.user_input
    payload = "Generating a poem given: " + user_input
    status = True
    try:
        response = requests.get(f"http://128.2.116.248:5000")
        generated = response.text
    except ConnectionError as e:
        generated = ""
        status = False
    response = {"success": status, "payload": payload, "generated": generated}
    return response


@app.post("/retrieve")
def retrieve():
    # get human and model generated poems
    limericks = parse_limerick(limerick_path)
    human_text, human_text_idx = get_random_limerick(limericks)
    samples = parse_sample(sample_path)
    model_text, model_text_idx = get_random_limerick(samples)
    # shuffle and record the ground truth
    text_list = [human_text, model_text]
    indices = [0, 1]  # before shuffling: 0: human, 1: model
    np.random.shuffle(indices)  # shuffle
    ground_truth = "0" if indices[0] == 1 else "1"
    text_shuffle = [text_list[i] for i in indices]
    status = True
    response = {"success": status, "text1": text_shuffle[0], "text2": text_shuffle[1], "human_text_idx": human_text_idx,
                "model_text_idx": model_text_idx, "ground_truth": ground_truth}
    return response

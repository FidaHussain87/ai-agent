from celery import shared_task
import torch
from tasks.utils import load_model
import pandas as pd

@shared_task
def run_inference(agent_id: int, input_data: dict):
    model = load_model(agent_id)
    input_tensor = torch.tensor([list(input_data.values())], dtype=torch.float32)
    output = model(input_tensor)
    return {"prediction": output.item()}

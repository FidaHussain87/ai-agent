import torch
import os

BASE_DIR = os.getenv("MODEL_DIR", "./model_registry")

def save_model(agent_id: int, model):
    agent_path = os.path.join(BASE_DIR, str(agent_id))
    os.makedirs(agent_path, exist_ok=True)
    file_path = os.path.join(agent_path, "model.pt")
    torch.save(model.state_dict(), file_path)
    return file_path

def load_model(agent_id: int):
    from torch import nn
    path = os.path.join(BASE_DIR, str(agent_id), "model.pt")
    model = nn.Sequential(
        nn.Linear(4, 16),  # assume 4 input features for example
        nn.ReLU(),
        nn.Linear(16, 1),
        nn.Sigmoid()
    )
    model.load_state_dict(torch.load(path))
    model.eval()
    return model

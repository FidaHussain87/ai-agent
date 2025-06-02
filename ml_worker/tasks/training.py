from celery import shared_task
import os
import torch
from torch import nn
import pandas as pd
from tasks.utils import save_model

@shared_task
def train_agent(agent_id: int, data_path: str, num_epochs: int = 10):
    df = pd.read_csv(data_path)
    X = torch.tensor(df.drop('label', axis=1).values, dtype=torch.float32)
    y = torch.tensor(df['label'].values, dtype=torch.float32).view(-1, 1)

    model = nn.Sequential(
        nn.Linear(X.shape[1], 16),
        nn.ReLU(),
        nn.Linear(16, 1),
        nn.Sigmoid()
    )

    loss_fn = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(num_epochs):
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model_path = save_model(agent_id, model)
    return {"status": "trained", "model_path": model_path}

import torch
import torch.cuda.amp as amp
import torch.nn as nn

import src.misc.dist as dist
from src.core import register

__all__ = ["GradScaler"]

GradScaler = register(amp.grad_scaler.GradScaler)

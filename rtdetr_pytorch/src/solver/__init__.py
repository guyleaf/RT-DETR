"""by lyuwenyu"""

from typing import Dict

from .det_solver import DetSolver
from .solver import BaseSolver

TASKS: Dict[str, BaseSolver] = {
    "detection": DetSolver,
}

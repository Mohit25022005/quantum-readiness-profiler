from dataclasses import dataclass

@dataclass
class ProblemProfile:
    """
    Represents characteristics of a computational problem
    to evaluate its quantum readiness.
    """
    parallelism: float
    scaling_advantage: float
    noise_sensitivity: float
    probabilistic_tolerance: float
    problem_structure: float
    classical_efficiency: float

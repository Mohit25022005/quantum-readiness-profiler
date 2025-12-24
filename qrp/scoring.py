from qrp.profile import ProblemProfile

def quantum_suitability_score(profile: ProblemProfile) -> float:
    """
    Computes a quantum suitability score in range [0, 1].
    """
    weights = {
        "parallelism": 0.2,
        "scaling_advantage": 0.25,
        "problem_structure": 0.2,
        "probabilistic_tolerance": 0.15,
        "noise_sensitivity": -0.1,
        "classical_efficiency": -0.1,
    }

    score = (
        weights["parallelism"] * profile.parallelism +
        weights["scaling_advantage"] * profile.scaling_advantage +
        weights["problem_structure"] * profile.problem_structure +
        weights["probabilistic_tolerance"] * profile.probabilistic_tolerance +
        weights["noise_sensitivity"] * profile.noise_sensitivity +
        weights["classical_efficiency"] * profile.classical_efficiency
    )

    return max(0.0, min(score, 1.0))


def recommendation(score: float) -> str:
    """
    Returns recommended approach based on score.
    """
    if score < 0.4:
        return "Classical"
    elif score < 0.7:
        return "Hybrid Quantum–Classical"
    else:
        return "Quantum"

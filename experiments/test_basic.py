from qrp.profile import ProblemProfile
from qrp.scoring import quantum_suitability_score, recommendation

profile = ProblemProfile(
    parallelism=0.8,
    scaling_advantage=0.9,
    noise_sensitivity=0.6,
    probabilistic_tolerance=0.8,
    problem_structure=0.7,
    classical_efficiency=0.4
)

score = quantum_suitability_score(profile)
print("Score:", score)
print("Recommendation:", recommendation(score))

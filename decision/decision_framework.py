# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Programmatic Decision Framework Model
# ==============================================================================
"""Decision framework for structured alternatives analysis and recommendations."""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Alternative:
    """An objective path forward, strictly requiring pros and cons."""
    id: int
    description: str
    pros: List[str]
    cons: List[str]

    @property
    def is_valid(self) -> bool:
        """Check if alternative has at least one pro and one con."""
        return len(self.pros) > 0 and len(self.cons) > 0

@dataclass
class Analysis:
    """The logical defense of reality. Must be the heaviest part of the model."""
    facts: List[str] = field(default_factory=list)
    warrants: List[str] = field(default_factory=list)

    @property
    def total_points(self) -> int:
        """Calculate total number of facts and warrants."""
        return len(self.facts) + len(self.warrants)

class DecisionEngine:
    """Engine for structured decision making with alternatives analysis."""

    def __init__(self, problem_statement: str):
        """Initialize decision engine with problem statement."""
        self.problem_statement = problem_statement
        self.analysis = Analysis()
        self.alternatives: dict[int, Alternative] = {}
        self.recommended_ids: List[int] = []
        self.justification: str = ""
        self.implementation_steps: List[str] = []
        self.conclusion: str = ""

    def add_fact(self, fact: str):
        """Add a fact to the analysis."""
        self.analysis.facts.append(fact)

    def add_warrant(self, warrant: str):
        """Add a warrant to the analysis."""
        self.analysis.warrants.append(warrant)

    def add_alternative(
        self,
        alt_id: int,
        description: str,
        pros: List[str],
        cons: List[str]
    ):
        """Add an alternative to consider."""
        if len(self.alternatives) >= 8:
            raise ValueError("Framework Limit: Cannot exceed 8 alternatives.")

        alt = Alternative(id=alt_id, description=description, pros=pros, cons=cons)
        if not alt.is_valid:
            msg = f"Alternative {alt_id} must have at least one pro and one con."
            raise ValueError(msg)

        self.alternatives[alt_id] = alt

    def set_recommendation(self, alt_ids: List[int], justification: str):
        """Set recommended alternatives with justification."""
        if len(alt_ids) < 1 or len(alt_ids) > 2:
            raise ValueError("Must recommend exactly 1 or 2 alternatives.")
        for alt_id in alt_ids:
            if alt_id not in self.alternatives:
                raise ValueError(f"Alternative {alt_id} does not exist.")
        self.recommended_ids = alt_ids
        self.justification = justification

    def add_implementation_step(self, step: str):
        """Add an implementation step."""
        self.implementation_steps.append(step)

    def set_conclusion(self, conclusion: str):
        """Set the conclusion."""
        self.conclusion = conclusion

    def evaluate_architecture(self) -> dict:
        """Evaluate the decision framework architecture for completeness."""
        errors = []
        if self.analysis.total_points < 3:
            msg = (
                "Analysis is too light. Must be the longest section. "
                "Add more facts and warrants."
            )
            errors.append(msg)
        if len(self.alternatives) < 1 or len(self.alternatives) > 8:
            errors.append("Must have between 1 and 8 viable alternatives.")
        if not self.recommended_ids:
            errors.append("No recommendation has been made.")
        if not self.implementation_steps:
            errors.append("Missing implementation steps.")

        status = "VALID" if not errors else "INVALID"
        return {"status": status, "errors": errors}

if __name__ == "__main__":
    decision = DecisionEngine("System lacks momentum in the second act.")
    decision.add_fact("Act 2 drops the BPM.")
    decision.add_warrant("If energy drops for more than 7 minutes, retention breaks.")
    decision.add_fact("Act 2 is ambient.")

    decision.add_alternative(1, "Cut ambient section.", ["Fixes runtime"], ["Loses narrative beat"])
    decision.add_alternative(2, "Swap Act 1 and 2.", ["Maintains flow"], ["Requires transition mixing"])

    decision.set_recommendation([2], "Alternative 2 outweighs the single con.")
    decision.add_implementation_step("1. Load session and swap.")
    decision.set_conclusion("Sequence will maintain tension.")

    res = decision.evaluate_architecture()
    print(f"Structure check: {res['status']}")

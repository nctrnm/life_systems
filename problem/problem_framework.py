# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Problem Framework Equation Model
# ==============================================================================

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ProblemVariable:
    """Represents a single variable in the problem equation."""
    name: str
    description: str
    is_self_influenced: bool = False

class SystemState:
    """
    Evaluates the state of a system based on the equation: 
    Problem = f(Trigger, Context, Conflict, Impact)
    """
    def __init__(
        self, 
        trigger: Optional[ProblemVariable] = None,
        context: Optional[ProblemVariable] = None,
        conflict: Optional[ProblemVariable] = None,
        impact: Optional[ProblemVariable] = None
    ):
        self.trigger = trigger
        self.context = context
        self.conflict = conflict
        self.impact = impact

    @property
    def _variables(self) -> List[ProblemVariable]:
        """Returns a list of currently defined variables in logical order."""
        return [v for v in [self.trigger, self.context, self.conflict, self.impact] if v is not None]

    @property
    def defined_count(self) -> int:
        return len(self._variables)

    @property
    def is_problem(self) -> bool:
        """A true problem exists ONLY if all 4 variables are defined."""
        return self.defined_count == 4

    @property
    def is_problematic(self) -> bool:
        """Problematic: Having 1 to 3 variables, but lacking the full equation."""
        return 1 <= self.defined_count <= 3

    @property
    def is_internal_problem(self) -> bool:
        """
        When you are the problem: All defined elements are self-influenced.
        Returns True if it's a full problem AND all factors are internal.
        """
        if not self.is_problem:
            return False
        return all(var.is_self_influenced for var in self._variables)

    def diagnose(self) -> str:
        """Returns a diagnostic string based on the current state."""
        if self.is_internal_problem:
            return "Status: INTERNAL PROBLEM. You are the root cause setting the friction in motion. Behavioral shift required."
        elif self.is_problem:
            return "Status: DEFINED PROBLEM. Source identified. Ready for logistical or strategic resolution."
        elif self.is_problematic:
            missing = [
                name for name, val in [
                    ("Trigger", self.trigger), ("Context", self.context), 
                    ("Conflict", self.conflict), ("Impact", self.impact)
                ] if val is None
            ]
            return f"Status: PROBLEMATIC. Missing variables: {', '.join(missing)}. Cannot be solved yet."
        else:
            return "Status: EMPTY. No variables defined."

if __name__ == "__main__":
    internal_bottleneck = SystemState(
        trigger=ProblemVariable("Trigger", "The Root Cause: Your specific behavior or blind spot acting as the catalyst.", True),
        context=ProblemVariable("Context", "Self-Imposed Rules: Habits, assumptions, and personal narratives setting the baseline.", True),
        conflict=ProblemVariable("Conflict", "Internal Friction: Self-sabotage or cognitive dissonance.", True),
        impact=ProblemVariable("Impact", "Self-Inflicted Damage: Burnout or stalled projects.", True)
    )

    print("--- Scenario 1: The Internal Problem ---")
    print(internal_bottleneck.diagnose())

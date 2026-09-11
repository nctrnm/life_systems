# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Problem Framework Equation Model
# ==============================================================================
"""Problem framework for systematically analyzing and diagnosing issues."""

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ProblemVariable:
    """Represents a single variable in the problem equation."""
    name: str
    description: str
    is_self_influenced: bool = False

class SystemState:
    """Evaluates system state using problem equation.

    Problem = f(Trigger, Context, Conflict, Impact)
    """

    def __init__(
        self,
        trigger: Optional[ProblemVariable] = None,
        context: Optional[ProblemVariable] = None,
        conflict: Optional[ProblemVariable] = None,
        impact: Optional[ProblemVariable] = None
    ):
        """Initialize system state with problem variables."""
        self.trigger = trigger
        self.context = context
        self.conflict = conflict
        self.impact = impact

    @property
    def _variables(self) -> List[ProblemVariable]:
        """Return list of currently defined variables in logical order."""
        return [
            v for v in [
                self.trigger, self.context, self.conflict, self.impact
            ] if v is not None
        ]

    @property
    def defined_count(self) -> int:
        """Get count of defined problem variables."""
        return len(self._variables)

    @property
    def is_problem(self) -> bool:
        """Check if a true problem exists (all 4 variables defined)."""
        return self.defined_count == 4

    @property
    def is_problematic(self) -> bool:
        """Check if problematic (1-3 variables, but lacking full equation)."""
        return 1 <= self.defined_count <= 3

    @property
    def is_internal_problem(self) -> bool:
        """Check if all defined elements are self-influenced.

        Returns True if it's a full problem AND all factors are internal.
        """
        if not self.is_problem:
            return False
        return all(var.is_self_influenced for var in self._variables)

    def diagnose(self) -> str:
        """Return diagnostic string based on current state."""
        if self.is_internal_problem:
            return (
                "Status: INTERNAL PROBLEM. You are the root cause setting the "
                "friction in motion. Behavioral shift required."
            )
        if self.is_problem:
            return (
                "Status: DEFINED PROBLEM. Source identified. Ready for "
                "logistical or strategic resolution."
            )
        if self.is_problematic:
            missing = [
                name for name, val in [
                    ("Trigger", self.trigger), ("Context", self.context),
                    ("Conflict", self.conflict), ("Impact", self.impact)
                ] if val is None
            ]
            return (
                f"Status: PROBLEMATIC. Missing variables: {', '.join(missing)}. "
                "Cannot be solved yet."
            )
        return "Status: EMPTY. No variables defined."

if __name__ == "__main__":
    internal_bottleneck = SystemState(
        trigger=ProblemVariable(
            "Trigger",
            "The Root Cause: Your specific behavior or blind spot acting as "
            "the catalyst.",
            True
        ),
        context=ProblemVariable(
            "Context",
            "Self-Imposed Rules: Habits, assumptions, and personal narratives "
            "setting the baseline.",
            True
        ),
        conflict=ProblemVariable(
            "Conflict",
            "Internal Friction: Self-sabotage or cognitive dissonance.",
            True
        ),
        impact=ProblemVariable(
            "Impact",
            "Self-Inflicted Damage: Burnout or stalled projects.",
            True
        )
    )

    print("--- Scenario 1: The Internal Problem ---")
    print(internal_bottleneck.diagnose())

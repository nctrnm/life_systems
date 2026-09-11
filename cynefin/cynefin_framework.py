# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Cynefin Complexity Mapping Model
# Attribution: This reference model adapts concepts from the Cynefin framework,
# associated with Dave Snowden, Cognitive Edge, and The Cynefin Company.
# Life Systems does not claim ownership of Cynefin terminology or its domain model.
# ==============================================================================
"""Cynefin framework implementation for categorizing problem complexity domains."""

from enum import Enum
from dataclasses import dataclass

class Domain(Enum):
    """Complexity domains in the Cynefin framework."""
    CLEAR = "Clear"
    COMPLICATED = "Complicated"
    COMPLEX = "Complex"
    CHAOTIC = "Chaotic"
    CONFUSION = "Confusing"

@dataclass
class OperationalState:
    """Represents the characteristics of the problem's context."""
    is_trigger_obvious: bool
    is_context_stable: bool
    requires_expert_analysis: bool
    is_immediate_crisis: bool

class CynefinMapper:
    """Evaluates operational state to categorize environment and output action."""

    def __init__(self, state: OperationalState):
        """Initialize mapper with operational state."""
        self.state = state

    def map_domain(self) -> Domain:
        """Map the operational state to a Cynefin domain."""
        if self.state.is_immediate_crisis:
            return Domain.CHAOTIC
        if self.state.is_context_stable and self.state.is_trigger_obvious:
            return Domain.CLEAR
        if self.state.is_context_stable and self.state.requires_expert_analysis:
            return Domain.COMPLICATED
        if not self.state.is_context_stable and not self.state.is_trigger_obvious:
            return Domain.COMPLEX

        return Domain.CONFUSION

    def get_protocol(self) -> str:
        """Get the action protocol for the mapped domain."""
        domain = self.map_domain()
        protocols = {
            Domain.CLEAR: (
                "Action Method: Sense -> Categorize -> Respond.\n"
                "Protocol: Apply standard best practices. Cause and effect are known."
            ),
            Domain.COMPLICATED: (
                "Action Method: Sense -> Analyze -> Respond.\n"
                "Protocol: Bring in expert knowledge or conduct architectural analysis."
            ),
            Domain.COMPLEX: (
                "Action Method: Probe -> Sense -> Respond.\n"
                "Protocol: Run safe-to-fail experiments. Sketch and test before committing."
            ),
            Domain.CHAOTIC: (
                "Action Method: Act -> Sense -> Respond.\n"
                "Protocol: Triage immediately. Stabilize the system to stop the bleeding."
            ),
            Domain.CONFUSION: (
                "Action Method: Deconstruct.\n"
                "Protocol: Break the problem down into smaller components."
            )
        }
        return f"--- Domain: {domain.value} ---\n{protocols[domain]}"

if __name__ == "__main__":
    complex_state = OperationalState(
        is_trigger_obvious=False,
        is_context_stable=False,
        requires_expert_analysis=False,
        is_immediate_crisis=False
    )

    mapper = CynefinMapper(complex_state)
    print(mapper.get_protocol())

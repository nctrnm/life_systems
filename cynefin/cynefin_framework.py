# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Cynefin Complexity Mapping Model
# Attribution: This reference model adapts concepts from the Cynefin framework,
# associated with Dave Snowden, Cognitive Edge, and The Cynefin Company.
# Life Systems does not claim ownership of Cynefin terminology or its domain model.
# ==============================================================================

from enum import Enum
from dataclasses import dataclass

class Domain(Enum):
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
    """
    Evaluates the operational state to categorize the environment and 
    output the correct action protocol.
    """
    def __init__(self, state: OperationalState):
        self.state = state

    def map_domain(self) -> Domain:
        if self.state.is_immediate_crisis:
            return Domain.CHAOTIC
        elif self.state.is_context_stable and self.state.is_trigger_obvious:
            return Domain.CLEAR
        elif self.state.is_context_stable and self.state.requires_expert_analysis:
            return Domain.COMPLICATED
        elif not self.state.is_context_stable and not self.state.is_trigger_obvious:
            return Domain.COMPLEX
        
        return Domain.CONFUSION

    def get_protocol(self) -> str:
        domain = self.map_domain()
        protocols = {
            Domain.CLEAR: "Action Method: Sense -> Categorize -> Respond.\nProtocol: Apply standard best practices. Cause and effect are known.",
            Domain.COMPLICATED: "Action Method: Sense -> Analyze -> Respond.\nProtocol: Bring in expert knowledge or conduct architectural analysis.",
            Domain.COMPLEX: "Action Method: Probe -> Sense -> Respond.\nProtocol: Run safe-to-fail experiments. Sketch and test before committing.",
            Domain.CHAOTIC: "Action Method: Act -> Sense -> Respond.\nProtocol: Triage immediately. Stabilize the system to stop the bleeding.",
            Domain.CONFUSION: "Action Method: Deconstruct.\nProtocol: Break the problem down into smaller components until they fit a known domain."
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

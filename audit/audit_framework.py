# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Programmatic Post-Mortem & Audit Model
# ==============================================================================

from dataclasses import dataclass
from typing import Optional

@dataclass
class PostMortemData:
    """The raw data evaluated at the end of a sprint."""
    original_trigger: str
    is_trigger_neutralized: bool
    new_context: str
    emergent_friction: Optional[str] = None

class SystemAudit:
    """Evaluates the execution phase. Closes the loop or demands a reset."""
    def __init__(self, sprint_name: str, audit_data: PostMortemData):
        self.sprint_name = sprint_name
        self.data = audit_data

    @property
    def is_loop_closed(self) -> bool:
        return self.data.is_trigger_neutralized

    def generate_report(self) -> str:
        report = [
            f"SYSTEM AUDIT: {self.sprint_name}",
            f"Original Trigger: {self.data.original_trigger}",
            f"Neutralized?:     {'YES' if self.data.is_trigger_neutralized else 'NO'}\n"
        ]

        if self.is_loop_closed:
            report.append("[SUCCESS] Trigger neutralized. Loop closed.")
            report.append(f"Updated Context: {self.data.new_context}")
        else:
            report.append("[FAILURE] Trigger remains active. Return to /decision.")

        return "\n".join(report)

if __name__ == "__main__":
    success_data = PostMortemData(
        original_trigger="Act 2 kills momentum.",
        is_trigger_neutralized=True,
        new_context="Acts swapped. Energy is front-loaded."
    )
    audit = SystemAudit("Act 2 Swap", success_data)
    print(audit.generate_report())

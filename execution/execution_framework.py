# ==============================================================================
# Name: Matthew McGilvery
# Date: June 18, 2026
# Topic: Programmatic Execution & Bandwidth Protection Model
# ==============================================================================

from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    """An implementation step with an assigned bandwidth cost."""
    id: int
    description: str
    bandwidth_cost: int

    @property
    def is_valid(self) -> bool:
        return self.bandwidth_cost > 0

class SprintManager:
    """
    Translates decisions into actionable, strictly bound reality.
    Enforces the ultimate rule: You cannot exceed your maximum bandwidth.
    """
    def __init__(self, sprint_name: str, max_bandwidth: int):
        self.sprint_name = sprint_name
        self.max_bandwidth = max_bandwidth
        self.tasks: List[Task] = []
    
    @property
    def current_load(self) -> int:
        return sum(task.bandwidth_cost for task in self.tasks)
    
    @property
    def remaining_bandwidth(self) -> int:
        return self.max_bandwidth - self.current_load

    def add_task(self, task_id: int, description: str, cost: int):
        task = Task(id=task_id, description=description, bandwidth_cost=cost)
        if not task.is_valid:
            raise ValueError(f"Task {task_id} must have a cost > 0.")
            
        if self.current_load + task.bandwidth_cost > self.max_bandwidth:
            raise SystemError(
                f"BANDWIDTH EXCEEDED: Cannot add Task {task_id}. "
                f"Cost ({task.bandwidth_cost}) exceeds remaining capacity ({self.remaining_bandwidth})."
            )
        self.tasks.append(task)
        print(f"[+] Task {task_id} queued. Remaining bandwidth: {self.remaining_bandwidth}")

if __name__ == "__main__":
    sprint = SprintManager("Nctrnm Sprint", max_bandwidth=100)
    try:
        sprint.add_task(1, "Load session.", cost=30)
        sprint.add_task(2, "Update visual mapping.", cost=40)
        sprint.add_task(3, "Overcommit task.", cost=40) # Will raise error
    except SystemError as e:
        print(f"\n[ERROR] {e}\n")

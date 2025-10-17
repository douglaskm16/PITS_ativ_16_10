from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Task:
    id: int
    name: str
    description: str
    status: str = "pending"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }

class TodoList:
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def _validate_name(self, name: str):
        if name is None or not str(name).strip():
            raise ValueError("O nome da tarefa não pode ser vazio.")

    def add_task(self, name: str, description: str = "") -> int:
        """Adiciona uma tarefa e retorna seu id."""
        self._validate_name(name)
        tid = self._next_id
        self._next_id += 1
        task = Task(id=tid, name=name.strip(), description=str(description))
        self._tasks[tid] = task
        return tid

    def get_task(self, task_id: int) -> Task:
        """Retorna o objeto Task; lança ValueError se não existir."""
        task = self._tasks.get(task_id)
        if task is None:
            raise ValueError(f"Tarefa com id {task_id} não encontrada.")
        return task

    def mark_complete(self, task_id: int):
        t = self.get_task(task_id)
        t.status = "completed"

    def mark_in_progress(self, task_id: int):
        t = self.get_task(task_id)
        t.status = "in_progress"

    def edit_task(self, task_id: int, name: Optional[str] = None, description: Optional[str] = None):
        t = self.get_task(task_id)
        if name is not None:
            self._validate_name(name)
            t.name = name.strip()
        if description is not None:
            t.description = str(description)

    def delete_task(self, task_id: int):
        if task_id not in self._tasks:
            raise ValueError(f"Tarefa com id {task_id} não encontrada.")
        del self._tasks[task_id]

    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        """Se status fornecido, filtra por status ('pending', 'in_progress', 'completed')."""
        if status is None:
            return list(self._tasks.values())
        else:
            return [t for t in self._tasks.values() if t.status == status]

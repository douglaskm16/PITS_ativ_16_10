import unittest
from todo import TodoList, Task

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        tid = self.todo.add_task("Comprar leite", "Ir ao mercado")
        task = self.todo.get_task(tid)
        self.assertEqual(task.name, "Comprar leite")
        self.assertEqual(task.description, "Ir ao mercado")
        self.assertEqual(task.status, "pending")

    def test_mark_in_progress_and_complete(self):
        tid = self.todo.add_task("Estudar", "Capítulo 3")
        self.todo.mark_in_progress(tid)
        self.assertEqual(self.todo.get_task(tid).status, "in_progress")
        self.todo.mark_complete(tid)
        self.assertEqual(self.todo.get_task(tid).status, "completed")

    def test_edit_task(self):
        tid = self.todo.add_task("Antigo", "Velha descrição")
        self.todo.edit_task(tid, name="Novo nome", description="Nova descrição")
        t = self.todo.get_task(tid)
        self.assertEqual(t.name, "Novo nome")
        self.assertEqual(t.description, "Nova descrição")

    def test_delete_task(self):
        tid = self.todo.add_task("Remover", "Será removida")
        self.todo.delete_task(tid)
        with self.assertRaises(ValueError):
            self.todo.get_task(tid)

    def test_list_tasks_and_filter(self):
        id1 = self.todo.add_task("t1", "d1")
        id2 = self.todo.add_task("t2", "d2")
        self.todo.mark_complete(id2)
        all_tasks = self.todo.list_tasks()
        self.assertEqual(len(all_tasks), 2)
        completed = self.todo.list_tasks(status="completed")
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].id, id2)

    def test_invalid_operations_raise(self):
        with self.assertRaises(ValueError):
            self.todo.mark_complete(999)
        with self.assertRaises(ValueError):
            self.todo.edit_task(999, name="x")
        with self.assertRaises(ValueError):
            self.todo.add_task("", "sem nome")

if __name__ == '__main__':
    unittest.main()

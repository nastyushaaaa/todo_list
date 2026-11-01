import unittest
import main

class TestTodoList(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()

    def test_add_task(self):
        main.add_task("Подготовить отчет")

        self.assertEqual(len(main.tasks), 1)
        self.assertEqual(main.tasks[0]["title"], "Подготовить отчет")
        self.assertFalse(main.tasks[0]["completed"])

    def test_delete_task(self):
        main.add_task("Подготовить отчет")

        main.delete_task(0)

        self.assertEqual(len(main.tasks), 0)

    def test_complete_task(self):
        main.add_task("Подготовить отчет")

        main.complete_task(0)

        self.assertTrue(main.tasks[0]["completed"])

    def test_add_empty_task(self):
        result = main.add_task("")

        self.assertFalse(result)
        self.assertEqual(len(main.tasks), 0)

if __name__ == "__main__":
    unittest.main()

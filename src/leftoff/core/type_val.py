from typing import Any


class InvalidTodo(Exception):
    pass


def validate_task(task: Any) -> bool:
    return (
        isinstance(task, dict)
        and isinstance(task.get("id"), int)
        and isinstance(task.get("task"), str)
        and isinstance(task.get("status"), str)
        and isinstance(task.get("due"), str)
    )


def validate_todo(data: Any) -> bool:
    if not isinstance(data, dict):
        return False

    if not isinstance(data.get("title"), str):
        return False

    if not isinstance(data.get("version"), (int, float)):
        return False

    mode = data.get("mode")

    if not isinstance(mode, dict):
        return False

    for category, tasks in mode.items():
        if not isinstance(category, str):
            return False

        if not isinstance(tasks, list):
            return False

        if not all(validate_task(task) for task in tasks):
            return False

    return True

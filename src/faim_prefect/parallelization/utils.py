from typing import Callable

from prefect.futures import PrefectFuture


def wait_for_task_run(
    results: list,
    buffer: list[PrefectFuture],
    max_buffer_length: int = 6,
    result_insert_fn: Callable = lambda r: r.result(),
) -> None:
    """Wait for next task-run to complete.

    Useful when number of task-runs times task-run resource requirements
    exceed hardware limits.

    :param results: list to which task-run results are appended
    :param buffer: list holding submitted task-runs
    :param max_buffer_length: maximum number of submitted task-runs at a time
    :param result_insert_fn: function retrieving the result of a completed
    task-run
    """
    while len(buffer) >= max(1, max_buffer_length):
        results.append(result_insert_fn(buffer.pop(0)))
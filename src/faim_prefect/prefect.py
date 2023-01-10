import json
from os.path import join
from typing import Dict

from prefect import get_run_logger, task
from prefect.context import FlowRunContext


def get_prefect_context(context: FlowRunContext) -> Dict:
    """
    Collect prefect context.

    :return:
    """
    return {
        "start_time": context.flow_run.start_time.strftime("%Y-%m-%d " "%H:%M:%S"),
        "flow_id": context.flow_run.flow_id,
        "flow_run_id": context.flow_run.id,
        "flow_run_version": context.flow_run.flow_version,
        "flow_run_name": context.flow_run.name,
        "deployment_id": context.flow_run.deployment_id,
    }


@task()
def save_prefect_context_task(output_dir: str, context: FlowRunContext):
    """
    Dump prefect context into prefect-context.json.

    :param output_dir:
    :param context_dict:
    :return:

    Example
    -------
    context = get_run_context() # In the flow function <- Gives the
    FlowRunContext
    save_prefect_context_task(output_dir, context)
    """
    context_dict = get_prefect_context(context=context)
    logger = get_run_logger()

    outpath = join(output_dir, "prefect-context.json")
    with open(outpath, "w") as f:
        json.dump(context_dict, f, indent=4)

    logger.info(f"Saved prefect context information to {outpath}.")

import json
from os.path import join
from typing import Dict

import prefect
from prefect import task


@task()
def get_prefect_context_task() -> Dict:
    """
    Collect prefect context.

    :return:
    """
    return {
        "date": prefect.context.get("date").strftime("%Y-%m-%d %H:%M:%S"),
        "flow_id": prefect.context.get("flow_id"),
        "flow_run_id": prefect.context.get("flow_run_id"),
        "flow_run_version": prefect.context.get("flow_run_version"),
        "flow_run_name": prefect.context.get("flow_run_name"),
    }


@task()
def save_prefect_context_task(output_dir: str, context_dict: Dict):
    """
    Dump prefect context into prefect-context.json.

    :param output_dir:
    :param context_dict:
    :return:
    """
    logger = prefect.context.get("logger")

    outpath = join(output_dir, "prefect-context.json")
    with open(outpath, "w") as f:
        json.dump(context_dict, f, indent=4)

    logger.info(f"Saved prefect context information to {outpath}.")

import json
import logging
import subprocess
from os.path import join
from typing import Dict

from prefect import task
from prefect.tasks.airtable import airtable


@task()
def save_slurm_job_info(output_dir: str, slurm_info_dict: Dict, logger=logging) -> None:
    """
    :param output_dir:
    :param slurm_info_dict:
    :param logger:
    :return:
    """
    outpath = join(output_dir, "slurm-job-info.json")
    with open(outpath, "w") as f:
        json.dump(slurm_info_dict, f, indent=4)

    logger.info(f"Saved slurm job information to {outpath}.")


@task()
def get_slurm_job_info(jobid: str, logger=logging):
    """
    Collect info about slurm job from slurm.

    :param jobid:
    :param logger:
    :return: job info
    """
    cmd = f"scontrol show jobid --d {jobid} -o"
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True)
    result.check_returncode()

    output = result.stdout.decode("utf-8")
    output_dict = {}
    for i in output.split():
        splitted = i.split("=")
        if len(splitted) > 1:
            output_dict[splitted[0]] = splitted[1]
        else:
            output_dict[splitted[0]] = None

    assert output_dict["JobId"] == str(jobid), logger.error("JobId does not " "match.")

    return output_dict


@task()
def log_slurm_flow_run_to_airtable(
    prefect_context: Dict,
    slurm_info_dict: Dict,
    base_key: str,
    table_name: str,
    api_key: str,
):
    """
    Log prefect slurm-job to airtable.

    :param prefect_context:
    :param slurm_info_dict:
    :param base_key: of airtable database
    :param table_name: of airtable table
    :param api_key: of airtable
    :return:
    """
    table = airtable.Table(base_id=base_key, table_name=table_name, api_key=api_key)
    return table.create(
        {
            "slurm-job-id": slurm_info_dict["JobId"],
            "date-gmt": prefect_context["date"],
            "flow_id": prefect_context["flow_id"],
            "flow_run_id": prefect_context["flow_run_id"],
            "flow_run_name": prefect_context["flow_run_name"],
        }
    )

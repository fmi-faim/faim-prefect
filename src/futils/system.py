import json
import logging
from os.path import join

from distro import distro
from prefect import task


@task()
def save_system_information(output_dir: str, logger=logging):
    """
    Dump system information into system-info.json.

    :param output_dir:
    :param logger:
    :return:
    """
    outpath = join(output_dir, "system-info.json")
    info = distro.info(pretty=True, best=True)
    with open(outpath, "w") as f:
        json.dump(info, f, indent=4)

    logger.info(f"Saved system information to {outpath}.")

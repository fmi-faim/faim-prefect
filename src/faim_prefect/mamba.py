import os
import subprocess
from os.path import join

from prefect import task


@task(refresh_cache=True)
def log_infrastructure(run_dir: str):
    env = {}
    env.update(os.environ)

    mamba = f"{os.environ['MAMBA_ROOT_PREFIX']}/bin/micromamba"
    env_prefix = os.environ["CONDA_PREFIX"]
    cmd = f"{mamba} env export -p {env_prefix} > {join(run_dir, 'environment.yaml')}"
    result = subprocess.run(cmd, shell=True, check=True, env=env)
    result.check_returncode()

    cmd = (
        f"{mamba} run -p {env_prefix} pip list --format=freeze >"
        f" {join(run_dir, 'requirements.txt')}"
    )
    result = subprocess.run(cmd, shell=True, check=True)
    result.check_returncode()

    cmd = f"hostnamectl > {run_dir}/host.txt"
    result = subprocess.run(cmd, shell=True, check=True)
    result.check_returncode()

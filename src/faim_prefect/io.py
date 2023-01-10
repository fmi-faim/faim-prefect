import os
from os.path import join


def create_output_dir(root_dir: str, group: str, user: str, flow_name: str):
    """
    Create output directory in `save_data_path` with sub-path
    `group/user/flow_name/`.

    :param root_dir:
    :param group:
    :param user:
    :param flow_name:
    :return: root_dir/group/user/flow_name
    """
    output_dir = join(root_dir, group, user, flow_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

import logging
import shutil
import tempfile
from os.path import exists, join
from unittest import TestCase

from faim_prefect.env import save_conda_env


class TestEnv(TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    def test_save_conda_env(self):
        save_conda_env.fn(self.dir, logger=logging.getLogger("test"))

        assert exists(join(self.dir, "conda-environment.yaml"))

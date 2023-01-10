import logging
import shutil
import tempfile
from os.path import exists, join
from unittest import TestCase

from faim_prefect.system import save_system_information


class TestSystem(TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    def test_save_system_information(self):
        save_system_information.fn(self.dir, logger=logging.getLogger("test"))

        assert exists(join(self.dir, "system-info.json"))

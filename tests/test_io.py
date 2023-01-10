import shutil
import tempfile
from os.path import exists, join
from unittest import TestCase

from faim_prefect.io import create_output_dir


class TestIO(TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    def test_create_ouput_dir(self):
        group = "group"
        user = "user"
        flow_name = "flow_name"

        create_output_dir(self.dir, group, user, flow_name)

        assert exists(join(self.dir, group, user, flow_name))

        # Test that everything works if group and user already exist.
        create_output_dir(self.dir, group, user, "flow_name_2")
        assert exists(join(self.dir, group, user, "flow_name_2"))

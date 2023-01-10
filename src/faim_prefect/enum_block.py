from enum import Enum
from typing import List

from prefect.blocks.core import Block


class GroupChoices(Block):
    choices: List[str]

    def get_choices(self):
        return Enum('GroupChoices', {x: x for x in self.choices})

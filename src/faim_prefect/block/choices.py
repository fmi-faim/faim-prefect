from enum import Enum
from typing import List

from prefect.blocks.core import Block


class Choices(Block):
    """A Prefect block representing a collection of options.

    To register this block, follow these instructions:
    https://docs.prefect.io/concepts/blocks/#registering-blocks-for-use-in-the-prefect-ui

    Usage example
    -------
    block = Choices.load('groups')

    @flow(name="Test Choice Parameters")
    def parameter_test_flow(group: block.get()):
        logger = get_run_logger()
        logger.info(group)
    """

    choices: List[str]
    docstring: str = 'Select one choice.'

    def get(self) -> Enum:
        """Get list of choices."""
        choices = Enum('Choices', {x: x for x in self.choices})
        choices.__doc__ = self.docstring
        return choices

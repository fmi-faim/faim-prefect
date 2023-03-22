from pydantic import BaseModel

from faim_prefect.block.choices import Choices

groups = Choices.load("fmi-groups")


class User(BaseModel):
    name: str
    group: groups.get()

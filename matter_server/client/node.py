"""Matter node."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .matter import Matter


class MatterNode:
    """Matter node."""

    def __init__(self, matter: Matter, node_info: dict) -> None:
        self.matter = matter
        self.raw_data = node_info

    @property
    def node_id(self) -> int:
        return self.raw_data["node_id"]

    @property
    def name(self) -> str:
        return self.basic_info["nodeLabel"]

    @property
    def unique_id(self) -> str:
        return self.basic_info["uniqueID"]

    @property
    def basic_info(self) -> dict:
        return self.raw_data["attributes"]["0"]["Basic"]

    def update_data(self, node_info):
        self.raw_data = node_info

    def __repr__(self):
        return f"<MatterNode {self.node_id}>"
from DATA.modules.base.upgrade import Upgrade


class UpgradeMap:
    """
    upgrades: list = [
        {
            "id": int
            "cost": [cost: int, type: str = "silver"],
            "dependencies": [id: int, ...],
            "image": str,
            "radius": int,

            "x": int,
            "y": int
        }
    ]

    """

    def __init__(self, game, upgrades):
        self.game = game

        self.upgrades = upgrades

        self.dependencies = []
        self.out = []

    def init(self):
        self.dependencies = []
        self.out = []

        for upgrade in self.upgrades:
            self.out.append(
                Upgrade(
                    self.game, upgrade
                )
            )

            for depend in upgrade["dependencies"]:
                self.dependencies.append(depend)

    def draw(self):
        for upgrade in self.out:
            upgrade.draw()

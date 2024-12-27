from model import Creature

_creatures: list[Creature] = [
    Creature(name="yeti",
            country="CN",
            area="Himalayas",
            description="Hirsute Himalayan",
            aka="Abnominable Snowman"
            ),
    Creature(name="sasquatch",
            country="US",
            area="*",
            description="Yeti's Cousing Eddie",
            aka="Bigfoot"
            )
]

def get_creature() -> list[Creature]:
    return _creatures
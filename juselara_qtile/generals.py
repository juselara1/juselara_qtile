from libqtile.config import Group
from libqtile import layout
from juselara_qtile.dataclasses import Keys, PathsConfig
from typing import List, Dict

def load_groups(keys: Keys) -> List[Group]:
    items = keys.keygroups.dict().items()
    group_vals = map(lambda x: x[1], items)
    valid_groups = filter(lambda x: x is not None, group_vals)
    group_names = map(lambda x: x[-1], valid_groups)
    return list(map(lambda x: Group(x), group_names))

def load_layouts(config: PathsConfig) -> List:
    return [
            layout.Columns(
                margin=config.spacing.margin,
                border_width=config.spacing.border_width,
                border_focus=config.colors.color0,
                border_normal=config.colors.color2
                )
            ]

def load_extension_defs(config: PathsConfig) -> Dict:
    return {
            "font": config.font.font,
            "fontsize": config.font.fontsize
            }

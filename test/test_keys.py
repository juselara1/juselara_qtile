from yacmmal import autoconfig, BaseModel
from libqtile.config import Key
from juselara_qtile.keys import KeyManager, GroupManager
from juselara_qtile.dataclasses import PathsConfig
from juselara_qtile.generals import load_groups

class Config(BaseModel):
    paths: PathsConfig

@autoconfig(
        base_path="test/",
        config=[( "conf", "paths", PathsConfig)],
        format="toml"
        )
def test_keys(cfg):
    keymanager = KeyManager(cfg.paths.keys)
    keys1 = keymanager()
    assert(isinstance(keys1, list))
    for key in keys1:
        assert(isinstance(key, Key))

@autoconfig(
        base_path="test/",
        config=[( "conf", "paths", PathsConfig)],
        format="toml"
        )
def test_groups(cfg):
    groups = load_groups(cfg.paths.keys)
    groupmanager = GroupManager(cfg.paths.keys, groups)
    keys2 = groupmanager()
    assert(isinstance(keys2, list))
    for key in keys2:
        assert(isinstance(key, Key))

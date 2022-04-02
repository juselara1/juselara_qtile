from juselara_qtile.dataclasses import PathsConfig
from yacmmal import autoconfig, BaseModel
from juselara_qtile.keys import KeyManager
from libqtile.config import Key

class Config(BaseModel):
    paths: PathsConfig

@autoconfig(
        base_path="test/",
        config=[( "conf", "paths", PathsConfig)],
        format="toml"
        )
def test_keys(cfg):
    manager = KeyManager(cfg.paths.keys)
    res = manager()
    assert(isinstance(res, list))
    assert(isinstance(res[0], Key))

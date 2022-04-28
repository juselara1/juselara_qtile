from juselara_qtile.dataclasses import PathsConfig
from yacmmal import autoconfig, BaseModel

class Config(BaseModel):
    paths: PathsConfig

@autoconfig(
        base_path="test/",
        config=[( "conf", "paths", PathsConfig)],
        format="toml"
        )
def test_config(cfg):
    assert isinstance(cfg.paths, PathsConfig)

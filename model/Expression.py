from dataclasses import dataclass

# Classes
#region asset_info
@dataclass
class AssetInfoContributor:
  author: str
  email: str
  website: str

@dataclass
class AssetInfo:
  id: str
  type: str
  revision: str
  modified: str
  contributor: AssetInfoContributor
#endregion

#region scene
@dataclass
class Animations:
  url: str
  keys: str

@dataclass
class Scene:
  animations: Animations
#endregion

@dataclass
class Expression:
  fileVersion: str
  assetInfo: AssetInfo
  scene: Scene

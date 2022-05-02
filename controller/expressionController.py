import json
import sys

sys.path.append("..") # Adds higher directory to python modules path.
from model.Expression import Expression, AssetInfo, AssetInfoContributor, Scene, Animations

def encoder(expression):
  if not isinstance(expression, Expression):
    raise TypeError(f'Object {expression} is not of type Expression.')

  return { 
    'file_version': expression.fileVersion, 
    'asset_info': {
      'id': expression.assetInfo.id,
      'type': expression.assetInfo.type,
      'revision': expression.assetInfo.revision,
      'modified': expression.assetInfo.modified,
      'contributor': {
        'author': expression.assetInfo.contributor.author,
        'email': expression.assetInfo.contributor.email,
        'website': expression.assetInfo.contributor.website,
      },
    }
  }

def load(data):
  assetInfo = data['asset_info']
  assetInfoContributor = assetInfo['contributor']
  scene = data['scene']
  modifiers = scene['modifiers']

  arrAnimations = []
  for modifier in modifiers:
    arrAnimations.append(modifier)

  print(arrAnimations)

  expressionObject = Expression(
    fileVersion=data['file_version'], 
    assetInfo=AssetInfo(
      id=assetInfo['id'], 
      type=assetInfo['type'], 
      revision=assetInfo['revision'], 
      modified=assetInfo['modified'], 
      contributor=AssetInfoContributor(
        author=assetInfoContributor['author'], 
        email=assetInfoContributor['email'], 
        website=assetInfoContributor['website']
      )
    ),
    scene=Animations(
      url='123',
      keys='ddd'
    )
  )

  return expressionObject



def test():
  expression = Expression(
    fileVersion='0.0.0.6.0', 
    assetInfo=AssetInfo(
      id='123', 
      type='algo', 
      revision='', 
      modified='', 
      contributor=AssetInfoContributor(author='someone', email='', website='')
    )
  )

  print(expression)

  jsonified = json.dumps(expression, default=encoder, indent=2)

  print(jsonified)


# test()
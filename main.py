import json
from controller.expressionController import load, encoder

def Main():
  with open('test/scenes/scene.json', 'r', encoding='utf-8') as sceneFile:
    dataScene = json.load(sceneFile)

    expression = load(dataScene)

    print(expression)

  #with open(expression.nome + '.json', 'w', encoding='UTF-8') as fa:
  #  json.dump(expression, fa, default=encoder_person, indent=2)

Main()
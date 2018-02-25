import yaml


class Recipe:
    ""

    def __init__(
        self,
        ):
        self.recipe = self.load_recipe(pathRecipe='')

    def load_recipe(self, pathRecipe):
        with open('C:\\Users\\Usuari\\github\\nyam_text\\config\\recipes.yaml', 'r') as f:
            data = yaml.load(f)
        return data['recipe']

    def print_recipe(self,):
        print(self.recipe)


if __name__ == '__main__':
    recip = Recipe()
    recip.print_recipe()

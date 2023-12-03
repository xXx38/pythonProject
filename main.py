# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""

nom1 = "jean"
age1 = 30

def afficher_informations_personne(nom : str, age:int):
    print(f"La personne s'appelle {nom}, son age est {age} ans")

afficher_informations_personne(nom1,age1)

"""


class Personne:
    """
    Classe Personne, crée par XLE

    """

    def __init__(self, nom: str, age: int):
        """
        constructeur tartapion
        blablabla
        :param nom:         nom de la personne
        :param age:        age de la personne
        """
        self.nom = nom
        print("constructeur personne " + nom)

    def SePresenter(self):
        print(f"je m'apelle {self.nom}")


personne1 = Personne("Jean",30)
personne1.SePresenter()
# personne2 = Personne()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

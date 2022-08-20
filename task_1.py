import requests
from pprint import pprint


class SuperHeroAPIService:

    _BASE_URL = 'https://akabab.github.io/superhero-api/api'
    _ALL_HEROES = '/all.json'

    def get_all_heroes(self) -> list:
        url = self._BASE_URL + self._ALL_HEROES
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_heroes_by_names(self, names: list) -> list:
        all_heroes = self.get_all_heroes()
        heroes = [hero for hero in all_heroes if hero.get('name', '') in names]
        return heroes

    def get_best_hero_by_powerstat(self, powerstat: str, heroes: list) -> dict:
        best_hero = max(heroes, key=lambda hero: hero['powerstats'][powerstat])
        return best_hero


if __name__ == '__main__':

    heroes_names = ['Hulk', 'Captain America', 'Thanos']
    powerstat = 'intelligence'

    superhero_service = SuperHeroAPIService()
    heroes = superhero_service.get_heroes_by_names(heroes_names)
    best_hero = superhero_service.get_best_hero_by_powerstat(powerstat, heroes)
    print(f'Лучший герой из: {", ".join(heroes_names)} '
          f'по параметру {powerstat} - это {best_hero["name"]}.')
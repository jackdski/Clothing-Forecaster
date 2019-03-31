from src.info import Info
from src.gui import gui
from src.weather import weather

import threading

# ID for Boulder: 5574999
# ID for San Diego County: 5391832
# ID for Poway: 5384690


def get_id(city):
    return {
        'Boulder': 5574999,
        'San Diego': 5391832,
        'Poway': 5384690,
    }.get(city)


if __name__ == "__main__":
    info = Info()

    zipcode_id = get_id('Boulder')

    w = threading.Thread(target=weather, args=(info,))
    g = threading.Thread(target=gui, args=(info,))

    w.start()
    w.join()
    g.start()
    g.join()

    print("Done!")


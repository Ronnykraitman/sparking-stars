import signal

from NeoWs.neo_data import get_neo_feed, get_dangerous_asteroids, get_closest_asteroid, get_fastest_asteroid
from general_utils import goodbye, show_menu


def signal_handler(signal, frame):
    goodbye()


def welcome():
    print("\nHello, welcome to NEO - your guide in the sky")
    print("First thing first, lets fetch NASA data for you, shall we?\n")
    return get_neo_feed()


def start(feed_by_dates):
    try:
        neo_feed_options: list = [
            ("Get the most dangerous asteroids", get_dangerous_asteroids),
            ("Get the closest asteroid to earth at that time", get_closest_asteroid),
            ("Get the fastest asteroid", get_fastest_asteroid),
            ("Start over with some new dates", neows),
            ("Main Menu", ()),
            ("Exit", goodbye)]
        # ("Get asteroids by a custom filter", "soon"),
        while True:
            selection = show_menu(neo_feed_options, "Neo feed options:")
            neo_feed_options[selection][1](feed_by_dates)

    except Exception as e:
        print(f"Oh No! Something went wrong: {e}")


def neows(msg: str = "\nLet's get you some data form Nasa\n"):
    print(msg)
    feed_by_dates = get_neo_feed()
    start(feed_by_dates)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    first_time_txt: str = ("\nHello, welcome to NEO - your guide in the sky."
                           "First thing first, lets fetch NASA data for you, shall we?\n")
    neows(first_time_txt)

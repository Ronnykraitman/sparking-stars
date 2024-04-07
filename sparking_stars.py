from NeoWs.neo_start import neows
import logging

logging.getLogger("py4j").setLevel(logging.ERROR)
logging.getLogger("pyspark").setLevel(logging.ERROR)


def sparking_stars():
    print("Welcome to sparking_stars")


if __name__ == "__main__":
    first_time_neo_txt: str = ("\nHello, welcome to NEO - your guide in the sky.\n"
                               "First thing first, lets fetch NASA data for you, shall we?\n")
    neows(first_time_neo_txt)

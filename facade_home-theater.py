# Компоненты домашнего кинотеатра
class Amplifier:
    def on(self):
        print("Top-O-Line Amplifier on")

    def off(self):
        print("Top-O-Line Amplifier off")

    def set_dvd(self, dvd):
        print(f"Top-O-Line Amplifier setting DVD player to {dvd}")

    def set_surround_sound(self):
        print("Top-O-Line Amplifier surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, level):
        print(f"Top-O-Line Amplifier setting volume to {level}")


class Tuner:
    def on(self):
        print("Tuner on")

    def tune(self, frequency):
        print(f"Tuner tuning to {frequency}MHz")

    def off(self):
        print("Tuner off")


class DvdPlayer:
    def on(self):
        print("Top-O-Line DVD Player on")

    def off(self):
        print("Top-O-Line DVD Player off")

    def play(self, movie):
        print(f"Top-O-Line DVD Player playing \"{movie}\"")

    def stop(self):
        print("Top-O-Line DVD Player stopped")

    def eject(self):
        print("Top-O-Line DVD Player eject")


class CdPlayer:
    def on(self):
        print("CD Player on")

    def play(self, music):
        print(f"CD Player playing \"{music}\"")

    def off(self):
        print("CD Player off")


class Projector:
    def on(self):
        print("Top-O-Line Projector on")

    def off(self):
        print("Top-O-Line Projector off")

    def widescreen_mode(self):
        print(f"Top-O-Line Projector in widescreen mode (16x9 aspect ratio)")

    def normal_mode(self):
        print(f"Top-O-Line Projector in normal mode (standard 4x3 aspect ratio)")


class TheaterLights:
    def dim(self, level):
        print(f"Theater Ceiling Lights dimming to {level}%")

    def on(self):
        print("Theater Ceiling Lights on")


class Screen:
    def down(self):
        print("Theater Screen going down")

    def up(self):
        print("Theater Screen going up")


class PopcornPopper:
    def on(self):
        print("Popcorn Popper on")

    def off(self):
        print("Popcorn Popper off")

    def pop(self):
        print("Popcorn Popper popping popcorn!")


# Фасад для управления домашним кинотеатром
class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.widescreen_mode()
        self.amp.on()
        self.amp.set_dvd("Top-O-Line DVD Player")
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

# Тестирование фасада
if __name__ == "__main__":
    # Создаем компоненты
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

    home_theater.watch_movie("Raiders of the Lost Ark")

    home_theater.end_movie()

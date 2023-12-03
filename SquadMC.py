class Interpolator:
    def __init__(self, data):
        self.data = data

    def interpolate_angle(self, range_value):
        for i in range(len(self.data) - 1):
            if (self.data[i][0] >= range_value >= self.data[i + 1][0]) or (
                self.data[i][0] <= range_value <= self.data[i + 1][0]
            ):
                slope = (self.data[i + 1][1] - self.data[i][1]) / (
                    self.data[i + 1][0] - self.data[i][0]
                )
                return self.data[i][1] + slope * (range_value - self.data[i][0])
        return "N/A"

    @staticmethod
    def format_angle(angle):
        return angle if isinstance(angle, str) else format(angle, ".2f")


class Mortar(Interpolator):
    def __init__(self):
        super().__init__(
            [
                (50, 1579),
                (100, 1558),
                (150, 1538),
                (200, 1517),
                (250, 1496),
                (300, 1475),
                (350, 1453),
                (400, 1431),
                (450, 1409),
                (500, 1387),
                (550, 1364),
                (600, 1341),
                (650, 1317),
                (700, 1292),
                (750, 1267),
                (800, 1240),
                (850, 1212),
                (900, 1183),
                (950, 1152),
                (1000, 1118),
                (1050, 1081),
                (1100, 1039),
                (1150, 988),
                (1200, 918),
                (1250, 800),
            ]
        )


class Tank(Interpolator):
    def __init__(self):
        super().__init__(
            [
                (925, 45),
                (900, 50),
                (875, 55),
                (800, 60),
                (700, 65),
                (600, 70),
                (500, 73.5),
                (400, 77),
                (300, 80.5),
                (200, 83.5),
                (150, 85),
                (0, 90),
            ]
        )


class Rocket(Interpolator):
    def __init__(self):
        super().__init__(
            [
                (50, 0),
                (250, 2.5),
                (500, 5),
                (700, 7.5),
                (800, 8.8),
                (900, 10),
                (1000, 12),
                (1100, 13.5),
                (1200, 15.5),
                (1300, 16.3),
                (1400, 18),
                (1500, 20),
                (1600, 22.5),
                (1700, 25),
                (1800, 27.5),
                (1900, 29.8),
                (2000, 32),
            ]
        )


def main(distance):
    mortar = Mortar()
    tank = Tank()
    rocket = Rocket()

    mortar_angle = mortar.format_angle(mortar.interpolate_angle(distance))
    tank_angle = tank.format_angle(tank.interpolate_angle(distance))
    rocket_angle = rocket.format_angle(rocket.interpolate_angle(distance))

    print(f"mortar:{mortar_angle}, tank:{tank_angle}, rocket:{rocket_angle}")


if __name__ == "__main__":
    distance = float(input("des："))
    main(distance)

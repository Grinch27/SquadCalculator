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


def format_angle(angle):
    return angle if isinstance(angle, str) else format(angle, ".2f")


def main():
    distance = float(input("des："))

    data_mortar = [
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
    data_tank = [
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
    data_rocket = [
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

    interpolator_mortar = Interpolator(data_mortar)
    interpolator_tank = Interpolator(data_tank)
    interpolator_rocket = Interpolator(data_rocket)

    mortar_angle = interpolator_mortar.interpolate_angle(distance)
    tank_angle = interpolator_tank.interpolate_angle(distance)
    rocket_angle = interpolator_rocket.interpolate_angle(distance)

    mortar_angle_str = format_angle(mortar_angle)
    tank_angle_str = format_angle(tank_angle)
    rocket_angle_str = format_angle(rocket_angle)

    print(
        f"mortar:{mortar_angle_str}, tank:{tank_angle_str}, rocket:{rocket_angle_str}"
    )


if __name__ == "__main__":
    main()

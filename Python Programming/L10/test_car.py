import unittest

from car import Car, Wheel, BattleCar

class CarTest(unittest.TestCase):
    def setUp(self):
        print("Setting up")
        diameter = 36
        resistance = 0.5
        num_of_wheels = 4
        self.wheels = [Wheel(diameter, resistance) for i in range(num_of_wheels)]
        self.car = Car("Honda Civic", 2015, False, self.wheels)

    def tearDown(self):
        print("Tearing down")

    def test_accelerate(self):
        print("Test accelerate")
        self.car.accelerate()
        self.assertEqual(self.car.speed, 0)
        self.car.accelerate(10)
        self.assertEqual(self.car.speed, 9)

    def test_decelerate(self):
        print("Test decelerate")
        self.car.accelerate(10)
        self.assertEqual(self.car.speed, 9)
        self.car.decelerate(4) 
        self.assertEqual(self.car.speed, 6)



class BattleCarTest(unittest.TestCase):
    def setUp(self):
        diameter = 38
        resistance = 0.5
        num_of_wheels = 4
        wheels = [Wheel(diameter, resistance) for i in range(num_of_wheels)]

        self.battle_car = BattleCar("The Terminator", 2020, True, wheels,
                               strength=5)

        self.opponent_car = Car("Honda Civic", 2015, True, wheels)

    def test_battlecar_attack(self):
        self.opponent_car.accelerate(50)
        self.assertEqual(self.opponent_car.speed, 49)

        self.battle_car.accelerate(40)
        self.assertEqual(self.battle_car.speed, 39)

        self.battle_car.attack(self.opponent_car)
        self.assertEqual(self.opponent_car.speed, 45)

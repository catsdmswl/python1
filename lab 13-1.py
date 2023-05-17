class Car:
	def __init__(self, speed, color):
		self.speed = speed
		self.color = color

	def drive(self):
		self.speed = 60
		print(str(self.color), str(self.speed), "km, 주행중입니다.")

	def stop(self):
		self.speed = 0
		print(str(self.color), "정지했습니다.")
#객체를 생성한다
car1 = Car(0, 'white')
car2 = Car(0, 'green')
car3 = Car(0, 'yellow')
#객체의 메소드를 호출한다.
car1.drive()
car1.stop()
car2.drive()
car2.stop()
car3.drive()
car3.stop()
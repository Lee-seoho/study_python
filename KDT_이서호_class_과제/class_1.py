# 차
# 브랜드, 모델, 연비, 주유(리터)

# 현재 기름으로 이동 가능한 거리 구하기
# 주유 하였을 때는 합산된 기름으로 이동 가능한 거리 구하기

class Car:

    def __init__(self, brand, model, liter, km_per_liter, refuel_liter = 0):
        self.brand = brand
        self. model = model
        self.liter = liter
        self.km_per_liter = km_per_liter
        self.refuel_liter = refuel_liter

    def fuel_efficiency(self):
        mileage = (self.liter + self.refuel_liter) * self.km_per_liter
        return mileage


car1 = Car('hyundai', 'avante', 10, 9, 5)
car2 = Car('kia', 'k8', 15, 12)

print(f"{car1.model}의 주행 가능한 거리는 {car1.fuel_efficiency()}km입니다.")
print(f"{car2.model}의 주행 가능한 거리는 {car2.fuel_efficiency()}km입니다.")




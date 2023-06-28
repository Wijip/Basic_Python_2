class Dog:
    def __init__(self,breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def detail(self):
        print(f'keturunan : {self.breed}')
        print(f'ukuran : {self.size}')
        print(f'usia : {self.age}')
        print(f'Warna : {self.color}')

    def Eat(self):
        print("Anjing makan")

    def sleep(self):
        print("Anjing Tidur")

    def sit(self):
        print("Anjing Duduk")

    def run(self):
        print("Anjing Lari")

hitam = Dog("Neapolitan Mastiff", "Large", "5 Year", "Black")
putih = Dog("Matese", "Small", "2 Year", "White")
coklat = Dog("Chow Chow", "Midium", "3 Years", "Brown")

hitam.detail()
putih.detail()
coklat.detail()


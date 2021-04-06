from class_test.Point import Point

class ColorPoint(Point):
    def __init__(self, color, x, y):
        super().__init__(x, y)
        self.color = color

    def draw(self): #부모 함수 오버라이딩
        print(f'color = {self.color}, x = {self.x}, y = {self.y} 에 점을 그렸습니다')
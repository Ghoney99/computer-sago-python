# User-defined module TurtleDrawings_classPolygon
import turtle
import math


class Shape:
    def __init__(self, color, shape_name, cx, cy):
        self.color = color  #색상
        self.shape_name = shape_name    #다각형 이름
        self.cx = cx    #중심좌표
        self.cy = cy
    
    #꼭짓점 갯수 - 다각형이름 딕셔너리
    shape_types = {0: "circle", 3: "triangle", 4: "square", 5: "pentagon",
                   6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
    
    #다각형이름 - 꼭짓점 갯수 딕셔너리
    num_vert = {"circle": 0, "triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6,
                "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10}


class Polygon(Shape):
    def __init__(self, color, shape_name, cx, cy, radius):  #super로 상속받음
        super().__init__(color, shape_name, cx, cy)
        self.radius = radius

    def __str__(self):  #좌표 출력
        return f"{super().__str__()}, Radius: {self.radius:.2f}"
    
    def turtle_draw(self, t):
        t.speed(0)

        n_vertex = Polygon.num_vert[self.shape_name] #다각형의 꼭지점개수
        if n_vertex!=0: #다격형일때만 계산
            angle = 2 * math.pi / n_vertex  #각도
            theta_rad = (math.pi - angle) / 2
            h = self.radius * math.sin(theta_rad)
            side_length = self.radius * math.cos(theta_rad) * 2
            sx = self.cx - side_length / 2  ##coordinates of start position
            sy = self.cy - h    #coordinates of start position

        #좌표를 나타낼 색상은 검정색으로 지정, 굵기는 1로 지정
        t.color("black")
        t.pensize(1)

        #외접원을 그림
        t.penup()
        t.goto(self.cx, self.cy-self.radius)    #반지름을 빼주므로써 높이 맞춤
        t.pendown()
        t.circle(self.radius)

        #중심좌표 (cx, cy) 위치에 설정하고, 푸른색 점을 찍음
        t.penup()
        t.goto(self.cx, self.cy)
        t.pendown()
        t.dot(10, "blue")
        t.write(f"({self.cx:.2f}, {self.cy:.2f})")

        #원일때와 다격형일때 조건문 설정
        if n_vertex!=0: #다각형일때
            #(sx, sy) 위치에 설정하고, 푸른색 점을 찍음
            t.penup()
            t.goto(sx, sy)
            t.pendown()
            t.dot(10, "red")
            t.write(f"({sx:.2f}, {sy:.2f})")

        else:   #원일때
            t.penup()
            t.goto(self.cx, self.cy-self.radius)
            t.pendown()
            t.dot(10, "red")
            t.write(f"({self.cx:.2f}, {(self.cy-self.radius):.2f})")

        #다각형을 그릴 색상 지정, 굵기는 2로 지정
        t.color(self.color)
        t.pensize(2)

        if n_vertex!=0:
        #다각형을 그림 왼쪽으로 돌면서 다각형의 각도만큼 움직임
            for i in range(n_vertex):
                t.forward(side_length)
                t.left(360/n_vertex)
        else:
            t.penup()
            t.goto(self.cx, self.cy-self.radius)
            t.pendown()
            t.circle(self.radius)
        

def fget_drawings(fin):
    L_drawings = []
    for line in fin:
        drawing_info = line.strip().split()
        color, shape_name, cx, cy, radius = drawing_info
        cx, cy, radius = float(cx), float(cy), float(radius)
        polygon = Polygon(color, shape_name, cx, cy, radius)
        L_drawings.append(polygon)
    return L_drawings
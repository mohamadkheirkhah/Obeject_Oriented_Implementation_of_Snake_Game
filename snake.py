from turtle import Turtle


class Snake:
    MOVING_DISTANCE = 15
    SNAKE_LENGTH = 5

    def __init__(self):
        self.last_snake_segment_position = {
            'x': 0,
            'y': 0
        }
        self.list_of_snake_segments = []
        self.snake_length = self.SNAKE_LENGTH
        self.previous_location = (0, 0)
        self.my_current_location = (0, 0)
        self.create_a_snake()
        self.snake_head = self.list_of_snake_segments[0]

    def create_a_snake(self):
        for _ in range(self.snake_length):
            self.add_segment()

    def add_segment(self):
        new_snake_body = Turtle(shape='square')
        new_snake_body.color('white')
        # new_snake_body.shapesize(0.5)
        new_snake_body.penup()
        new_snake_body.setpos(self.last_snake_segment_position['x'], self.last_snake_segment_position['y'])
        new_snake_body.location = new_snake_body.pos()
        self.last_snake_segment_position['x'] -= 10
        self.list_of_snake_segments.append(new_snake_body)

    def extend_a_segment(self):
        self.snake_length += 1
        self.add_segment()
        # print(self.snake_head)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move(self):
        for index, segment in enumerate(self.list_of_snake_segments):
            if index == 0:
                self.previous_location = segment.pos()
                segment.forward(self.MOVING_DISTANCE)
                self.my_current_location = segment.pos()
            else:
                self.my_current_location = segment.pos()
                segment.setpos(self.previous_location)
                self.previous_location = self.my_current_location

"""
작성자: 윤완
작성일: 2026-10-03
문제: 9번 - 터틀 그래픽에서 각각의 거북이는 객체이다.
      2개의 거북이를 생성하여 서로 다른 방향으로 움직이도록 하자.
"""
import turtle


def test_prob9():
    a = turtle.Turtle()
    a.shape("circle")
    a.setheading(180)

    b = turtle.Turtle()
    b.shape("turtle")

    a.forward(165)
    a.right(90)
    a.forward(30)
    a.left(90)
    a.forward(145)

    b.forward(165)
    b.right(90)
    b.forward(30)
    b.left(90)
    b.forward(145)

    turtle.exitonclick()


if __name__ == "__main__":
    test_prob9()
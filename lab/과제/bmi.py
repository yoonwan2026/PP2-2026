import turtle

def draw_text(clean_data):
    headers = ["전화번호", "이름", "키(cm)", "몸무게(kg)", "bmi", "소견"]
    

    t = turtle.Turtle()
    t.hideturtle()  
    t.penup()      


    start_x = -350
    start_y = 200
    col_width = 120 
    row_height = 35  

    for col_idx, header in enumerate(headers):
        x = start_x + (col_idx * col_width)
        t.goto(x, start_y)
        t.write(header, align="center", font=("맑은 고딕", 11, "bold"))

    for row_idx, row in enumerate(clean_data):
        y = start_y - ((row_idx + 1) * row_height)  
        
        for col_idx, item in enumerate(row):
            x = start_x + (col_idx * col_width)
            t.goto(x, y)
            t.write(str(item), align="center", font=("맑은 고딕", 10, "normal"))

    turtle.done()
    #draw_text
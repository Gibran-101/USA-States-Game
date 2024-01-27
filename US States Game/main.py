import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

counter = 0
to_continue = True
reader = pandas.read_csv("50_states.csv")
actual_answer_list = reader["state"].to_list()
while to_continue:
    scoreboard = f"{counter}/ 50"
    user_answer = screen.textinput(title=scoreboard, prompt="What is the name of another state?").title()
    if user_answer == "Exit":
        new_file = pandas.DataFrame(actual_answer_list)
        new_file.to_csv("missed_states.csv")
        break
    if user_answer in actual_answer_list:
        counter += 1
        actual_answer_list.remove(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = reader[reader.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    elif user_answer not in actual_answer_list:
        pass
    if counter == 50:
        to_continue = False
#        pandas item() method grabs and returns the first element/ item in a row

turtle.mainloop()


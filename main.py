from turtle import Turtle, Screen
import pandas

# Setting up the screen
screen = Screen()
screen.tracer(0)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
states_map = Turtle()
states_map.shape(image)

exit_code = Turtle()
exit_code.hideturtle()
exit_code.penup()
exit_code.goto(0, -280)
exit_code.write('After making all your guesses, to generate a .csv file containing any U.S. states '
                'you\'ve missed, type: "Exit"', align="center", font=('Arial', 10, 'normal'))

# Running the game...
guessed_states = []

while len(guessed_states) < 50:
	screen.update()
	# User guesses a state
	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
									prompt="Can you name another state?").title()

	data = pandas.read_csv("50_states.csv")
	all_states = data.state.to_list()

	# Create break sequence to end the game
	if answer_state == "Exit":
		break

	# Check if the guess is among the 50 states
	if answer_state in all_states and answer_state not in guessed_states:
		# Add to list of guessed states to increase score
		guessed_states.append(answer_state)

		# Write the correct guesses on the map
		x = int(data[data.state == answer_state].x)
		y = int(data[data.state == answer_state].y)
		state = Turtle()
		state.hideturtle()
		state.penup()
		state.goto(x, y)
		state.write(answer_state)

missing_states = []
for state in all_states:
	if state not in guessed_states:
		missing_states.append(state)

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")

#pg158 or 120.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

'''We set the variable active to True u so the program starts in an active
state. Doing so makes the while statement simpler because no comparison is
made in the while statement itself; the logic is taken care of in other parts of
the program. As long as the active variable remains True, the loop will continue running v.
In the if statement inside the while loop, we check the value of message
once the user enters their input. If the user enters 'quit' w, we set active
to False, and the while loop stops. If the user enters anything other than
'quit' x, we print their input as a message.'''


'''FLAG- For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result,
our overall while statement needs to check only one condition: whether or
not the flag is currently True. Then, all our other tests (to see if an event has
occurred that should set the flag to False) can be neatly organized in the rest
of the program.'''


'''This program has the same output as the previous example where we
placed the conditional test directly in the while statement. But now that we
have a flag to indicate whether the overall program is in an active state, it
would be easy to add more tests (such as elif statements) for events that
should cause active to become False. This is useful in complicated programs
like games in which there may be many events that should each make the
program stop running. When any of these events causes the active flag to
become False, the main game loop will exit, a Game Over message can be
displayed, and the player can be given the option to play again.'''

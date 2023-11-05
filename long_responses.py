import random

R_EATING = " I don't like eating anything because i'm a bot obviously!"
R_ADVISE = "Tf i were you, Twould go to thr internet an dtype exactly what you wrote there!"
def unknown():
    response = ['Could yoiu please re_ phrase that ?', 
                ". . .",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter + 1
    
# Define event handler functions
def tick():
    increment()
    print counter
    
def buttonpress():
    global counter
    counter = 0
    
def increase():
    global counter
    increment()
    print counter

def decrease():
    global counter
    counter = counter - 1


# Create a frame
frame = simplegui.create_frame("SimpleGUI Test", 300, 300)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
# add button to increase and reset counter
frame.add_button("Increase counter", increase)
frame.add_button("Reset counter", buttonpress)
frame.add_button("Decrease counter", decrease)

# Start frame and timers
frame.start()
timer.start()

import simplegui

message = "Hi Krystal!!!"

def click():
  global message
  message = "Hooray!!"
  
def draw(canvas):
  canvas.draw_text(message, [60, 150], 36, "Blue")
  
frame = simplegui.create_frame("My badass box", 300, 300)
frame.add_button("Don't you dare click!", click)
frame.set_draw_handler(draw)

frame.start()
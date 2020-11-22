import hal
from graphics.const import *
import uasyncio
from utils import clean_memory, create_repeat_task

print("Main Operation started")

hal.canvas.clear(WHITE)
hal.canvas.draw_line(0, 0, hal.canvas.width, hal.canvas.height-40, BLACK)
hal.canvas.draw_line(0, hal.canvas.height-40, hal.canvas.width, 0, BLACK)
hal.display.update_screen()
hal.display.clear(WHITE)

print("Startup Finished")


# setup async system
def main():
    uasyncio.create_task(create_repeat_task(clean_memory, 60000, True))
    uasyncio.get_event_loop().run_forever()


# Start main loop
main()

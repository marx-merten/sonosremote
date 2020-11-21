import time

from rotary_irq_esp import RotaryIRQ
import globals.pinout as pinout


r = RotaryIRQ(pin_num_clk=pinout.ROT_B,
              pin_num_dt=pinout.ROT_A,
              min_val=0,
              max_val=50,
              range_mode=RotaryIRQ.RANGE_WRAP,
              half_step=True,
              pull_up=True)


def readout():
    val_old = r.value()
    while True:
        val_new = r.value()

        if val_old != val_new:
            val_old = val_new
            print('result =', val_new)

        time.sleep_ms(50)


readout()

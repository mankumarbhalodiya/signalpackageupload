import numpy as np
from signal_ICT_mankumar_92400133125 import unitary_signals, trigonometric_signals, operations

# 1. Generate unit step and impulse
n = np.arange(-10, 10)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)

# 2. Generate sine wave
t = np.linspace(0, 1, 500)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)

# 3. Time shift sine wave
shifted_sine = operations.time_shift(sine, 50)  
# 4. Add step + ramp
ramp = unitary_signals.ramp_signal(n)
added = operations.signal_addition(step, ramp)

# 5. Multiply sine and cosine
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
product = operations.signal_multiplication(sine, cosine)

# 6. Time scale the sine wave (downsample by factor of 2)
scaled_sine = operations.time_scale(sine, 2)

# 7. Exponential signal
exp_signal = trigonometric_signals.exponential_signal(1, 2, t)  # A=1, a=2
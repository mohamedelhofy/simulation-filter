import numpy as np
import matplotlib.pyplot as plt

# Low-pass filter class
class LowPassFilter:
    def __init__(self, alpha):
        self.alpha = alpha
        self.prev_value = 0

    def filter(self, input_value):
        filtered_value = self.alpha * input_value + (1 - self.alpha) * self.prev_value
        self.prev_value = filtered_value
        return filtered_value

# Generate a noisy encoder signal
def generate_noisy_signal(frequency, noise_level, duration, sample_rate):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False) 
    clean_signal = np.sin(2 * np.pi * frequency * t) #  a clean signal
    noise = noise_level * np.random.normal(size=t.shape) # Add noise
    noisy_signal = clean_signal + noise
    return t, noisy_signal, clean_signal

# Parameters
encoder_frequency = 334  
noise_level = 0.5  
duration = 1.0  
sample_rate = 1000
cutoff_frequency = 500  

# Calculate alpha for the LPF
dt = 1 / sample_rate  
RC = 1 / (2 * np.pi * cutoff_frequency)
alpha = dt / (RC + dt)

# Generate the noisy signal
time, noisy_signal, clean_signal = generate_noisy_signal(encoder_frequency, noise_level, duration, sample_rate)

# Apply the low-pass filter
lpf = LowPassFilter(alpha=alpha)
filtered_signal = [lpf.filter(x) for x in noisy_signal]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(time, noisy_signal, label="Noisy Signal", color='red', alpha=0.6)
plt.plot(time, filtered_signal, label="Filtered Signal (LPF)", color='blue', linewidth=2)
plt.plot(time, clean_signal, label="Clean Signal", color='green', linestyle='--')
plt.title("Noisy Signal vs. Filtered Signal with Low-Pass Filter")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

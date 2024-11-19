
import numpy as np
import matplotlib
#matplotlib.use('Agg')  # Use 'Agg' backend for rendering without a display
import matplotlib.pyplot as plt

def show_plot(mean, std_dev):
    num_samples = 100
    measurement_error = np.random.normal(mean, std_dev, num_samples)
    process_data = np.full(num_samples, 10)
    exp_data =  process_data + measurement_error
    plt.hist(exp_data, bins=30)
    plt.title("Histogram of Experimental Data")
    plt.show()

show_plot(0,1)
show_plot(0,10)
show_plot(0,20)
show_plot(1,1)
show_plot(10,1)
show_plot(20,1)
show_plot(10,10)
show_plot(20,20)






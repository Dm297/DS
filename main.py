
import numpy as np
import matplotlib
#matplotlib.use('Agg')  # Use 'Agg' backend for rendering without a display
import matplotlib.pyplot as plt

def constant_process(size, value=10):
   return np.full(size, value)

# Initialize parameters
mean = 0
std_dev = 1
num_samples = 1000

#Нормальний розподіл
measurement_error = np.random.normal(mean, std_dev, num_samples)

#Закон зміни досліджуваного процесу – постійна
process_data = np.full(num_samples, 10)

#Адитивна модель
experimental_data = process_data + measurement_error

#Монте-Карло

results = []
for _ in range(num_samples):
   measurement_error = np.random.normal(mean, std_dev, num_samples)
   experimental_data = process_data + measurement_error
   results.append(np.mean(experimental_data))

# Результати Монте-Карло
monte_carlo_mean = np.mean(results)
monte_carlo_std_dev = np.std(results)

print("Монте-Карло: Середнє",monte_carlo_mean)
print("Монте-Карло: Відхилення",monte_carlo_std_dev)


# Дисперсія
variance = np.var(experimental_data)
print("Дисперсія: ", variance)
# середньоквадратичне квадратичне відхилення
std_dev = np.std(experimental_data)
print("середньоквадратичне квадратичне відхилення: ", std_dev)

# Відхилення мат. сподівання
mean = np.mean(experimental_data)
print("Відхилення мат. сподівання: ", mean)


#Gist
# Plotting histogram of the experimental data
plt.hist(experimental_data, bins=30)
plt.title("Histogram of Experimental Data")
plt.show()

plt.hist(measurement_error, bins=30, color='yellow')
plt.title("Histogram of Measurement Errors")
plt.show()





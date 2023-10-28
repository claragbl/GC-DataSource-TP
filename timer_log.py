import time
from collections import Counter
import timeit
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------------------
# Decorator to measure the execution time of a function
def timing_decorator(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{func.__name__} took {execution_time:.2f} seconds to execute.")
    #result_str = f"{func.__name__} took {execution_time:.2f} seconds to execute."
    return result
  return wrapper

# Function using a dictionary to count words
@timing_decorator
def word_count_dict(text):
  word_count = {}
  words = text.split()
  for word in words:
    word = word.lower() # Lowercase for case-insensitive word counting
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

# Function using Counter to count words
@timing_decorator
def word_count_counter(text):
  words = text.split()
  words = [word.lower() for word in words]  
  return Counter(words)

# ----------------------------------------------------------------------------------

if __name__ == "__main__":
  with open('shakespeare.txt', 'r') as file:
    text = file.read()

  nb_experiments = 100

  # lists to store execution time
  execution_times_dic = []
  execution_times_counter = []

  for i in range(nb_experiments):

    # execution time for counting words using a dictionary
    dic_time = timeit.timeit(
      lambda: word_count_dict(text),
          number=1
    )
    execution_times_dic.append(dic_time)

    # execution time for counting words using Counter
    counter_time = timeit.timeit(
      lambda: word_count_counter(text),
        number=1
    )
    execution_times_counter.append(counter_time)

  
  # mean and variance
  mean_dict = np.mean(execution_times_dic)
  var_dict = np.var(execution_times_dic)
  mean_counter = np.mean(execution_times_counter)
  var_counter = np.var(execution_times_counter)
  print(f"Mean (Dictionary): {mean_dict:.6f} seconds")
  print(f"Variance (Dictionary): {var_dict:.6f}")
  print(f"Mean (Counter): {mean_counter:.6f} seconds")
  print(f"Variance (Counter): {var_counter:.6f}")
    
  # Distribution plots
  plt.figure(figsize=(10, 5))
  plt.hist(execution_times_dic, bins=20, alpha=0.5, label='Dictionary function', color='g')
  plt.hist(execution_times_counter, bins=20, alpha=0.5, label='Counter function', color='b')
  plt.xlabel('execution time (s)')
  plt.ylabel('frequency')
  plt.legend()
  plt.title('Execution Time Distribution for Word Counting Functions')
  plt.show()

  

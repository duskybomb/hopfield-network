import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('Set2')


N = 400
P = 100
N_sqrt = np.sqrt(N).astype('int32')
NO_OF_ITERATIONS = 40
NO_OF_BITS_TO_CHANGE = 200

epsilon = np.asarray([np.random.choice([1, -1], size=N)])
for i in range(P-1):
    epsilon = np.append(epsilon, [np.random.choice([1, -1], size=N)], axis=0)

print(epsilon.shape)

random_pattern = np.random.randint(P)
test_array = epsilon[random_pattern]
random_pattern_test = np.random.choice([1, -1], size=NO_OF_BITS_TO_CHANGE)
test_array[:NO_OF_BITS_TO_CHANGE] = random_pattern_test

print(random_pattern)

w = np.zeros((N, N))
h = np.zeros(N)
for i in range(N):
    for j in range(N):
        for p in range(P):
            w[i, j] += (epsilon[p, i]*epsilon[p, j]).sum()
        if i==j:
            w[i, j] = 0
w /= N

hamming_distance = np.zeros((NO_OF_ITERATIONS, P))
for iteration in range(NO_OF_ITERATIONS):
    for _ in range(N):
        i = np.random.randint(N)
        h[i] = 0
        for j in range(N):
            h[i] += w[i, j]*test_array[j]
    test_array = np.where(h<0, -1, 1)

    for i in range(P):
        hamming_distance[iteration, i] = ((epsilon - test_array)[i]!=0).sum()

fig = plt.figure(figsize = (8, 8))
plt.plot(hamming_distance)
plt.xlabel('No of Iterations')
plt.ylabel('Hamming Distance')
plt.ylim([0, N])
plt.show()
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# compare with the original
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

# test with range that doesn't start with 0
for elem in ft_tqdm(range(50, 100)):
    sleep(0.005)
print()
for elem in tqdm(range(50, 100)):
    sleep(0.005)
print()

# test with range that has a step larger than 1
for elem in ft_tqdm(range(50, 100, 2)):
    sleep(0.005)
print()
for elem in tqdm(range(50, 100, 2)):
    sleep(0.005)
print()

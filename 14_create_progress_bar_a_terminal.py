# To create a progress bar in your terminal script we need tqdm
# first install tqdm using
# >> pip install tqdm

import time

for i in tqdm(range(10)):
    time.sleep(1)

# Running this script should show a progress bar that runs for
# 10 seconds before exit.

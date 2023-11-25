from Simulator.main import run_iter
import time

# Will except if file already exists. So will just append onto file
try:
    myFile = open("results.csv", 'x')
    myFile.write("Turn,Time,Hand\n")
except:
    myFile = open("results.csv", 'a')

# Findout how many iterations must be completed
i = input("Number of trials: ")

for _ in range(int(i)):
    print("Starting trial...")
    initial_time = time.time()
    ans = run_iter()
    final_time = time.time()

    myFile.write(str(ans[0]) + "," + str(final_time-initial_time) + "," + str(ans[1])+"\n")

myFile.close()
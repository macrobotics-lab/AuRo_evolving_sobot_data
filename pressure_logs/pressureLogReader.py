import numpy as np
import csv
import matplotlib.pyplot as plt
pressurelog=[]
with open("logs-red-nRNDs18-table-RECALIB_MATT_trial0_kd_0.85.csv", newline='') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    for row in csv:
        pressurelog.append(row)


time2 = pressurelog[0]
time1 = np.array(time2)
time = np.ndarray.flatten(time1).astype(np.float)
time = time/1000

A = np.array(pressurelog[1]).astype(np.float)
B = np.array(pressurelog[2]).astype(np.float)
C = np.array(pressurelog[3]).astype(np.float)
hw = pressurelog[4]
regulatorA=[]
regulatorB=[]
regulatorC=[]
sensedA = []
sensedB = []
sensedC = []
for sec in hw:
   regulatorA.append(eval(sec)["regulator"][2])
   regulatorB.append(eval(sec)["regulator"][1])
   regulatorC.append(eval(sec)["regulator"][0])
   sensedA.append(eval(sec)["honeywell"][0])
   sensedB.append(eval(sec)["honeywell"][1])
   sensedC.append(eval(sec)["honeywell"][2])

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Honeywell sensed(r), regulator(b), commanded(g)')
ax1.plot(time, regulatorA,'b')
ax1.plot(time, sensedA,'r')
ax1.plot(time, A,'g')
ax1.grid()

ax2.plot(time, regulatorB,'b')
ax2.plot(time, sensedB,'r')
ax2.plot(time, B,'g')

ax3.plot(time, regulatorC,'b')
ax3.plot(time, sensedC,'r')
ax3.plot(time, C,'g')

# plt.plot(time,regulatorA)
# plt.plot(time,regulatorB)
# plt.plot(time,regulatorC)
# plt.plot(time,sensedA)
plt.show()

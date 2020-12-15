from pylab import *
import re 
# plot([1,2,3])
# show()

#l1d_size
data = []
size = []
hits = []
numCycles = []
writebacks = np.zeros(10)

for i in range(10):
    rep = 2**(7+i)
    size.append(rep)
    fileo = "stats/l1d_size/stats"+str(rep)+".txt"
    with open(fileo) as f:
        datafile = f.readlines()
    for line in datafile:
        if "system.cpu.dcache.overall_misses::total" in line:
            found = (re.search("([0-9]+)",line))
            data.append(found[0])
        elif "system.cpu.dcache.overall_hits::total" in line:
            found = (re.search("([0-9]+)",line))
            hits.append(found[0])
        elif "system.cpu.dcache.writebacks::total" in line:
            found = (re.search("([0-9]+)",line))
            writebacks[i] = found[0]
        elif "system.cpu.numCycles" in line:
            found = (re.search("([0-9]+)",line))
            numCycles.append(found[0])
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.invert_yaxis()
ax1.plot(data,'o-')
ax1.xaxis.set_ticks(np.arange(10))
ax1.xaxis.set_ticklabels(size)
ax1.legend(["Misses"])
ax2.plot(hits,'o-')
ax2.legend(["Hits"])
ax2.xaxis.set_ticks(np.arange(10))
ax2.xaxis.set_ticklabels(size)
ax3.plot(writebacks,'o-')
ax3.legend(["WriteBack"])
ax3.xaxis.set_ticks(np.arange(10))
ax3.xaxis.set_ticklabels(size)
ax4.plot(numCycles,'o-')
ax4.legend(["numCycles"])
ax4.xaxis.set_ticks(np.arange(10))
ax4.xaxis.set_ticklabels(size)
ax4.invert_yaxis()
show()
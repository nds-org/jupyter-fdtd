# Bare-bones 1D FDTD simulation with a hard source.
import math

SIZE = 200

ez = [0.0] * SIZE
hy = [0.0] * SIZE
imp0 = 377.0
maxTime = 250

# do time stepping
for qTime in range(maxTime):
  #
  # update magnetic field
  for mm in range(SIZE-1):
    hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) / imp0
  #
  # update electric field
  for mm in range(SIZE):
    ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0
  #
  # hardwire a source node */
  ez[0] = math.exp(-(qTime - 30) * (qTime - 30) / 100)
  #
  print(ez[50])

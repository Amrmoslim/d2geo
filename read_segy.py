"""
Program to read SEGY seismic data and convert to Numpy

@author: Yohanes Nuwara
@email: ign.nuwara97@gmail.com
"""

import segyio

# example here is Dutch F3 seismic data
filename = './Dutch Government_F3_entire_8bit seismic.segy'

with segyio.open(filename) as f:

  data = segyio.tools.cube(f)
  inline_data = f.iline
  crossline_data = f.xline

  inlines = f.ilines
  crosslines = f.xlines
  twt = f.samples
  sample_rate = segyio.tools.dt(f) / 1000
  print('Inline range from', inlines[0], 'to', inlines[-1])
  print('Crossline range from', crosslines[0], 'to', crosslines[-1])
  print('TWT from', twt[0], 'to', twt[-1])   
  print('Sample rate:', sample_rate, 'ms')

  clip_percentile = 99
  vm = np.percentile(data, clip_percentile)

f'The {clip_percentile}th percentile is {vm:.0f}; the max amplitude is {data.max():.0f}'

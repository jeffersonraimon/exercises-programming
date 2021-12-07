#question8

fileDown = float(input('type the size of file (MB): '))
speedLink = float(input('type the speed of your link internet (Mbps): ')) /8
print(f'the time aproximate is {((fileDown / speedLink)):0.1f} seconds')

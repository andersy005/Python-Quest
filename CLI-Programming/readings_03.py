import sys
import numpy as np 

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=',')
        for m in np.mean(data, axis=1):
            print(m)
   

if __name__ == '__main__':
    main()
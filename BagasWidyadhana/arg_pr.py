import argparse
from parabola import parabola
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--vo', type=float, default=1.0,
                        help='kecepatan awal')
    parser.add_argument('--agl', type=float, default=1.0,
                        help='waktu')
    parser.add_argument('--x', type=float, default=1.0,
                        help='nilai x')
    parser.add_argument('--y', type=float, default=1.0,
                        help='nilai y')
    parser.add_argument('--rm', type=str, default='null',
                        help='rumus')
    args= parser.parse_args()
    sys.stdout.write(str(rumus(args)))

def rumus(args):
    if args.rm == 'null':
        print('masukan perintah')
    elif args.rm == 'pr':
        v=args.vo
        agl=args.agl
        x=args.x
        y=args.y
        parabola(v,agl,x,y)
    elif args.rm != 'pr':
        print('masukan perintah yang benar')
    elif args.rm != 'null':
        print('masukan perintah yang benar')
    
if __name__ == '__main__':
    main()
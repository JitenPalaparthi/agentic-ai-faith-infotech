import argparse
p = argparse.ArgumentParser()
sub = p.add_subparsers(dest="cmd", required=True)
add = sub.add_parser("add")
add.add_argument("a", type=int)
add.add_argument("b", type=int)
args = p.parse_args()
if args.cmd == "add":
    print(args.a + args.b)

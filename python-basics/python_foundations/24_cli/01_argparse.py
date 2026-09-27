import argparse
p = argparse.ArgumentParser()
p.add_argument("--name", default="Python")
args = p.parse_args()
print("Hello", args.name)

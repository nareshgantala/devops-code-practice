import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--app", required=True)
parser.add_argument("--env", required=True)

args = parser.parse_args()

print(f"Deploying {args.app} in {args.env} environment")

# python deploy.py --app payment --env dev

#!/usr/bin/env python3
"""sm-wordstat — Yandex Wordstat API client."""
import argparse, json, sys, os, urllib.request

API_URL = "https://searchapi.api.cloud.yandex.net/v2/wordstat"

def get_api_key():
    return os.environ.get("WORDSTAT_API_KEY", "")

def get_folder_id():
    return os.environ.get("WORDSTAT_FOLDER_ID", "")

def make_request(body):
    headers = {
        "Authorization": f"Api-Key {get_api_key()}",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode()
    req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def cmd_top(args):
    body = {
        "phrase": args.phrase,
        "numPhrases": args.limit,
        "regions": [args.region],
        "devices": ["DEVICE_ALL"],
        "folderId": get_folder_id(),
    }
    result = make_request(body)
    print(f"Total: {result.get('totalCount', 0)}")
    for r in result.get("results", []):
        print(f"  {r['count']:>8}  {r['phrase']}")

def cmd_dynamics(args):
    from_str = getattr(args, "from")
    body = {
        "phrase": args.phrase,
        "from": from_str,
        "to": args.to,
        "regions": [args.region],
        "folderId": get_folder_id(),
    }
    result = make_request(body)
    for r in result.get("results", []):
        print(f"  {r['date']}  {r['count']:>8}")

def cmd_regions(args):
    body = {
        "phrase": args.phrase,
        "regions": [args.region],
        "folderId": get_folder_id(),
    }
    result = make_request(body)
    for r in result.get("results", []):
        print(f"  {r['regionName']}: {r['count']}")

def main():
    parser = argparse.ArgumentParser(description="Yandex Wordstat API client")
    sub = parser.add_subparsers(dest="command")
    
    p_top = sub.add_parser("top", help="Top requests")
    p_top.add_argument("phrase")
    p_top.add_argument("--limit", type=int, default=50)
    p_top.add_argument("--region", default="225")
    
    p_dyn = sub.add_parser("dynamics", help="Dynamics by month")
    p_dyn.add_argument("phrase")
    p_dyn.add_argument("--from", required=True)
    p_dyn.add_argument("--to", required=True)
    p_dyn.add_argument("--region", default="225")
    
    p_reg = sub.add_parser("regions", help="Regional distribution")
    p_reg.add_argument("phrase")
    p_reg.add_argument("--region", default="225")
    
    args = parser.parse_args()
    
    if args.command == "top":
        cmd_top(args)
    elif args.command == "dynamics":
        cmd_dynamics(args)
    elif args.command == "regions":
        cmd_regions(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

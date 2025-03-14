import argparse

def get_username():
    parser = argparse.ArgumentParser(description="get user name from git hub")
    parser.add_argument("username",type=str,help="give proper name")
    args = parser.parse_args()
    return args.username
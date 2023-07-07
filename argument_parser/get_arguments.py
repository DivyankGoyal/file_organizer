import argparse

def argParser():
    parser = argparse.ArgumentParser(description='Describe Arguments for File Organizer')
    parser.add_argument('-p', '--path', type=str, help='Your name', required=True)
    args = parser.parse_args()
    return args
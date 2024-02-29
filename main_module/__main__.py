import argparse

def create_parser():
    # Create the parser
    parser = argparse.ArgumentParser(description="A sample CLI tool that demonstrates help and available commands.")

    # Define a positional argument
    parser.add_argument('command', type=str, choices=['start', 'stop', 'status'], help="The command to run (start, stop, status).")

    # Define optional arguments
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode.")
    parser.add_argument('-c', '--config', type=str, help="Path to the configuration file.")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    # Example of handling commands
    if args.command == 'start':
        print("Starting the service...")
        if args.verbose:
            print("Verbose mode enabled.")
    elif args.command == 'stop':
        print("Stopping the service...")
    elif args.command == 'status':
        print("Checking the service status...")
    
    if args.config:
        print(f"Using configuration file at {args.config}")

if __name__ == "__main__":
    main()

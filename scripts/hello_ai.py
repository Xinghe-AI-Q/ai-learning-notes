import requests

def print_intro():
    print("AI journey starts here.")

def print_dependency_info():
    print("Requests version:", requests.__version__)

def main():
    print_intro()
    print_dependency_info()

if __name__ == "__main__":
    main()

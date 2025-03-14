from fetch import fectch_by_name
from getname import get_username
from display import display_git
def main():
     username = get_username()

     events = fectch_by_name(username)
     if events:
          
       display_git(events)
  

if __name__ == "__main__":
     main()          
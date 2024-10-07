import cmd
import requests


class MyCLI(cmd.Cmd):
    prompt = 'github-activity -> '
    intro = '''
- Welcome to my User activity tracker!
- You can just type the user like "Mean-says" and see what the user has been doing.
'''

    def __init__(self):
        super().__init__()

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
    def default(self, line):
        if line:
            username = line
            self.get_events(username)
                            
    def get_events(self, username):
        
        url = f'https://api.github.com/users/{username}/events'
        
        try: 
            response = requests.get(url)
            
            if response.status_code == 200:
                dados = response.json()
                event_count = {}

                for item in dados:
                    event_type = item.get("type")
                    repo = item.get("repo", {}).get("name")

                    # Count occurrences of each event type
                    if event_type in event_count:
                        event_count[event_type] += 1
                    else:
                        event_count[event_type] = 1

                # Display the event counts
                for event_type, count in event_count.items():
                    if event_type == 'WatchEvent':
                        print(f"{count} times started watching a repo.")
                    else:
                        print(f"{count} times {event_type.lower()} a repo in {repo}.")

            else:
                print(f"Failed to fetch events for user '{username}': {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    MyCLI().cmdloop()

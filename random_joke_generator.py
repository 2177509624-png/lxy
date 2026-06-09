"""
Random Joke Generator using External APIs
A Python application that fetches random jokes from multiple joke APIs
"""

import requests
import json
import random
from typing import Dict, List, Optional
from datetime import datetime


class JokeGenerator:
    """Generate random jokes from various external APIs"""
    
    # Available joke APIs
    JOKES_API = "https://official-joke-api.appspot.com/jokes/random"
    JOKE_API_COM = "https://api.api-ninjas.com/v1/jokes"
    RANDOM_JOKE_API = "https://icanhazdadjoke.com/"
    CHUCK_NORRIS_API = "https://api.chucknorris.io/jokes/random"
    
    def __init__(self):
        """Initialize the joke generator"""
        self.jokes_history = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_joke_from_official_api(self) -> Optional[Dict]:
        """
        Fetch a random joke from Official Joke API
        
        Returns:
            Dictionary containing joke data or None if failed
        """
        try:
            response = requests.get(self.JOKES_API, headers=self.headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                joke = {
                    'source': 'Official Joke API',
                    'type': data.get('type', 'general'),
                    'setup': data.get('setup', ''),
                    'punchline': data.get('punchline', ''),
                    'full_joke': f"{data.get('setup', '')} - {data.get('punchline', '')}",
                    'timestamp': datetime.now().isoformat()
                }
                return joke
        except Exception as e:
            print(f"Error fetching from Official Joke API: {e}")
        
        return None
    
    def get_dad_joke(self) -> Optional[Dict]:
        """
        Fetch a random dad joke from icanhazdadjoke.com
        
        Returns:
            Dictionary containing joke data or None if failed
        """
        try:
            headers = {
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0'
            }
            response = requests.get(self.RANDOM_JOKE_API, headers=headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                joke = {
                    'source': 'Dad Jokes (icanhazdadjoke)',
                    'type': 'dad_joke',
                    'joke': data.get('joke', ''),
                    'full_joke': data.get('joke', ''),
                    'id': data.get('id', ''),
                    'timestamp': datetime.now().isoformat()
                }
                return joke
        except Exception as e:
            print(f"Error fetching from Dad Jokes API: {e}")
        
        return None
    
    def get_chuck_norris_joke(self) -> Optional[Dict]:
        """
        Fetch a random Chuck Norris joke
        
        Returns:
            Dictionary containing joke data or None if failed
        """
        try:
            response = requests.get(self.CHUCK_NORRIS_API, headers=self.headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                joke = {
                    'source': 'Chuck Norris Jokes',
                    'type': 'chuck_norris',
                    'joke': data.get('value', ''),
                    'full_joke': data.get('value', ''),
                    'id': data.get('id', ''),
                    'url': data.get('url', ''),
                    'timestamp': datetime.now().isoformat()
                }
                return joke
        except Exception as e:
            print(f"Error fetching from Chuck Norris API: {e}")
        
        return None
    
    def get_random_joke(self, source: Optional[str] = None) -> Optional[Dict]:
        """
        Get a random joke from any available API
        
        Args:
            source: Specific joke source ('official', 'dad', 'chuck_norris') or None for random
        
        Returns:
            Dictionary containing joke data or None if failed
        """
        sources = {
            'official': self.get_joke_from_official_api,
            'dad': self.get_dad_joke,
            'chuck_norris': self.get_chuck_norris_joke
        }
        
        if source and source in sources:
            joke = sources[source]()
        else:
            # Pick a random API
            selected_source = random.choice(list(sources.keys()))
            joke = sources[selected_source]()
        
        if joke:
            self.jokes_history.append(joke)
        
        return joke
    
    def display_joke(self, joke: Dict) -> None:
        """
        Display a joke in a nice format
        
        Args:
            joke: Dictionary containing joke data
        """
        if not joke:
            print("✗ Failed to fetch a joke. Please try again!")
            return
        
        print("\n" + "="*70)
        print(f"📢 Source: {joke.get('source', 'Unknown')}")
        print("="*70)
        
        if 'setup' in joke and 'punchline' in joke:
            print(f"\n🎤 {joke['setup']}")
            print(f"\n😂 {joke['punchline']}\n")
        else:
            print(f"\n😂 {joke.get('full_joke', joke.get('joke', 'No joke found'))}\n")
        
        print("="*70)
    
    def get_multiple_jokes(self, count: int = 5) -> List[Dict]:
        """
        Fetch multiple random jokes
        
        Args:
            count: Number of jokes to fetch
        
        Returns:
            List of joke dictionaries
        """
        jokes = []
        for i in range(count):
            print(f"\n[{i+1}/{count}] Fetching joke...", end=" ")
            joke = self.get_random_joke()
            if joke:
                jokes.append(joke)
                print("✓")
            else:
                print("✗")
        
        return jokes
    
    def save_jokes_to_file(self, filename: str = "jokes.json") -> None:
        """
        Save joke history to a JSON file
        
        Args:
            filename: Output filename
        """
        if not self.jokes_history:
            print("✗ No jokes to save!")
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.jokes_history, f, ensure_ascii=False, indent=2)
            print(f"✓ Saved {len(self.jokes_history)} jokes to {filename}")
        except Exception as e:
            print(f"✗ Error saving jokes: {e}")
    
    def display_history(self) -> None:
        """Display all jokes from history"""
        if not self.jokes_history:
            print("✗ No joke history yet!")
            return
        
        print("\n" + "="*70)
        print(f"📚 JOKE HISTORY ({len(self.jokes_history)} jokes)")
        print("="*70)
        
        for i, joke in enumerate(self.jokes_history, 1):
            print(f"\n{i}. [{joke.get('source', 'Unknown')}]")
            if 'setup' in joke and 'punchline' in joke:
                print(f"   Q: {joke['setup']}")
                print(f"   A: {joke['punchline']}")
            else:
                print(f"   {joke.get('full_joke', joke.get('joke', 'N/A'))}")
        
        print("\n" + "="*70)
    
    def get_statistics(self) -> None:
        """Display statistics about fetched jokes"""
        if not self.jokes_history:
            print("✗ No jokes in history!")
            return
        
        sources = {}
        for joke in self.jokes_history:
            source = joke.get('source', 'Unknown')
            sources[source] = sources.get(source, 0) + 1
        
        print("\n" + "="*70)
        print("📊 JOKE STATISTICS")
        print("="*70)
        print(f"Total jokes fetched: {len(self.jokes_history)}")
        print(f"\nBreakdown by source:")
        for source, count in sources.items():
            percentage = (count / len(self.jokes_history)) * 100
            print(f"  • {source}: {count} ({percentage:.1f}%)")
        print("="*70 + "\n")


def interactive_mode():
    """Interactive mode for the joke generator"""
    generator = JokeGenerator()
    
    print("\n" + "="*70)
    print("🎭 RANDOM JOKE GENERATOR")
    print("="*70)
    print("\nWelcome to the Random Joke Generator!")
    print("This app fetches jokes from multiple external APIs.\n")
    
    while True:
        print("\nOptions:")
        print("  1. Get a random joke (any source)")
        print("  2. Get a joke from a specific source")
        print("  3. Get multiple random jokes")
        print("  4. View joke history")
        print("  5. View statistics")
        print("  6. Save jokes to file")
        print("  7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            print("\n⏳ Fetching a random joke...")
            joke = generator.get_random_joke()
            generator.display_joke(joke)
        
        elif choice == "2":
            print("\nAvailable sources:")
            print("  1. Official Joke API (setup & punchline)")
            print("  2. Dad Jokes (icanhazdadjoke)")
            print("  3. Chuck Norris Jokes")
            
            source_choice = input("\nSelect source (1-3): ").strip()
            source_map = {"1": "official", "2": "dad", "3": "chuck_norris"}
            
            if source_choice in source_map:
                print(f"\n⏳ Fetching {source_map[source_choice]} joke...")
                joke = generator.get_random_joke(source=source_map[source_choice])
                generator.display_joke(joke)
            else:
                print("✗ Invalid choice!")
        
        elif choice == "3":
            count_str = input("\nHow many jokes? (default 5): ").strip()
            count = int(count_str) if count_str.isdigit() else 5
            
            print(f"\n⏳ Fetching {count} jokes...")
            jokes = generator.get_multiple_jokes(count)
            
            for joke in jokes:
                generator.display_joke(joke)
        
        elif choice == "4":
            generator.display_history()
        
        elif choice == "5":
            generator.get_statistics()
        
        elif choice == "6":
            filename = input("Enter filename (default: jokes.json): ").strip()
            filename = filename if filename else "jokes.json"
            generator.save_jokes_to_file(filename)
        
        elif choice == "7":
            print("\n👋 Thanks for using the Joke Generator!")
            break
        
        else:
            print("✗ Invalid choice! Please try again.")


def main():
    """Main function with demo mode"""
    import sys
    
    # Check for command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        print("\n" + "="*70)
        print("🎭 JOKE GENERATOR - DEMO MODE")
        print("="*70 + "\n")
        
        generator = JokeGenerator()
        
        # Demo: Get one joke from each source
        sources = ['official', 'dad', 'chuck_norris']
        
        for source in sources:
            print(f"\n📥 Fetching from {source}...")
            joke = generator.get_random_joke(source=source)
            generator.display_joke(joke)
        
        # Show statistics
        generator.get_statistics()
        
        # Save to file
        generator.save_jokes_to_file("demo_jokes.json")
        
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()

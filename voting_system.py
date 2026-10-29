"""
Simple Voting System
--------------------
Features:
1. Add Candidates - Enter candidate names
2. Vote - Cast a vote
3. Result - Show vote count and winner
"""

import sys

class VotingSystem:
    def __init__(self):
        # Dictionary to store candidate names and their vote counts
        # Structure: {candidate_name: vote_count}
        self.candidates = {}

    def add_candidate(self, name: str) -> bool:
        """Add a candidate by name."""
        name = name.strip()
        if not name:
            print("[!] Candidate name cannot be empty.")
            return False
        
        # Case-insensitive duplicate check
        for existing in self.candidates:
            if existing.lower() == name.lower():
                print(f"[!] Candidate '{name}' already exists.")
                return False

        self.candidates[name] = 0
        print(f"[+] Candidate '{name}' added successfully!")
        return True

    def cast_vote(self, candidate_name: str) -> bool:
        """Cast a vote for a candidate."""
        # Find candidate matching case-insensitively
        for existing in self.candidates:
            if existing.lower() == candidate_name.strip().lower():
                self.candidates[existing] += 1
                print(f"[OK] Vote cast successfully for '{existing}'!")
                return True
        
        print(f"[!] Candidate '{candidate_name}' not found. Please choose from the list.")
        return False

    def get_results(self):
        """Display vote counts and identify the winner(s)."""
        if not self.candidates:
            print("[!] No candidates have been registered yet.")
            return

        total_votes = sum(self.candidates.values())
        print("\n" + "=" * 45)
        print("               ELECTION RESULTS              ")
        print("=" * 45)
        print(f"Total Votes Cast: {total_votes}")
        print("-" * 45)
        print(f"{'Candidate Name':<25} | {'Votes':<7} | {'Percentage':<8}")
        print("-" * 45)

        for candidate, votes in self.candidates.items():
            pct = (votes / total_votes * 100) if total_votes > 0 else 0.0
            print(f"{candidate:<25} | {votes:<7} | {pct:>6.2f}%")
        print("-" * 45)

        if total_votes > 0:
            max_votes = max(self.candidates.values())
            winners = [name for name, votes in self.candidates.items() if votes == max_votes]

            if len(winners) == 1:
                print(f"[WINNER] {winners[0]} with {max_votes} vote(s)!")
            else:
                print(f"[TIE] Tie between: {', '.join(winners)} with {max_votes} vote(s) each!")
        else:
            print("No votes have been cast yet.")
        print("=" * 45 + "\n")


def display_menu():
    print("\n" + "=" * 35)
    print("       SIMPLE VOTING SYSTEM        ")
    print("=" * 35)
    print("1. Add Candidates (Enter names)")
    print("2. Vote (Cast a vote)")
    print("3. Result (Show vote count)")
    print("4. View All Candidates")
    print("5. Reset All Votes")
    print("6. Exit")
    print("=" * 35)


def main():
    system = VotingSystem()
    print("Welcome to the Simple Voting System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Add Candidates ---")
            names_input = input("Enter candidate name(s) (comma-separated for multiple): ")
            names = [n.strip() for n in names_input.split(",") if n.strip()]
            if not names:
                print("[!] No candidate name entered.")
            else:
                for name in names:
                    system.add_candidate(name)

        elif choice == "2":
            print("\n--- Cast a Vote ---")
            if not system.candidates:
                print("[!] No candidates available. Please add candidates first.")
                continue

            candidates_list = list(system.candidates.keys())
            print("Available Candidates:")
            for idx, name in enumerate(candidates_list, start=1):
                print(f"  {idx}. {name}")

            vote_input = input("Enter candidate number or name to vote for: ").strip()
            
            # Check if input is an index
            if vote_input.isdigit():
                index = int(vote_input) - 1
                if 0 <= index < len(candidates_list):
                    chosen_candidate = candidates_list[index]
                    system.cast_vote(chosen_candidate)
                else:
                    print("[!] Invalid candidate number.")
            else:
                system.cast_vote(vote_input)

        elif choice == "3":
            system.get_results()

        elif choice == "4":
            print("\n--- Registered Candidates ---")
            if not system.candidates:
                print("[!] No candidates registered.")
            else:
                for idx, name in enumerate(system.candidates.keys(), start=1):
                    print(f"  {idx}. {name}")

        elif choice == "5":
            confirm = input("Are you sure you want to reset all vote counts to 0? (y/n): ").strip().lower()
            if confirm == "y":
                for candidate in system.candidates:
                    system.candidates[candidate] = 0
                print("[OK] All vote counts have been reset to 0.")
            else:
                print("Reset cancelled.")

        elif choice == "6":
            print("Thank you for using Simple Voting System. Goodbye!")
            sys.exit(0)

        else:
            print("[!] Invalid choice. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()

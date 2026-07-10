"""Movie Interest Recommendation CLI.

Computes common and unseen web series interests between two users in a dataset.
"""

def run_movie_recommendation():
    dataset = {
        'Rahul': {'Permanent Roomates': 2, 'Inside Edge': 3, 'Four More Shots Please': 3, 'Sacred Games': 3, 'Apharan': 2, 'Mirzapur': 3},
        'Rishabh': {'Permanent Roomates': 3, 'Inside Edge': 3, 'Sacred Games': 5, 'Mirzapur': 3, 'Apharan': 3},
        'Sonali': {'Permanent Roomates': 2, 'Inside Edge': 3, 'Sacred Games': 3, 'Mirzapur': 4},
        'Ritvik': {'Inside Edge': 4, 'Apharan': 2, 'Sacred Games': 4},
        'Harshita': {'Permanent Roomates': 4, 'Inside Edge': 4, 'Four More Shots Please': 2, 'Sacred Games': 3, 'Mirzapur': 3, 'Apharan': 2},
        'Shubhi': {'Permanent Roomates': 3, 'Inside Edge': 4, 'Mirzapur': 3, 'Sacred Games': 5, 'Apharan': 3},
        'Shaurya': {'Inside Edge': 4, 'Apharan': 1, 'Sacred Games': 4}
    }
    
    print("--- Movie Interest Recommendation ---")
    print("Available Users:", ", ".join(dataset.keys()))
    
    a = input("Enter Name 1: ").strip()
    b = input("Enter Name 2: ").strip()
    
    if a not in dataset or b not in dataset:
        print("Error: One or both names do not exist in the dataset.")
        return
        
    s1 = set(dataset[a].keys())
    s2 = set(dataset[b].keys())
    
    print(f"\n{a}'s watched series: {s1}")
    print(f"{b}'s watched series: {s2}")
    print("-" * 45)
    
    common = s1.intersection(s2)
    unseen = s1.union(s2) - common
    
    print("Common web series watched:")
    print(f"  {common if common else 'None'}")
    print("\nUnseen/unshared web series (watched by only one of them):")
    print(f"  {unseen if unseen else 'None'}")

if __name__ == "__main__":
    run_movie_recommendation()

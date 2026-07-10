"""Dot Product calculator using an efficient approach.

Refactored from O(N^2) loop to O(N) lookup.
"""

def run_vector_dot():
    a = [2, 4, 6, 8, 10]
    b = [1, 5, 1, 2, 3]
    
    # Refactored from nested loops to list zip computation
    dot_product = sum(x * y for x, y in zip(a, b))
    
    print("--- Dot Product ---")
    print("Vector A:   ", a)
    print("Vector B:   ", b)
    print("Dot Product:", dot_product)

if __name__ == "__main__":
    run_vector_dot()

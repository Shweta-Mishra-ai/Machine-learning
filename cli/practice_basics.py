"""Consolidated Basic Programming Practice.

Holds the custom character sorting, list inserts, updates, and lambda power logic
originally found in str.txt, lst.txt, and neg_pow.txt.
"""

def run_string_sorting():
    string_val = "shweta"
    s = set(string_val)
    l = list(s)
    l.sort()
    print("String Sorting Practice (Unique sorted characters in 'shweta'):")
    print(f"  Result: {l}")

def run_list_manipulation():
    lst = [10, 20, 30, 50]
    lst2 = [40]
    print("\nList Manipulation Practice:")
    print(f"  Original list: {lst}")
    print(f"  Inserting element: {lst2}")
    
    # Inserting 40 at index 3
    lst_new = lst[:3] + lst2 + lst[3:]
    print(f"  After insertion: {lst_new}")
    
    # Deleting element 30 (which was at index 2)
    lst_del = lst_new[:2] + lst_new[3:]
    print(f"  After deleting 30: {lst_del}")
    
    # Updating 20 with 25
    lst_update = list(lst_del)
    for i in range(len(lst_update)):
        if lst_update[i] == 20:
            lst_update[i] = 25
    print(f"  After replacing 20 with 25: {lst_update}")

def run_lambda_power():
    print("\nLambda Power Practice:")
    power_fn = lambda x, y: x ** y
    base, exp = 2, -3
    res = power_fn(base, exp)
    print(f"  Base={base}, Exp={exp}")
    print(f"  Calculated Power: {res}")

def run_all_practice():
    print("--- Running Preserved Practice Snippets ---")
    run_string_sorting()
    run_list_manipulation()
    run_lambda_power()

if __name__ == "__main__":
    run_all_practice()

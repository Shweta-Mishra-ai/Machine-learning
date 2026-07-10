"""Utility functions for array and list manipulations, searches, and sorting."""

def second_max(lst: list[float]) -> float:
    """Find the second maximum value in a list of numbers.
    
    Ignores duplicates (e.g. for [1, 2, 6, 6, 6, 5], returns 5).
    """
    unique_vals = list(set(lst))
    if len(unique_vals) < 2:
        raise ValueError("List must contain at least two unique elements to find second maximum.")
    unique_vals.sort()
    return unique_vals[-2]

def second_lowest_students(students: list[list]) -> list[str]:
    """Find student names with the second lowest grade.
    
    Returns names sorted alphabetically. Assumes input format is a list of [name, grade].
    """
    if len(students) < 2:
        raise ValueError("List must contain at least two students.")
    
    grades = {s[1] for s in students}
    if len(grades) < 2:
        raise ValueError("There must be at least two unique grades in the dataset.")
    
    second_lowest_grade = sorted(list(grades))[1]
    matching_names = [s[0] for s in students if s[1] == second_lowest_grade]
    return sorted(matching_names)

def adjacent_nearest_neighbor(lst: list[float], val: float) -> float:
    """Find the nearest adjacent neighbor in a sorted list for a value present in the list.
    
    Safely handles boundary cases (first and last elements of the list) to prevent IndexError.
    """
    # Ensure list is sorted for logic to hold
    sorted_lst = sorted(lst)
    if val not in sorted_lst:
        raise ValueError(f"Value {val} must exist in the list.")
    if len(sorted_lst) < 2:
        raise ValueError("List must contain at least two elements to determine neighbors.")
    
    idx = sorted_lst.index(val)
    if idx == 0:
        return sorted_lst[1]
    if idx == len(sorted_lst) - 1:
        return sorted_lst[-2]
    
    left_dist = val - sorted_lst[idx - 1]
    right_dist = sorted_lst[idx + 1] - val
    
    if left_dist <= right_dist:
        return sorted_lst[idx - 1]
    else:
        return sorted_lst[idx + 1]

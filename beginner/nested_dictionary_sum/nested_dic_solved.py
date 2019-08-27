def recursive_sum(n): #write a function that returns the sum of any number of nested dictionaries
    current_sum=0
    for key in n:
        if not isinstance(n[key], dict):
            current_sum=current_sum+n[key]
        else:
            current_sum=current_sum+recursive_sum(n[key])
    return current_sum

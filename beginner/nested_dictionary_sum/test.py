from nested_dic import recursive_sum

x={
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': {
                'f': 4,
                'g':{
                    'h':
                    {
                        'i':5
                    }
                }
            }
        }
    }
y={
        'a': 1,
        'b': 2,
        'c': {
		'd': 3,
		'e': {
			'f': 4
		}
	}
}
z={
        'a': {'A':-1},
        'b': 2,
        'c': {
                'd': 3,
                'e': {
                        'f': 4
                }
        }
}

if recursive_sum(x) != 15:
    print("Fail")
elif recursive_sum(x) == 15:
    print("Pass")
if recursive_sum(y) != 10:
    print("Fail")
elif recursive_sum(y) == 10:
    print("Pass")
if recursive_sum(z) == 8:
    print("Pass")
elif recursive_sum(z) !=8:
    print("Fail")

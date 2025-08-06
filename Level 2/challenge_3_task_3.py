def num_obj(s):
    return [{str(num): chr(num)} for num in s]

print(num_obj([118, 117, 120]))
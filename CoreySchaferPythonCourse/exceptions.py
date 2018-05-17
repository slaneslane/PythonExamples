# exceptions.py
# based on: https://www.youtube.com/watch?v=NIWwJbo-9_8

try:
    f = open('Sample-Dir-One/file1_1')
#    if f.name == file1_1:
#        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally')

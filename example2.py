# example3.py


from __future__ import print_function 
from trains import Task
import string_func

 
task = Task.init(project_name='test', task_name='Tensorflow mnist example - 2 files')


some_string = "Hello, Universe!"

print(string_func.stringLength(some_string))
print(string_func.stringToLower(some_string))
print(string_func.stringToUpper(some_string))
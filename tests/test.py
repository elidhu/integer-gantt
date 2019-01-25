import integer_gantt
data = utils.load('fake.json')
from generate import gantt
gantt(data, 'Weeks', 'Tasks', 'gantt.png')
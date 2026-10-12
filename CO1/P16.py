my_dict={'banana':3,'apple':1,'cherry':2,'date':4}
print(my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("assending",asorted_dict)
desorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("desending",desorted_dict)

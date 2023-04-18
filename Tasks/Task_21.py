a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
     {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

b = []
for i in a :
     for (k, v) in i.items() :
              b.append(v.strip())
print(set(b))

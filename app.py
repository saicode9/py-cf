json_obj = {
  "text": "hello world",
  "predictions":
   [
     {"class": "Class 1", "percentage": 4.63},
     {"class": "Class 2", "percentage": 74.68},
     {"class": "Class 3", "percentage": 9.38},
     {"class": "Class 4", "percentage": 5.78},
     {"class": "Class 5", "percentage": 5.53}
   ]
}

sorted_obj = dict(json_obj)
sorted_obj['predictions'] = sorted(json_obj['predictions'], key=lambda x : x['percentage'])

print(sorted_obj)
print(json_obj)

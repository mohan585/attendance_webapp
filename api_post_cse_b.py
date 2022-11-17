
from deta import Deta

deta = Deta("c0tuummb_bRtUtBpGWyhhaLkpQGrX7JQAtiYM2eyd")

users = deta.Base("Total_Classes_CSE_B")
students = deta.Base("Students_Data_CSE_B")
time = deta.Base("last_time")



def total_return():
  fetch_res_4 = users.fetch({"select": "Subs_Value"})
  return fetch_res_4.items
# fetch_res = users.fetch({"select": "Subs_Value"})

# print(fetch_res.items)

def list_converter(total_data):
    new_list = []
    for i in total_data:
        i.pop("key")
        i.pop("select")
        new_list.append(i)

    for i in range(len(new_list)):
        if new_list[i]["subjects"] == "TOTAL":
            del new_list[i]
            break
    return new_list


def total_adder(names1,names2):
    res = [list(ele) for ele in names2]
    for i in names1:
        for j in range(len(res)):
            if i["subjects"] == names2[j][0]:
                res[j].append(i["values"])
    return res

def pin_checker(pin):
  fetch_res_2 = students.fetch({"Pin": f"{pin}"})
  return fetch_res_2.items

def time_checker():
    time_fetch = time.fetch({"time": "last"})
    return time_fetch.items

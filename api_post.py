
from deta import Deta

deta = Deta("c0tuummb_bRtUtBpGWyhhaLkpQGrX7JQAtiYM2eyd")

users = deta.Base("Total_Classes")
students = deta.Base("Students_Data")





# def total_data():
#   table = soup.find('table')
#   rows = table.find_all('tr')[0]
#   rows1 = table.find_all('tr')[1]
#   name = rows.find_all('td')
#   name1 = rows1.find_all('td')
#   list_subs = []
#   list_value = []
#   for i in name:
#     if "Sl.No" != i.text and "Student Name" != i.text and "" != i.text and "Roll.No" != i.text and "%" != i.text:
#       list_subs.append(i.text)
#   for i in name1:
#     if "Batch-1" != i.text and "\xa0" != i.text:
#       list_value.append(i.text)
#   return list_subs,list_value


# def total_list():
#   list_subs,list_value = total_data()
#   for i,j in zip(list_subs,list_value):
#     users.insert({
#     "select": "Subs_Value",
#     "subjects": f"{i}",
#     "values": f"{j}"
#     })

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

# def update():
#   list_subs,list_value = total_data()
#   fetch_res = users.fetch({"select": "Subs_Value"})
#   for i in fetch_res.items:
#     key = i['key']
#     subjects = i['subjects']
#     for x,j in zip(list_subs,list_value):
#       if x == subjects:
#         users.put({
#           "select": "Subs_Value",
#           "subjects": f"{subjects}",
#           "values": f"{j}"
#           },key)







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

# def student_retr():
#   table = soup.find('table')
#   rows = table.find_all('tr')
#   itercars = iter(rows)
#   next(itercars)
#   next(itercars)
#   return itercars

# def student_data_update():
#   fetch_res_1 = students.fetch({"data": "students"})
#   table = soup.find('table')
#   rows = table.find_all('tr')
#   itercars = iter(rows)
#   next(itercars)
#   next(itercars)
#   for i in fetch_res_1.items:
#     key = i['key']
#     pins = i['Pin']
#     for row in itercars:
#       pin = (row.find_all('td')[2]).text
#       name = (row.find_all('td')[3]).text
#       cn = (row.find_all('td')[4]).text
#       daa = (row.find_all('td')[5]).text
#       dwdm = (row.find_all('td')[6]).text
#       ai = (row.find_all('td')[7]).text
#       be = (row.find_all('td')[8]).text
#       es = (row.find_all('td')[9]).text
#       dwdm_lab = (row.find_all('td')[10]).text
#       cn_lab = (row.find_all('td')[11]).text
#       dev_ops = (row.find_all('td')[12]).text
#       total = (row.find_all('td')[13]).text
#       percent = (row.find_all('td')[14]).text
#       if str(pin) == str(pins):
#         students.put({
#           "data": "students",
#           "Pin": f"{pin}",
#           "Name": f"{name}",
#           "CN": f"{cn}",
#           "DAA": f"{daa}",
#           "DWDM": f"{dwdm}",
#           "AI": f"{ai}",
#           "BE": f"{be}",
#           "ES": f"{es}",
#           "DWDM_LAB": f"{dwdm_lab}",
#           "CN_LAB": f"{cn_lab}",
#           "DEV_OPS": f"{dev_ops}",
#           "TOTAL": f"{total}",
#           "Percent": f"{percent}",
#           "Status": False
#           },key)
        

# student_data_update()

# fetch_res_1 = students.fetch({"data": "students"})
# for item in fetch_res_1.items:
#     students.delete(item["key"])
    
    
# for row in rows:
#     name = row.find('td').text
#     second = row.find_all('td')[2].text
#     # print(row.attr( "class" ))
#     print(name,second)

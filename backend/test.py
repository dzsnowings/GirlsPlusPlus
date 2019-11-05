import cgi
import csv

form = cgi.FieldStorage()
searchterm = form.getvalue('dream')

# driver = webdriver.PhantomJS()
# driver.get(my_url)
# p_element = driver.find_element_by_id(id_='dream')
# print(p_element.text)

with open("test.csv", "w") as fout:
  writer = csv.writer(fout)
  writer.writerow(["hello", "python"])

file1 = open("test.txt","w+")
file1.writelines(["hello", ",", "python"])
file1.close()

import tkinter as tk
from tkinter import ttk

#future use
tooltypes = ['no tool selected!', 'all others', 'reamer', 'carbide reamer', 'carbide, all others']
tt = [0]

class Material:
  def __init__(self, family, name, lowsfm, highsfm):
    self.name = name
    self.family = 'carbon'
    self.lowsfm = lowsfm
    self.highsfm = highsfm
  

under32hrc = []
above32hrc = []


under32hrc.append(Material('(P) steel', 'high strength steel',50, 250))
under32hrc.append(Material('(P) steel', 'high alloy steel', 100, 300))
under32hrc.append(Material('(P) steel', 'medium alloy steel', 150, 350))
under32hrc.append(Material('(P) steel', 'low alloy steel', 100, 400))
under32hrc.append(Material('(M) stainless steel', 'precipitation', 80, 250))
under32hrc.append(Material('(M) stainless steel', 'austenic', 100, 350))
under32hrc.append(Material('(M) stainless steel', 'martensitic', 100, 250))
under32hrc.append(Material('(K) cast iron', 'ductile cast iron', 100, 400))
under32hrc.append(Material('(K) cast iron', 'gray cast iron', 100, 400))
under32hrc.append(Material('(N) non-ferrous mat.', 'aluminum and alloys', 800, 2000))
under32hrc.append(Material('(N) non-ferrous mat.', 'copper', 800, 1500))
under32hrc.append(Material('(N) non-ferrous mat.', 'copper alloys', 800, 1000))
under32hrc.append(Material('(N) non-ferrous mat.', 'magnesium', 1000, 1000))
under32hrc.append(Material('(N) non-ferrous mat.', 'plastics, acrylics, phenolics', 200, 800))
under32hrc.append(Material('(N) non-ferrous mat.', 'carbon, graphites', 200, 400))
under32hrc.append(Material('(S) super alloys', 'titanium alloys', 50, 250))
under32hrc.append(Material('(H) high temp alloys', 'cobalt alloys', 60, 100))
under32hrc.append(Material('(H) high temp alloys', 'nickle alloys', -1, -1))
under32hrc.append(Material('(H) high temp alloys', 'iron alloys', 80, 130))


above32hrc.append(Material('(P) steel', 'high strength steel', 80, 180))
above32hrc.append(Material('(P) steel', 'high alloy steel', 80, 180))
above32hrc.append(Material('(P) steel', 'medium alloy steel', 80, 180))
above32hrc.append(Material('(P) steel', 'low alloy steel', 100, 200))
above32hrc.append(Material('(M) stainless steel', 'precipitation', 90, 150))
above32hrc.append(Material('(M) stainless steel', 'austenic', 100, 150))
above32hrc.append(Material('(M) stainless steel', 'martensitic', 100, 175))
above32hrc.append(Material('(K) cast iron', 'ductile cast iron', 100, 200))
above32hrc.append(Material('(K) cast iron', 'gray cast iron', 80, 140))
above32hrc.append(Material('(N) non-ferrous mat.', 'aluminum and alloys', 500, 1000))
above32hrc.append(Material('(N) non-ferrous mat.', 'copper', 800, 1000))
above32hrc.append(Material('(N) non-ferrous mat.', 'copper alloys', 700, 1000))
above32hrc.append(Material('(N) non-ferrous mat.', 'magnesium', 700, 1000))
above32hrc.append(Material('(N) non-ferrous mat.', 'plastics, acrylics, phenolics', 200, 500))
above32hrc.append(Material('(N) non-ferrous mat.', 'carbon, graphites', -1, -1))
above32hrc.append(Material('(S) super alloys', 'titanium alloys', 90, 160))
above32hrc.append(Material('(H) high temp alloys', 'cobalt alloys', 40, 80))
above32hrc.append(Material('(H) high temp alloys', 'nickle alloys', 50, 90))
above32hrc.append(Material('(H) high temp alloys', 'iron alloys', 60, 120))


window = tk.Tk()
window.geometry = ('700x300')
window.title("CNC Drilling & Milling Speeds Calculator")
notebook = ttk.Notebook(window)
tabcontrol = ttk.Notebook(window)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text="Materials selector")
tabcontrol.add(tab2, text="Speed Calculator")
tabcontrol.pack(expand=1, fill="both")



def msg_success():
  print("tab change d!")

tabs = [tab1, tab2]

matnames = []
allmats = []
for mat in under32hrc:
  allmats.append(mat)
  matnames.append(mat.family + ' - ' + mat.name + '(< 32 hrc)')

mat = None #so we don't cause iterator problems with the the material variable
for mat in above32hrc:
  allmats.append(mat)
  matnames.append(mat.family + ' - ' + mat.name + '(> 32 hrc))')



def show(self):
  print(str_out.get())
  print(f"material: {str_out.get()},  sfm: {allmats[matnames.index(str_out.get())].lowsfm} - {allmats[matnames.index(str_out.get())].highsfm}")
  l2.config(text = f"sfm: {allmats[matnames.index(str_out.get())].lowsfm} - {allmats[matnames.index(str_out.get())].highsfm}")
  pass





str_out=tk.StringVar(tab1)
str_out.set("Output")

l2 = tk.Label(tab1, text="select a material", width=32 )
l2.pack()


options = tk.OptionMenu(tab1, str_out, *matnames, command=show).pack()



def callback(P):
    if str.isdigit(P) or P == "" or P == ".":
        return True
    else:
        return False

vcmd = (tab2.register(callback),"%P")


def calcmillrpm():
  try:
    rsfm = float(sfmentry.get())
    inches = float(inchentry.get())
    rpm = (rsfm*12)/(3.141592*inches)
    finalrpm.config(text = str(rpm))

  except ValueError:
    return None #return any nonmatching input

recomsfmlab = tk.Label(tab2, text="enter precise manf. sfm: ")
toolincheslab = tk.Label(tab2, text="tool diameter in inches: ")
sfmentry = tk.Entry(tab2, width=32)

recomsfmlab.pack()
sfmentry.pack()
toolincheslab.pack()
inchentry = tk.Entry(tab2, validate='all', validatecommand=(vcmd, '%P'), width=32)
calcrpmbtn = tk.Button(tab2, text="Calculate RPM", command=calcmillrpm)
finalrpm = tk.Label(tab2, text="rpm...")


recomsfmlab.pack()
toolincheslab.pack()
sfmentry.pack()
inchentry.pack()
calcrpmbtn.pack()
finalrpm.pack()


window.mainloop()
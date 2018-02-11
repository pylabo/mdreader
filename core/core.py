import json
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
from subprocess import Popen, STDOUT, call

class createx():
  def __init__(self,master):
    self.master = master
    self.root = Toplevel(master,bg="#FFFFFF")
    self.root.title('X Instance')
  def get(self,obj):
    objhandler = {'root':self.root,'master':self.master}
    return objhandler[obj]
  def destroy(self,obj):
    objhandler = {'root':self.root,'master':self.master}
    objhandler[obj].destroy()

class mdreader(createx):
  def __init__(self,master):
    createx.__init__(self,master)
    self.root.focus()
    self.filename = None
    self.languagecmd = json.load(open('visualiser.json',mode='r'))['language']['cmd']
    self.language = json.load(open('visualiser.json',mode='r'))['language']['name']+' '+json.load(open('visualiser.json',mode='r'))['language']['version']
    self.title = 'Visualiser - / - '+str(self.filename).split()[-1]
    self.root.title(self.title)
    self.topnav = Frame(self.root,bg='#fff')
    self.topnav.pack(side=TOP,fill=X)
    self.language = Label(self.topnav,text=self.language,fg='#000',bg='#fff')
    self.language.pack(side=RIGHT)
    self.filenamel = Label(self.topnav, text=self.filename, fg='#0af', bg='#fff')
    self.filenamel.pack(side=RIGHT, fill=X)
    self.filefr = Frame(self.topnav)
    self.filefr.pack(side=LEFT)
    self.filestate = False
    self.file = Label(self.filefr,text='File',fg='#0af',bg='#fff')
    self.file.bind('<ButtonRelease-1>',self._choosefileoptions)
    self.file.pack(side=LEFT)
    self.fileopfr = Frame(self.filefr)
    self.fileopsave = Label(self.fileopfr,text='Save',fg='#0af',bg='#fff')
    self.fileopsave.bind('<ButtonRelease-1>',self._save)
    self.fileopsaveas = Label(self.fileopfr,text='Save As',fg='#0af',bg='#fff')
    self.fileopsaveas.bind('<ButtonRelease-1>',self._saveas)
    self.fileopopen = Label(self.fileopfr,text='Open',fg='#0af',bg='#fff')
    self.fileopopen.bind('<ButtonRelease-1>',self._open)
    self.fileopsave.pack(side=LEFT)
    self.fileopsaveas.pack(side=LEFT)
    self.fileopopen.pack(side=LEFT)
    '''self.runfr = Frame(self.topnav)
    self.runfr.pack(side=LEFT)
    self.runstate = False
    self.run = Label(self.runfr,text='Run',fg='#707',bg='#fff')
    self.run.bind('<ButtonRelease-1>',self._chooserunoptions)
    self.run.pack(side=LEFT)
    self.runopfr = Frame(self.runfr)
    self.runopos = Label(self.runopfr,text='OS Shell',fg='#707',bg='#fff')
    self.runopos.bind('<ButtonRelease-1>',self._runossh)
    self.runopos.pack(side=LEFT)'''
    self.exitfr = Frame(self.topnav)
    self.exitfr.pack(side=LEFT)
    self.exit = Label(self.exitfr,text='Exit',fg='#f00',bg='#fff')
    self.exit.bind('<ButtonRelease-1>',self._rootdestroy)
    self.exit.pack(side=LEFT)
    self.helpstate = False
    self.helpfr = Frame(self.topnav)
    self.helpfr.pack(side=LEFT)
    self.help = Label(self.helpfr,text='Help',fg='#f90',bg='#fff')
    self.help.bind('<ButtonRelease-1>',self._choosehelpoptions)
    self.help.pack(side=LEFT)
    self.helpopfr = Frame(self.helpfr)
    self.helpopabout = Label(self.helpopfr,text='About',fg='#f90',bg='#fff')
    self.helpopabout.bind('<ButtonRelease-1>',self._about)
    self.helpopabout.pack(side=LEFT)
    self.rootfield = Frame(self.root,relief=FLAT,bd=0,bg='#fff')
    self.textfield = Frame(self.rootfield,relief=FLAT,bd=0,bg='#fff')
    self.text = Text(self.textfield,bg='#fff',relief=FLAT,bd=0,font='consolas 11',fg='#000')
    yscroll = ttk.Scrollbar(self.textfield)
    self.text.config(yscrollcommand=yscroll.set)
    yscroll.config(command=self.text.yview)
    xscroll = ttk.Scrollbar(self.textfield)
    self.text.config(xscrollcommand=xscroll.set)
    xscroll.config(command=self.text.xview)
    yscroll.pack(side=RIGHT, fill=Y)
##    xscroll.pack(side=BOTTOM, fill=X)
    self.cnvsfield = Frame(self.rootfield,relief=FLAT,bd=0,bg='#fff')
    self.cnvs = Canvas(self.cnvsfield,bg='#fff',relief=FLAT,bd=0,width=640,height=360)
    self.text.pack(side=LEFT,fill=BOTH)
    self.cnvs.pack(side=RIGHT,fill=BOTH)
    self.textfield.pack(side=LEFT,fill=BOTH)
    self.cnvsfield.pack(side=RIGHT,fill=BOTH)
    self.rootfield.pack(side=TOP,fill=BOTH)
    self.root.mainloop()
  def _rootdestroy(self,event=None):
    self.root.destroy()
  def _choosefileoptions(self,event=None):
    if self.filestate:
      self._hidefileoptions()
    else:
      self._showfileoptions()
  def _showfileoptions(self):
    self.filestate = True
    self.fileopfr.pack(side=LEFT)
  def _hidefileoptions(self):
    self.filestate = False
    self.fileopfr.pack_forget()
  def _chooserunoptions(self,event=None):
    if self.runstate:
      self._hiderunoptions()
    else:
      self._showrunoptions()
  def _showrunoptions(self):
    self.runstate = True
    self.runopfr.pack(side=LEFT)
  def _hiderunoptions(self):
    self.runstate = False
    self.runopfr.pack_forget()
  def _choosehelpoptions(self,event=None):
    if self.helpstate:
      self._hidehelpoptions()
    else:
      self._showhelpoptions()
  def _showhelpoptions(self):
    self.helpstate = True
    self.helpopfr.pack(side=LEFT)
  def _hidehelpoptions(self):
    self.helpstate = False
    self.helpopfr.pack_forget()
  def _changefile(self,filename):
    print('i self._changefile')
    self.filename = filename
    print('i self.filename',self.filename)
    self.title = 'Visualiser - / - '+str(self.filename).split('/')[-1]
    self.filenamel.config(text=self.filename)
    self.root.title(self.title)
    print('i self._changefile END')
  '''def _runossh(self,event=None):
    print('i self._run')
    self.root.withdraw()
    print('i "OS Shell"')
    call([self.languagecmd,self.filename])
    self.root.deiconify()
  def _runcstm(self,cmd,event=None):
    print('i self._run')
    self.root.withdraw()
    print('i "Custom"')
    call([cmd,self.filename])
    self.root.deiconify()
  def _save(self,event=None):
    print('i self._save')
    if self.filename == None:
      print('! self.filename is NoneType')
      print('i Redirect to self._saveas')
      self._saveas()
    else:
      self.root.title(self.title+' - Saving {}...'.format(self.filename.split('/')[-1]))
      obj = open(self.filename,mode='w')
      obj.write(self.text.get('0.0',END))
      obj.close()
      self.root.title(self.title+' - Saved {}'.format(self.filename.split('/')[-1]))
  def _saveas(self,event=None):
    print('i self._saveas')
    self.root.title(self.title + ' - Saving As...')
    file = filedialog.asksaveasfilename()
    self.root.title(self.title + ' - Saving As {}...'.format(file.split('/')[-1]))
    if file not in ('',None):
      self._changefile(file)
      self._save()
    else:
      pass
    self.root.title(self.title + ' - Saved As {}'.format(self.filename.split('/')[-1]))'''
  def _open(self,event=None):
    file = filedialog.askopenfilename()
    if file not in ('',None):
      self._changefile(file)
      self.root.title(self.title+' - Opening...')
      obj = open(self.filename,mode='r')
      self.text.delete('0.0',END)
      self.text.insert('0.0',obj.read())
      obj.close()
      self.root.title(self.title+' - Opened')
    else:
      pass
  def _about(self,event=None):
    root = Toplevel(self.root,bg='#fff')
    root.focus()
    root.title('Visualiser - /Help/About')
    title =  Label(root,text='\nNo Image\n\nMDReader 0.0.0',bg='#fff',fg='#0af',font='consolas 25')
    version = Label(root,text='mdreader-0_0_0,py-3_6_X(tkinter)\n',bg='#fff',fg='#0af',font='consolas 10')
    description = Label(root,text='A Python 3 script\nfor making tkinter turtle\nand\ntkinter Canvas programs in Python 3.\n',bg='#fff',fg='#0af',font='consolas 15')
    author = Label(root,text='By Ken Shibata (@python3lover on GitLab and GitHub)\n',bg='#fff',fg='#0af',font='consolas 13')
    title.pack(side=TOP)
    version.pack(side=TOP)
    description.pack(side=TOP,fill=X)
    author.pack(side=BOTTOM,fill=X)

if __name__ == '__main__':
  master = Tk(className=' MDReader')
  btn = Button(master,text='STOP\n--------------------------------------------------\nStop Process\n--------------------------------------------------\nVisualiser master',fg='#f00',command=exit)
  btn.pack(fill=BOTH)
  x = visualiser(master)

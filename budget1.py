import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import datetime


        



class MainWindow(Screen):
    def password(self,p):
        f = open("pass.txt", "r+")

        lines = f.readlines()
        result = False
        if not lines: 
            f.write(p)
            result = True
        elif lines[0] == p: result = True
        f.close()
        return result


class PassWindow(Screen):
    def passChange(self,old,new):
        f = open("pass.txt", "r")
        lines = f.readlines()
        f.close()
        result = False
        if not lines and old == '': 
            f = open("pass.txt", "w")
            f.write(new)
            result = True
            f.close()
        elif not lines and old != '': result = False
        elif lines[0] == old: 
            f = open("pass.txt", "w")
            f.write(new)
            result = True
            f.close()
        return result

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

    def year(self):
        return datetime.date.today().year

    def dateValid(self,day,month):
        y = datetime.date.today().year
        ten = ['0','1','2','3','4','5','6','7','8','9']
        if any([d not in ten for d in day]): return False
        if any([m not in ten for m in month]): return False
        try:
            newDate = datetime.datetime(y, int(month), int(day))
            return True
        except ValueError:
            return False

    def decimal(self,entry):
        try:
            f = float(entry)
            return True
        except ValueError:
            return False


    def write(self,s):
        f = open("entries.txt", "a")    
        f.write(s)  
        f.close()

    def savedLast(self):
        f = open("entries.txt", "r")
        try: 
            lines = f.readlines()
            f.close()
            return lines[-1].split(';')
        except IndexError:
            return []

    def delete(self):
        f = open("entries.txt", "r")
        lines = f.readlines()
        f.close()
        f = open("entries.txt", "w")
        for l in lines[:-1]:
            f.write(l)
        f.close()



class ThirdWindow(Screen):
        

    def __init__(self, **kwargs):
        super(ThirdWindow, self).__init__(**kwargs)

        f = open("entries.txt", "r")
        lines = f.readlines()
        f.close()

        self.btn0 = [None]*10
        self.btn1 = [None]*10
        self.btn2 = [None]*10
        self.btn3 = [None]*10
        self.btn4 = [None]*10
        

        for i in range(10):
            if i < len(lines):
                line = lines[-(i+1)].split(';')
            else: line = ['']*5
            col = 1,0,0,1
            self.btn0[i] = Button(text= line[0] , size_hint=(.15, .05), pos_hint={'x': .05, 'y': .7-.07*i}, background_color = col)
            self.btn0[i].bind(width = self.resize_text1)
            self.add_widget(self.btn0[i])
            self.btn1[i] = Button(text= line[1] , size_hint=(.15, .05), pos_hint={'x': .22, 'y': .7-.07*i}, background_color = col)
            self.btn1[i].bind(width = self.resize_text1)
            self.add_widget(self.btn1[i])
            self.btn2[i] = Button(text= line[2] , size_hint=(.15, .05), pos_hint={'x': .39, 'y': .7-.07*i}, background_color = col)
            self.btn2[i].bind(width = self.resize_text1)
            self.add_widget(self.btn2[i])
            self.btn3[i] = Button(text= line[3] , size_hint=(.08, .05), pos_hint={'x': .56, 'y': .7-.07*i}, background_color = col)
            self.btn3[i].bind(width = self.resize_text2)
            self.add_widget(self.btn3[i])
            self.btn4[i] = Button(text= line[4] , size_hint=(.29, .05), pos_hint={'x': .66, 'y': .7-.07*i}, background_color = col)
            self.btn4[i].bind(width = self.resize_text3)
            self.add_widget(self.btn4[i])
    
    def resize_text1(self,label, new_width):
        label.font_size = 0.16*label.width

    def resize_text2(self,label, new_width):
        label.font_size = 0.32*label.width

    def resize_text3(self,label, new_width):
        label.font_size = 0.08*label.width


    def refresh(self):
        f = open("entries.txt", "r")
        lines = f.readlines()
        f.close()

        endParts = ['']*10
        for i in range(10):
            if i < len(lines): endParts[i] = lines[-(i+1)].split(';')[4]
            else: endParts[i] = ''

        for i in range(10):
            if i < len(lines):
                line = lines[-(i+1)].split(';')
            else: line = ['']*5
            col = 1,0,0,1
            if line[1] == 'Income': col = 0,1,0,1
            elif line[1] == 'Food': col = 0.8,0,0,1
            elif line[1] == 'Bills': col = 1,0.6,0,1
            elif line[1] == 'Clothing': col = 0,0.5,0.5,1
            elif line[1] == 'Education': col = 0.7,0,0.7,1
            elif line[1] == 'Health': col = 0,0.4,0.8,1
            elif line[1] == 'Fun': col = 0.9,0.3,0.2,1
            self.btn0[i].text = line[0]
            self.btn0[i].background_color = col
            self.btn1[i].text = line[1]
            self.btn1[i].background_color = col
            self.btn2[i].text = line[2]
            self.btn2[i].background_color = col
            self.btn3[i].text = line[3]
            self.btn3[i].background_color = col
            self.btn4[i].text = twenty(line[4])
            self.btn4[i].background_color = col
            if line[4] == '': self.btn4[i].text = ''

class FourthWindow(Screen):
    incD = ObjectProperty(None)

    def dateValid(self,day,month,year):
        ten = ['0','1','2','3','4','5','6','7','8','9']
        if any([d not in ten for d in day]): return False
        if any([m not in ten for m in month]): return False
        if any([y not in ten for y in year]): return False
        try:
            newDate = datetime.datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    def dater(self,day,month,year):
        result = datetime.datetime(int(year), int(month), int(day))
        return result


    def getSum(self,From,To,category,currency):
        f = open("entries.txt", "r")
        lines = f.readlines()
        f.close()
        
        result = 0
        for line in lines:
            ls = line.split(';')
            d = ls[0].split('-')
            date = datetime.datetime(int(d[2]),int(d[1]),int(d[0]))
            if ls[1] == category and ls[3] == currency and date >= From and date <= To:
                result += float(ls[2])
        return str(round(result,1))

    def getAll(self,From,To):
    
        self.incD.text = self.getSum(From,To,'Income','Dollar')
        self.incE.text = self.getSum(From,To,'Income','Euro')
        self.incL.text = self.getSum(From,To,'Income','Lira')
        self.fooD.text = self.getSum(From,To,'Food','Dollar')
        self.fooE.text = self.getSum(From,To,'Food','Euro')
        self.fooL.text = self.getSum(From,To,'Food','Lira')
        self.bilD.text = self.getSum(From,To,'Bills','Dollar')
        self.bilE.text = self.getSum(From,To,'Bills','Euro')
        self.bilL.text = self.getSum(From,To,'Bills','Lira')
        self.cloD.text = self.getSum(From,To,'Clothing','Dollar')
        self.cloE.text = self.getSum(From,To,'Clothing','Euro')
        self.cloL.text = self.getSum(From,To,'Clothing','Lira')
        self.eduD.text = self.getSum(From,To,'Education','Dollar')
        self.eduE.text = self.getSum(From,To,'Education','Euro')
        self.eduL.text = self.getSum(From,To,'Education','Lira')
        self.heaD.text = self.getSum(From,To,'Health','Dollar')
        self.heaE.text = self.getSum(From,To,'Health','Euro')
        self.heaL.text = self.getSum(From,To,'Health','Lira')
        self.entD.text = self.getSum(From,To,'Fun','Dollar')
        self.entE.text = self.getSum(From,To,'Fun','Euro')
        self.entL.text = self.getSum(From,To,'Fun','Lira')


def twenty(text):
    l = len(text) 
    if l <= 20: return text
    else: return text[:19]+'**'
        
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('bud.kv')


class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
import time
#from kivy.graphics import canvas, Rectangle


class Stuff(FloatLayout):
    def animate_the_widget(self,widget,*args):
        anim=Animation(this=0,duration=.2)
        anim.start(widget)

    def animate_the_button(self,widget,*args):
    	anim = Animation(opacity = 0,duration = 0)
    	anim.start(widget)
        
    def animate_the_widget1(self,widget,*args):
        anim=Animation(tim=0.6,duration=.4)
        anim.start(widget)
        
    def animate_the_widget2(self,widget,*args):
        anim=Animation(that=0.8,duration=.6)
        anim.start(widget)  
        time.sleep(0.1)

    def animate_the_widget3(self,widget,*args):
        anim=Animation(th=0.4,duration=.2)
        anim.start(widget) 

    def animate_the_widget4(self,widget,*args):
        anim=Animation(tom=0.2,duration=.4)
        anim.start(widget) 

    def animate_the_widget5(self,widget,*args):
        anim=Animation(tam=0,duration=.6)
        anim.start(widget)
        time.sleep(0.1)
    def animate_the_widget6(self,widget,*args):
        anim=Animation(tbm=0.4,duration=.2)
        anim.start(widget)  
              
    def animate_the_widget7(self,widget,*args):
        anim=Animation(tcm=0.8,duration=.4)
        anim.start(widget) 

    def animate_the_widget8(self,widget,*args):
        anim=Animation(tdm=0.2,duration=.6)
        anim.start(widget) 
        time.sleep(0.1)
    def animate_the_widget9(self,widget,*args):
        anim=Animation(tem=0.6,duration=.2)
        anim.start(widget)
        
    def animate_the_widget10(self,widget,*args):
        anim=Animation(tfm=0,duration=.4)
        anim.start(widget)  
              
    def animate_the_widget11(self,widget,*args):
        anim=Animation(tgm=0.4,duration=.6)
        anim.start(widget)
        time.sleep(0.1) 

    def animate_the_widget12(self,widget,*args):
        anim=Animation(thm=0.8,duration=.2)
        anim.start(widget) 

    def animate_the_widget13(self,widget,*args):
        anim=Animation(tjm=0.2,duration=.4)
        anim.start(widget)
        
    def animate_the_widget14(self,widget,*args):
        anim=Animation(tkm=0.6,duration=.6)
        anim.start(widget)  
        time.sleep(0.1)
    def animate_the_widget15(self,widget,*args):
        anim=Animation(tlm=0,duration=.2)
        anim.start(widget) 

    def animate_the_widget16(self,widget,*args):
        anim=Animation(tmm=0.4,duration=.4)
        anim.start(widget) 

    def animate_the_widget17(self,widget,*args):
        anim=Animation(tnm=0.8,duration=.6)
        anim.start(widget)
        time.sleep(0.1)
    def animate_the_widget18(self,widget,*args):
        anim=Animation(tpm=0.2,duration=.2)
        anim.start(widget)  
              
    def animate_the_widget19(self,widget,*args):
        anim=Animation(tqm=0.6,duration=.4)
        anim.start(widget) 

    def animate_the_widget20(self,widget,*args):
        anim=Animation(trm=0,duration=.6)
        anim.start(widget) 
        time.sleep(0.1)
    def animate_the_widget21(self,widget,*args):
        anim=Animation(tsm=0.4,duration=.2)
        anim.start(widget)
        
    def animate_the_widget22(self,widget,*args):
        anim=Animation(ttm=0.8,duration=.4)
        anim.start(widget)  
              
    def animate_the_widget23(self,widget,*args):
        anim=Animation(tum=0.2,duration=.6)
        anim.start(widget) 
        time.sleep(0.1)
    def animate_the_widget24(self,widget,*args):
        anim=Animation(tvm=0.6,duration=.2)
        anim.start(widget) 


this = """

    
Stuff:
    
        
      #  Button:
    #        text:"hello"
    
    GridLayout:
        id:stuff
        size_hint:.2,.1
        this:-.5
        pos_hint:{"x":self.this,"top":1}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos     
    Button:
        text:"hello"
        size_hint:.3,.3
        pos_hint:{"x":0,"top":0.5}  
        on_release:
            root.animate_the_widget(stuff)
            root.animate_the_widget1(stuff4)
            root.animate_the_widget2(stuff1)
            root.animate_the_widget3(stuff2)
            root.animate_the_widget4(stuff3)
            root.animate_the_widget5(stuff5)
            root.animate_the_widget6(stuff6)
            root.animate_the_widget7(stuff7)
            root.animate_the_widget8(stuff8)
            root.animate_the_widget9(stuff9)
            root.animate_the_widget10(stuff10)
            root.animate_the_widget11(stuff11)
            root.animate_the_widget12(stuff12)
            root.animate_the_widget13(stuff13)
            root.animate_the_widget14(stuff14)
            root.animate_the_widget15(stuff15)
            root.animate_the_widget16(stuff16)
            root.animate_the_widget17(stuff17)
            root.animate_the_widget18(stuff18)
            root.animate_the_widget19(stuff19)
            root.animate_the_widget20(stuff20)
            root.animate_the_widget21(stuff21)
            root.animate_the_widget22(stuff22)
            root.animate_the_widget23(stuff23)
            root.animate_the_widget24(stuff24)
            root.animate_the_button(self)
  
  
 
  
  
 #   FloatLayout: #for chess pieces to move and be ontop ofthe chess board
  #      size:root.width,root.height
  #      Button:
       #     size_hint:.3,.3
          #  pos_hint:{"x":0,"top":1}
         #   text:"hello"    
    GridLayout:
        id:stuff1
        that:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.that,"top":1}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos   
                
                
                
    GridLayout:
        id:stuff2
        th:-.5
        size_hint:.2,.1
        #0.4
        pos_hint:{"x":self.th,"top":1}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos  
                
                
    GridLayout:
        id:stuff3
        tom:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tom,"top":.9}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos 
                
                
                
    GridLayout:
        id:stuff4
        tim:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tim,"top":.9}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos                                                       

    GridLayout:
        id:stuff5
        tam:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tam,"top":.8}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff6
        tbm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tbm,"top":.8}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos
                
    GridLayout:
        id:stuff7
        tcm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tcm,"top":.8}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos                                          
                
    GridLayout:
        id:stuff8
        tdm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tdm,"top":.7}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             


    GridLayout:
        id:stuff9
        tem:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tem,"top":.7}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos   
                
                
                
    GridLayout:
        id:stuff10
        tfm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tfm,"top":.6}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos   
                
                
                
    GridLayout:
        id:stuff11
        tgm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tgm,"top":.6}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             
                
    GridLayout:
        id:stuff12
        thm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.thm,"top":.6}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos                                                                                 

    GridLayout:
        id:stuff13
        tjm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tjm,"top":.5}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             


    GridLayout:
        id:stuff14
        tkm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tkm,"top":.5}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             


    GridLayout:
        id:stuff15
        tlm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tlm,"top":.4}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff16
        tmm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tmm,"top":.4}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             



    GridLayout:
        id:stuff17
        tnm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tnm,"top":.4}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff18
        tpm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tpm,"top":.3}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff19
        tqm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tqm,"top":.3}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff20
        trm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.trm,"top":.2}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             


    GridLayout:
        id:stuff21
        tsm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tsm,"top":.2}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff22
        ttm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.ttm,"top":.2}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff23
        tum:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tum,"top":.1}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             

    GridLayout:
        id:stuff24
        tvm:-.5
        size_hint:.2,.1
        pos_hint:{"x":self.tvm,"top":.1}
        
        cols:1
        
        canvas:    
            Color:
                rgb:(1,1,1)
            Rectangle:
                size:self.size    
                pos:self.pos             


"""    




kv = Builder.load_string(this)
class TestApp(App):
    def build(self):
        return kv
TestApp().run()

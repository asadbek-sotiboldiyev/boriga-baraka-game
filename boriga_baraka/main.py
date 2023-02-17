# ====   AsAdbEk_Sotiboldiyev    ====
# ==== t.me/asadbef_sotiboldiyev ====
# ========== BORIGA BARAKA ==========

from tkinter import*
from tkinter import messagebox
import random

win_c=0 # necha marta oyna ochilganini snab boradi

def game():
	"""O'yin boshlanish funksiyasi"""
	global a,win_c,buttons,window #o'zgaruvchilarni global qilish
	if win_c>0:
		window.destroy()
	win_c+=1
	window=Tk()
	window.config(bg="blue")

	# o'yin nomiuchun banner Frame
	banner=Frame(window,bg="blue")
	banner.pack(anchor=N)

	banner_l=Label(banner,text="BORIGA BARAKA",font=("supercell-magic",35,"underline"),bg="blue",fg="white")
	banner_l.pack(side=LEFT,padx=20)
	restart=Button(banner,text="RESTART",state=DISABLED,cursor="hand2",bg="blue",relief=SOLID,fg="white",font=("supercell-magic",20))
	restart.pack(side=RIGHT)

	# Asosiy Frame
	root=Frame(window,bg="aqua",relief=SOLID,bd=3)
	root.pack(anchor=CENTER,pady=40,padx=20)

	# Tugmalar uchun Frame
	tugma_frame=Frame(root,bg="aqua")
	tugma_frame.pack(side=LEFT)

	fontt=('sans-serif',14) # standart FONT

	sovga_frame=Frame(root,bg="cyan")
	sovga_frame.pack(side=RIGHT)

	sovgalar=["GUGURT","SALFETKA","LAMPOCHKA","VAZA","TELEFON","BLENDER","NONPISHIRGICH","MIKROTO'LQINLI PECH","CHANG YUTGICH","PLANSHET","GAZ PLITA","KOMPYUTER","TELEVIZOR","KIR YUVISH MASHINASI","MUZLATGICH","YUMSHOQ MEBEL","AKFA MEDLINE\nVAUCHER","LADA VESTA SW CROSS","COBALT","2 XONALI UY"]

	# sovg'alar ro'xati(LABEL)
	s04=Label(sovga_frame,text=sovgalar[0],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s04.grid(row=0,column=4,pady=2,padx=2)
	s14=Label(sovga_frame,text=sovgalar[1],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s14.grid(row=1,column=4,pady=2,padx=2)
	s24=Label(sovga_frame,text=sovgalar[2],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s24.grid(row=2,column=4,pady=2,padx=2)
	s34=Label(sovga_frame,text=sovgalar[3],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s34.grid(row=3,column=4,pady=2,padx=2)
	s44=Label(sovga_frame,text=sovgalar[4],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s44.grid(row=4,column=4,pady=2,padx=2)
	s54=Label(sovga_frame,text=sovgalar[5],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s54.grid(row=5,column=4,pady=2,padx=2)
	s64=Label(sovga_frame,text=sovgalar[6],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s64.grid(row=6,column=4,pady=2,padx=2)
	s74=Label(sovga_frame,text=sovgalar[7],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s74.grid(row=7,column=4,pady=2,padx=2)
	s84=Label(sovga_frame,text=sovgalar[8],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s84.grid(row=8,column=4,pady=2,padx=2)
	s94=Label(sovga_frame,text=sovgalar[9],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s94.grid(row=9,column=4,pady=2,padx=2)

	s05=Label(sovga_frame,text=sovgalar[10],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s05.grid(row=0,column=5,pady=2,padx=2)
	s15=Label(sovga_frame,text=sovgalar[11],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s15.grid(row=1,column=5,pady=2,padx=2)
	s25=Label(sovga_frame,text=sovgalar[12],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s25.grid(row=2,column=5,pady=2,padx=2)
	s35=Label(sovga_frame,text=sovgalar[13],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s35.grid(row=3,column=5,pady=2,padx=2)
	s45=Label(sovga_frame,text=sovgalar[14],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s45.grid(row=4,column=5,pady=2,padx=2)
	s55=Label(sovga_frame,text=sovgalar[15],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s55.grid(row=5,column=5,pady=2,padx=2)
	s65=Label(sovga_frame,text=sovgalar[16],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s65.grid(row=6,column=5,pady=2,padx=2)
	s75=Label(sovga_frame,text=sovgalar[17],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s75.grid(row=7,column=5,pady=2,padx=2)
	s85=Label(sovga_frame,text=sovgalar[18],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s85.grid(row=8,column=5,pady=2,padx=2)
	s95=Label(sovga_frame,text=sovgalar[19],font=fontt,width=25,height=2,relief=SOLID,bg='coral')
	s95.grid(row=9,column=5,pady=2,padx=2)

	img=PhotoImage(file='yutuq.png')
	list0=[s04,s14,s24,s34,s44,s54,s64,s74,s84,s94,
	s05,s15,s25,s35,s45,s55,s65,s75,s85,s95]
	a=0
	def function(btn,index):
		global a,buttons
		a+=1

		# yugmani bosilmaydigan holatga o'tkazish
		btn.config(bg="orange",state=DISABLED)
		# a==19 bo'lsa o'yin yankunlanadi
		if a==19:
			messagebox.showinfo("YUTUQ...",f"Siz {sovgalar[index]}ni yutib oldingiz!")
			list0[index].config(bg="green")
			restart.config(state=NORMAL,command=game)
			for i in buttons:
				i.config(state=DISABLED)
		else:
			# aksincha bo'lsa davom etadi
			list0[index].config(text="",bg="blue")

	# sovg'alar tugmalarga RANDOM orqali taqsimlanadi
	indexlar=[int(i) for i in range(20)]
	random.shuffle(indexlar)

	# 1-ustun tugmalar
	b00=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b00,indexlar[0]))
	b10=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b10,indexlar[1]))
	b20=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b20,indexlar[2]))
	b30=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b30,indexlar[3]))
	b40=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b40,indexlar[4]))
	b00.grid(row=0,column=0,pady=5,padx=5)
	b10.grid(row=2,column=0,pady=5,padx=5)
	b20.grid(row=4,column=0,pady=5,padx=5)
	b30.grid(row=6,column=0,pady=5,padx=5)
	b40.grid(row=8,column=0,pady=5,padx=5)

	# 2-ustun tugmalar
	b01=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b01,indexlar[5]))
	b11=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b11,indexlar[6]))
	b21=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b21,indexlar[7]))
	b31=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b31,indexlar[8]))
	b41=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b41,indexlar[9]))
	b01.grid(row=0,column=1,pady=5,padx=5)
	b11.grid(row=2,column=1,pady=5,padx=5)
	b21.grid(row=4,column=1,pady=5,padx=5)
	b31.grid(row=6,column=1,pady=5,padx=5)
	b41.grid(row=8,column=1,pady=5,padx=5)
	# 3-ustun tugmalar
	b02=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b02,indexlar[10]))
	b12=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b12,indexlar[11]))
	b22=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b22,indexlar[12]))
	b32=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b32,indexlar[13]))
	b42=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b42,indexlar[14]))
	b02.grid(row=0,column=2,pady=5,padx=5)
	b12.grid(row=2,column=2,pady=5,padx=5)
	b22.grid(row=4,column=2,pady=5,padx=5)
	b32.grid(row=6,column=2,pady=5,padx=5)
	b42.grid(row=8,column=2,pady=5,padx=5)

	# 4-ustun tugmalar
	b03=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b03,indexlar[15]))
	b13=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b13,indexlar[16]))
	b23=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b23,indexlar[17]))
	b33=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b33,indexlar[18]))
	b43=Button(tugma_frame,bg="grey",image=img,command=lambda:function(b43,indexlar[19]))
	b03.grid(row=0,column=3,pady=5,padx=5)
	b13.grid(row=2,column=3,pady=5,padx=5)
	b23.grid(row=4,column=3,pady=5,padx=5)
	b33.grid(row=6,column=3,pady=5,padx=5)
	b43.grid(row=8,column=3,pady=5,padx=5)

	# tugmalar ro'yxati shakllantiriladi
	buttons=[b00,b10,b20,b30,b40,b01,b11,b21,b31,b41,b02,b12,b22,b32,b42,b03,b13,b23,b33,b43]

	window.mainloop()
# dastur ishga tushadi
game()
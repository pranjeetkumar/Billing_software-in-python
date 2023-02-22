from cProfile import label
from distutils.command.config import config
from fileinput import filename
from this import s
from tkinter import *
from tkinter import ttk
from tokenize import String
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1530x800+0+0")
        #==============================Variables=============================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000,10000)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        #Product Categories list
        self.Category = ["Select option",'Clothing','Lifestyle','Mobiles']

        #SubCatClothing
        self.SubCatClothing = ["Pant","T-Shirt","Shirt"]
        self.pant = ["Lewis","Mufti","Spykar"]
        self.price_lewis = 5000
        self.price_mufti = 700
        self.price_spykar = 8000

        self.T_Shirt = ['Polo','RoadStar','Jack&Jones']
        self.price_polo = 1500
        self.price_Roadstar = 1800
        self.price_JackJones = 1700

        self.Shirt = ['Peter','Louis Phillipe','Park Avenue']
        self.price_Peter = 2100
        self.price_Louis = 2700
        self.price_Park = 1740

        # Life Style
        self.SubCatLifeStyle = ["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_soap = ['Lifebuy','Lux','Santoor','Pearl']
        self.price_life = 20
        self.price_lux =20
        self.price_santoor =20
        self.price_pearl = 30

        self.Face_Cream = ['Fair & Lovely','Ponds','Olay','Garnier']
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30

        self.Hair_oil = ["Parachute",'Jasmine','Bajaj']
        self.price_para = 25
        self.price_jasmine = 22
        self.price_bajaj = 30

        # SubCatMobiles
        self.SubCatMobiles = ["iphone","samsung","Xiome",'realme',"oneplus"]
        self.Iphone = ['iphone x','iphone 11','iphone 12']
        self.price_ix = 40000
        self.price_i11 = 60000
        self.price_i12 = 85000

        self.samsung = ['samsung M31','sumsung F23','samsung F12']
        self.price_sm31 =16000
        self.price_sf23 = 20000
        self.price_sf12 = 13000

        self.xiome = ['redmi 10','redmi 11','redmi pro']
        self.price_r10 = 11000
        self.price_r11 = 12000
        self.price_rpro = 18000

        self.realme = ['realme 12','realme 13','realme pro']
        self.price_rel12 = 21000
        self.price_rel13 = 25000
        self.price_relpro = 30000

        self.OnePlus = ['oneplus1','oneplus2','oneplus3']
        self.price_One1 = 38000
        self.price_One2 = 45000
        self.price_One3 = 54000 



        #image 1
        img = Image.open(r"D:\Visual Studio Code\Python Projects\Billing_Software\image\img1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root,image = self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height = 130)



        # image 2
        img_1 = Image.open(r"D:\Visual Studio Code\Python Projects\Billing_Software\image\img2.jpg")
        img_1 = img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.root,image = self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height = 130)



        # image 3
        img_2 = Image.open(r"D:\Visual Studio Code\Python Projects\Billing_Software\image\img3.jpg")
        img_2= img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root,image = self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=520,height = 130)


        lbl_title = Label(self.root,text="Welcome To A-Z Wholesale Store , Jalandhar",font=("times new roman",35,"bold"),bg="pink",fg="black")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font=('times new roman',16,'bold'),background= 'pink',foreground="black")
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame = Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)


        # Customer LabelFrame

        Cust_Frame = LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob = Label(Cust_Frame,text="Mobile No. : ",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

    

        self.lblCustName = Label(Cust_Frame,text="Customer Name : ",bd=4,font=("times new roman",12,"bold"),bg="white")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txtCustName = ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1)
        

        self.lblEmail = Label(Cust_Frame,font=("times new roman",12,"bold"),bg="white",text="Email :",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

         # Product LabelFrame

        Product_Frame = LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        # category
        self.lblcategory = Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories :",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value = self.Category,font=('arial',10,'bold'),width=24,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # subCategory
        self.lblSubCategory = Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Subcategory :",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory = ttk.Combobox(Product_Frame,value = [""],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name :",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.product,state='readonly',font=('arial',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        

        #price

        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price :",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame,state='readonly',textvariable=self.prices,font=('arial',10,'bold'),width=20)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # QTY

        self.lblQTY=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty :",bd=4)
        self.lblQTY.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty = ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=22)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        # Middle Frame

        MiddleFrame = Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #image 1
        img12 = Image.open(r"D:\Visual Studio Code\Python Projects\Billing_Software\image\img1.jpg")
        img12 = img12.resize((490,340),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lbl_img12 = Label(MiddleFrame,image = self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height = 340)



        # image 2
        img_13 = Image.open(r"D:\Visual Studio Code\Python Projects\Billing_Software\image\img2.jpg")
        img_13 = img_13.resize((490,340),Image.ANTIALIAS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(MiddleFrame,image = self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=500,height = 340)



        # search

        Search_Frame = Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)


        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg="red",fg="white",text="Bill Number :")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=22)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSerach = Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnSerach.grid(row=0,column=2)

        

        # Right Frame Bill area

        RightLabelFrame = LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y = Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea = Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
    
        # Bill counter label frame
        Bottom_Frame = LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

       # self.subtotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Sub Total :",bd=4)
       # self.subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        #self.entrytotal = ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22)
        #self.entrytotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

       # self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Govt. Tax :",bd=4)
        #self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        #self.txt_tax = ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22)
        #self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

       # self.lbl_Amount=Label(Bottom_Frame,font=('arial',12,'bold'),bg="white",text="Total :",bd=4)
       # self.lbl_Amount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #self.txtAmount = ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22)
        #self.txtAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)
    


        # Button Frame

        Btn_Frame = Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart = Button(Btn_Frame,height = 2,command=self.AddItem,text="Add To Cart",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Btngenerate_bill = Button(Btn_Frame,height = 2,command = self.gen_bill,text="Generate Bill",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.Btnsave = Button(Btn_Frame,height = 2,command=self.save_bill,text="Save Bill",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.Btnsave.grid(row=0,column=2)

        self.Btnprint = Button(Btn_Frame,height = 2,command=self.iprint,text="Print",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.Btnprint.grid(row=0,column=3)

        self.BtnClear= Button(Btn_Frame,height = 2,command=self.clear,text="Clear",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit = Button(Btn_Frame,height = 2,command=self.root.destroy,text="Exit",font=('arial',15,'bold'),bg="orange",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)


        self.welcome()
        self.l = []


    #=========================function declaration====================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome To A-Z Wholesale Store")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email :{self.c_email.get()}")

        self.textarea.insert(END,"\n ================================================")
        self.textarea.insert(END,f'\n Products\t\t\tQTY\t\tPrice')
        self.textarea.insert(END,"\n ================================================\n")



    def AddItem(self):
        Tax = 1
        self.n=self.prices.get()
        self.m = self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get() == " ":
            messagebox.showerror("Error","Please select product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()==" ":
            messagebox.showerror("Error","Please Add to card Product")
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ===============================================")
            self.textarea.insert(END,f"\n Sub Amount : \t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount : \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount : \t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ===============================================")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1 = open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            messagebox.showinfo("saved bill",f" Bill no. :{self.bill_no.get()} Saved successfully")
            f1.close()

    def iprint(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found = 'yes'
        if found =='no':
            messagebox.showerror("Error","Invalid Bill No.")

    

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()



    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(values=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Lifestyle":
            self.ComboSubCategory.config(values=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(values=self.SubCatMobiles)
            self.ComboSubCategory.current(0)
    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(values=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(values=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(values=self.Shirt)
            self.ComboProduct.current(0)

        # LifeStyle

        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_Cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)



        # Mobile
        if self.ComboSubCategory.get()=="iphone":
            self.ComboProduct.config(value = self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="samsung":
            self.ComboProduct.config(value=self.samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="oneplus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="realme":
            self.ComboProduct.config(value=self.realme)
            self.ComboProduct.current(0)


    def price(self,event = " "):

        # pant

        if self.ComboProduct.get() == "Lewis":
            self.ComboPrice.config(value = self.price_lewis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Mufti":
            self.ComboPrice.config(value = self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Spykar":
            self.ComboPrice.config(value = self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-Shirt

        if self.ComboProduct.get() =="Polo":
            self.ComboPrice.config(value = self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RoadStar":
            self.ComboPrice.config(value = self.price_Roadstar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jack&Jones":
            self.ComboPrice.config(value = self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        # Shirts
        if self.ComboProduct.get() == "Peter":
            self.ComboPrice.config(value = self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Louis Phillipe":
            self.ComboPrice.config(value = self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Park Avenue":
            self.ComboPrice.config(value = self.price_lewis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        

        # Bath Soap
        if self.ComboProduct.get() == "Lifebuy":
            self.ComboPrice.config(value = self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(value = self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Santoor":
            self.ComboPrice.config(value = self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Pearl":
            self.ComboPrice.config(value = self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get() == "Fair & Lovely":
            self.ComboPrice.config(value = self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(value = self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Olay":
            self.ComboPrice.config(value = self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Garnier":
            self.ComboPrice.config(value = self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(value = self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jasmine":
            self.ComboPrice.config(value = self.price_jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Bajaj":
            self.ComboPrice.config(value = self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "iphone x":
            self.ComboPrice.config(value = self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "iphone 11":
            self.ComboPrice.config(value = self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "iphone 12":
            self.ComboPrice.config(value = self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "samsung M31":
            self.ComboPrice.config(value = self.price_sm31)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "samsung F23":
            self.ComboPrice.config(value = self.price_sf23)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "samsung F12":
            self.ComboPrice.config(value = self.price_sf12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get() == "redmi 10":
            self.ComboPrice.config(value = self.price_r10)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "redmi 11":
            self.ComboPrice.config(value = self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "redmi pro":
            self.ComboPrice.config(value = self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "realme 12":
            self.ComboPrice.config(value = self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "realme 13":
            self.ComboPrice.config(value = self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "realme pro":
            self.ComboPrice.config(value = self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "oneplus1":
            self.ComboPrice.config(value = self.price_One1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "oneplus2":
            self.ComboPrice.config(value = self.price_One2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "oneplus3":
            self.ComboPrice.config(value = self.price_One3)
            self.ComboPrice.current(0)
            self.qty.set(1)



if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
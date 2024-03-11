from tkinter import *
from tkinter.ttk import Combobox

From=Tk()
From.geometry("800x600")

R2Value=StringVar()
txModal=StringVar()

def NewData():
    from sklearn.datasets import make_blobs
    x,y=make_blobs(n_samples=1000,n_features=2,centers=3)
    global z1
    global z2
    z1=x
    z2=y
def NewDataMoon():
    from sklearn.datasets import make_moons
    x, y = make_moons(n_samples=1000)
    global z1
    global z2
    z1=x
    z2=y

def NewDataCircle():
    from sklearn.datasets import make_circles
    x, y = make_circles(n_samples=1000)
    global z1
    global z2
    z1=x
    z2=y

def Action():
    global z3
    global z4
    global z5

    x=z1
    y=z2
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    modal2=txModal.get()
    match modal2:
        case "MLPClassifier":
            modal=MLPClassifier()
        case "DecisionTreeClassifier":
            modal = DecisionTreeClassifier()
        case "SVM":
            modal = SVC(kernel="linear")
        case "Naive_bays":
            modal = GaussianNB()

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.33)
    modal.fit(xtrain,ytrain)
    r=modal.score(xtest,ytest)
    ypred=modal.predict(xtest)
    R2Value.set(r)

    z3=xtrain
    z4=ytrain
    z5=modal

def plot():
    import matplotlib.pyplot as plt
    from mlxtend.plotting import plot_decision_regions
    plot_decision_regions(z3,z4,clf=z5)
    plt.show()

frame=LabelFrame(From)

labal1=Label(frame,text="Generate Linear Data")
labal1.grid(row=0,column=0,padx=10,pady=10)

GenerateButton1=Button(frame,text="Enter For Data Linear Generation Randomly",width=40,command=NewData)#command=NewData
GenerateButton1.grid(row=1,column=0,padx=15,pady=15)

labal2=Label(frame,text="Generate moon Data")
labal2.grid(row=2,column=0,padx=10,pady=10)
GenerateButton2=Button(frame,text="Enter For Data moon generation",width=40,command=NewDataMoon)#command=NewDataMoon
GenerateButton2.grid(row=3,column=0,padx=15,pady=15)

labal3=Label(frame,text="Generate Circle data")
labal3.grid(row=4,column=0,padx=10,pady=10)
GenerateButton3=Button(frame,text="Enter For Data circle generation",width=40,command=NewDataCircle)#command=NewDataCircle
GenerateButton3.grid(row=5,column=0,padx=15,pady=15)

labal4=Label(frame,text="Select Method")
labal4.grid(row=6,column=0,padx=10,pady=10)

entModal=Combobox(frame,textvariable=txModal,width=20,state="readonly")#textvariable=txtModal
entModal.grid(row=7,column=0,padx=15,pady=15)
entModal['values']=['MLPClassifier','DecisionTreeClassifier','SVM','Naive_bays']

frame.place(x=20,y=20)

frame2=LabelFrame(From)
ActionButton=Button(frame2,text="Enter your implementation",width=35,command=Action)
ActionButton.grid(row=0,column=0,padx=10,pady=10)

labal2=Label(frame2,text="R2 Value")
labal2.grid(row=1,column=0,padx=10,pady=10)

entryR2=Entry(frame2,textvariable=R2Value,width=10)#textvariable=R2Value
entryR2.grid(row=2,column=0,padx=10,pady=10)

labal3=Label(frame2,text="Plot Diagram")
labal3.grid(row=3,column=0,padx=10,pady=10)

DiagramButton=Button(frame2,text="Enter for Plotting",width=35,command=plot)#command=plot
DiagramButton.grid(row=4,column=0,padx=10,pady=10)

frame2.place(x=450,y=20)

From.mainloop()



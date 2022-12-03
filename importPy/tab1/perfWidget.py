from tkinter import *
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

LS = 0
BS = 1
CS = 2
RS = 3

class PerfWidget():
    def __init__(self, root, cbIdx, i, frame, perf, decryptFile, varList, btnList, defaultData):
        self.root = root
        self.cbIdx = cbIdx
        self.decryptFile = decryptFile
        self.varList = varList
        self.btnList = btnList
        self.defaultData = defaultData
        
        self.perfNameLb = Label(frame, text=self.decryptFile.trainPerfNameList[i], font=("", 20), width=24, borderwidth=1, relief="solid")
        self.perfNameLb.grid(row=i, column=0, sticky=W+E)
        self.varPerf = DoubleVar()
        self.varPerf.set(str(perf[i]))
        self.varList.append(self.varPerf)
        self.perfLb = Label(frame, textvariable=self.varPerf, font=("", 20), width=7, borderwidth=1, relief="solid")
        self.perfLb.grid(row=i, column=1, sticky=W+E)
        self.perfBtn = Button(frame, text="修正", font=("", 14), command=lambda:self.editVar([self.perfNameLb, self.perfLb], self.varPerf, self.varPerf.get(), self.defaultData[self.cbIdx]["att"][i]), state="disabled")
        self.perfBtn.grid(row=i, column=2, sticky=W+E)
        self.btnList.append(self.perfBtn)

        color = ""
        if self.defaultData[self.cbIdx]["att"][i] < perf[i]:
            color = "red"
        elif self.defaultData[self.cbIdx]["att"][i] > perf[i]:
            color = "blue"
        else:
            color = "black"
        self.perfNameLb["fg"] = color
        self.perfLb["fg"] = color

    def editVar(self, labelList, var, value, defaultValue, flag = False):
        EditPerfVarInfo(self.root, "値変更", labelList, var, value, defaultValue, flag)

class PerfHurikoWidget():
    def __init__(self, root, cbIdx, i, perfCnt, frame, huriko, decryptFile, varList, btnList, defaultData):
        self.root = root
        self.cbIdx = cbIdx
        self.decryptFile = decryptFile
        self.varList = varList
        self.btnList = btnList
        self.defaultData = defaultData
        
        self.hurikoNameLb = Label(frame, text=self.decryptFile.trainHurikoNameList[i], font=("", 20), width=24, borderwidth=1, relief="solid")
        self.hurikoNameLb.grid(row=perfCnt+i, column=0, sticky=W+E)
        self.varHuriko = IntVar()
        self.varHuriko.set(str(huriko[i]))
        self.varList.append(self.varHuriko)
        self.hurikoLb = Label(frame, textvariable=self.varHuriko, font=("", 20), width=7, borderwidth=1, relief="solid")
        self.hurikoLb.grid(row=perfCnt+i, column=1, sticky=W+E)
        self.hurikoBtn = Button(frame, text="修正", font=("", 14), command=lambda:self.editVar([self.hurikoNameLb, self.hurikoLb], self.varHuriko, self.varHuriko.get(), self.defaultData[self.cbIdx]["huriko"][i]), state="disabled")
        self.hurikoBtn.grid(row=perfCnt+i, column=2, sticky=W+E)
        self.btnList.append(self.hurikoBtn)

        color = ""
        if self.defaultData[self.cbIdx]["huriko"][i] < huriko[i]:
            color = "red"
        elif self.defaultData[self.cbIdx]["huriko"][i] > huriko[i]:
            color = "blue"
        else:
            color = "black"
        self.hurikoNameLb["fg"] = color
        self.hurikoLb["fg"] = color

    def editVar(self, labelList, var, value, defaultValue, flag = True):
        EditPerfVarInfo(self.root, "値変更", labelList, var, value, defaultValue, flag)

class EditPerfVarInfo(sd.Dialog):
    def __init__(self, master, title, labelList, var, value, defaultValue, flag = False):
        self.labelList = labelList
        self.var = var
        self.value = value
        self.defaultValue = defaultValue
        self.flag = flag
        super(EditPerfVarInfo, self).__init__(parent=master, title=title)

    def body(self, frame):
        self.defaultLb = Label(frame, text="デフォルトの値＝" + str(self.defaultValue), font=("", 14))
        self.defaultLb.pack()

        sep = ttk.Separator(frame, orient='horizontal')
        sep.pack(fill=X, ipady=5)

        self.inputLb = Label(frame, text="値を入力してください", font=("", 14))
        self.inputLb.pack()

        v_val = StringVar()
        v_val.set(self.value)
        self.inputEt = Entry(frame, textvariable=v_val, font=("", 14))
        self.inputEt.pack()

    def validate(self):
        result = self.inputEt.get()
        if result:
            try:
                if self.flag:
                    try:
                        result = int(result)
                        if result < 0:
                            errorMsg = "0以上の整数で入力してください。"
                            mb.showerror(title="整数エラー", message=errorMsg)
                            return False
                        self.var.set(result)
                    except:
                        errorMsg = "整数で入力してください。"
                        mb.showerror(title="整数エラー", message=errorMsg)
                        return False
                else:
                    try:
                        result = float(result)
                        self.var.set(result)
                    except:
                        errorMsg = "数字で入力してください。"
                        mb.showerror(title="数字エラー", message=errorMsg)
                        return False
            except Exception:
                errorMsg = "予想外のエラーです"
                mb.showerror(title="エラー", message=errorMsg)
                return False

            if self.defaultValue != None:
                color = ""
                if self.defaultValue < result:
                    color = "red"
                elif self.defaultValue > result:
                    color = "blue"
                else:
                    color = "black"

                for label in self.labelList:
                    label["fg"] = color
            return True

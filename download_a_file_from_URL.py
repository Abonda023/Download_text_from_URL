from turtle import up
import urllib.request
import bs4
from tkinter import CENTER, DISABLED, END, HORIZONTAL, NS, LEFT, TOP, Tk, Label, Button, Entry, Variable, ttk, W, E, IntVar, Checkbutton
import operator
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



def get_words_from_url(url,progress,parameters):
    dictionary = {}

    index_page = urllib.request.urlopen(url) 
    page_data = bs4.BeautifulSoup(index_page, "html.parser")

    if( parameters[1]==1 ):
      progress['value']=0
      progress.grid(row = 5, column=0, columnspan=3,sticky=NS)

      for i in range(0,len(page_data.find_all(['p']))):
        split = page_data.find_all(['p'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['p']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1
            
      progress.grid_forget()
      

    if( parameters[2]== 1):
      progress['value']=0
      progress.grid(row = 5, column=0, columnspan=3,sticky=NS)
      for i in range(0,len(page_data.find_all(['a']))):
        split = page_data.find_all(['a'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['a']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress.grid_forget()

    

    if( parameters[0]== 1):
      progress['value']=0
      progress.grid(row = 5, column=0, columnspan=3,sticky=NS)
      for i in range(0,len(page_data.find_all(['h']))):
        split = page_data.find_all(['h'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h1']))):
        split = page_data.find_all(['h1'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h1']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h2']))):
        progress['value']=0
        

        split = page_data.find_all(['h2'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h2']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h3']))):
        split = page_data.find_all(['h3'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h3']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h4']))):
        split = page_data.find_all(['h4'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h4']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h5']))):
        split = page_data.find_all(['h5'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h5']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress['value']=0

      for i in range(0,len(page_data.find_all(['h6']))):
        split = page_data.find_all(['h6'])[i].text.split()
        progress['value'] = float(((i+1)/len(page_data.find_all(['h6']))*100))

        progress.update()

        for j in split:
          if j[len(j)-1] =="." or j[len(j)-1] == ",":
            j = j[:-1]
          if dictionary.get(j) is not None:
            dictionary[j] = dictionary[j] + 1

          else:
            dictionary[j] = 1

      progress.grid_forget()
      
    return dictionary

def count_of_words(dictionary):
  count= 0
  length = 0
  for i in range(0,len(dictionary.items())):
    length = length + dictionary[list(dictionary.keys())[i]] * len(list(dictionary.keys())[i])
    count = count + dictionary[list(dictionary.keys())[i]]
  length= length/count
  return count,length,list(dictionary.keys())[0]


class Gui(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("app")
    self.geometry("600x400")


    var_headers = IntVar()
    var_paragraphs = IntVar()
    var_links = IntVar()

    self.dictionary = {}
    self.parameters = []

    self.var_headers = var_headers
    self.var_paragraphs = var_paragraphs
    self.var_links = var_links


    self.columnconfigure(0, pad=3)
    self.columnconfigure(1, pad=3)
    self.rowconfigure(0, pad=3)
    self.rowconfigure(1, pad=3)

    self.entry = Entry(self,width = 80)
    self.entry.insert(END,"https://en.wikipedia.org/wiki/Python_(programming_language)")
  
    self.label = Label(self, text="Proszę podać adres strony", font=30, fg="black")
    self.button_url= Button(self,text="Pokaż statystyki", font=30, fg="black", command=self.button_url_click)
    self.button_statistic = Button(self, text="Drukuj", font = 30, command = self.print_statistic, state=DISABLED)
    self.progress_bar = ttk.Progressbar(self, orient=HORIZONTAL, length = 380, mode= "determinate")

    self.checkbox_headers=Checkbutton(self, text = "Nagłówki", variable=var_headers,onvalue=1, offvalue=0)
    self.checkbox_paragraphs=Checkbutton(self, text = "Akapity",variable=var_paragraphs,onvalue=1, offvalue=0)
    self.checkbox_links=Checkbutton(self,text = "Linki",variable=var_links,onvalue=1, offvalue=0)

    self.label_most_common_word_text = Label(self, text= "Najczęściej używane słowo: ",font=30 )
    self.label_count_of_words_text = Label(self, text= "Liczba słów: ",font=30 )
    self.label_Average_word_length_text = Label(self, text= "Średnia długość słowa: ",font=30 )

    self.label_most_common_word_value = Label(self,font=30 )
    self.label_count_of_words_value = Label(self,font=30 )
    self.label_Average_word_length_value = Label(self,font=30 )


    self.columnconfigure(0, weight=4)
    self.columnconfigure(1, weight=4)
    self.columnconfigure(2, weight=4)

    self.label.grid(row = 0, column=0, columnspan=3,sticky=NS)
    self.entry.grid(row = 1, column=0, columnspan=3,sticky=NS)

    self.checkbox_headers.grid(row = 2, column=0,sticky=NS)
    self.checkbox_paragraphs.grid(row = 2, column=1,sticky=NS)
    self.checkbox_links.grid(row = 2, column=2,sticky=NS)


    self.button_url.grid(row = 3, column=0, columnspan=3,sticky=NS)
    self.button_statistic.grid(row = 4, column=0, columnspan=3,sticky=NS)

   

    self.label_most_common_word_text.grid(row = 6, column=0,sticky=NS)
    self.label_most_common_word_value.grid(row = 6, column=1,sticky=NS)

    self.label_count_of_words_text.grid(row = 7, column=0,sticky=NS)
    self.label_count_of_words_value.grid(row = 7, column=1,sticky=NS)

    self.label_Average_word_length_text.grid(row = 8, column=0,sticky=NS)
    self.label_Average_word_length_value.grid(row = 8, column=1,sticky=NS)

    self.most_common_word = None
    self.median_word_length = None
    self.count_of_words = None
    self.average_word_length = None


  def button_url_click(self):
    self.parameters.clear()
    self.parameters.extend([self.var_headers.get(),self.var_paragraphs.get(),self.var_links.get()])
    self.button_statistic["state"]="normal"

    self.dictionary = get_words_from_url(self.entry.get(),self.progress_bar, self.parameters)
    self.dictionary = dict(sorted(self.dictionary.items(), key = operator.itemgetter(1), reverse=True ))
    self.count_of_words, self.average_word_length,self.most_common_word = count_of_words(self.dictionary)
    self.label_most_common_word_value['text'] = self.most_common_word
    self.label_count_of_words_value['text'] = self.count_of_words
    self.label_Average_word_length_value['text'] = str(round(self.average_word_length,2)) + " litery" 
  

  def print_statistic(self):
    data={'wyraz':self.dictionary.keys(), 'liczba wystapien':self.dictionary.values()}
    df = pd.DataFrame(data)
    print(df[['wyraz','liczba wystapien']])

    fig,ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,colLabels=df.columns,loc='center')

    pp = PdfPages("table.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()


    

def main():
    root = Gui()
    root.mainloop()
    

if __name__ == "__main__":
    main()
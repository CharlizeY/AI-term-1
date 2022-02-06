import numpy as np

def top5_bigram_frequency(filename):
   file_input = open(filename, "r")
   lines = file_input.read().lower()
   list_of_lines = lines.splitlines()
   
   bigrams = [b for l in list_of_lines for b in list(zip(l.split(" ")[:-1], l.split(" ")[1:]))]
   
   new_bigrams = []
   new_bigrams.extend([' '.join(bigram) for bigram in bigrams]) # use extend to add more than one element
      
   values, counts = np.unique(new_bigrams, return_counts=True)
   
   bigrams_dict = {}
   
   for i in np.argsort(-1*counts)[:5]: # use -1*counts to sort in descending order 
       bigrams_dict.update({values[i]: counts[i]})
       
   return bigrams_dict


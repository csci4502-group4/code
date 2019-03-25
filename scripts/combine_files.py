import pandas as pd 
import sys

"""
Usage: python3 combine_files.py <csv file> <csv file>
Example: python3 return_calc.py a.us.csv aa.us.csv
"""

def main(argv):
    
    # Correctly parse in the arguments
    file = pd.read_csv(argv[1])
    arg1 = argv[1]
    tag = arg1[:-4]
    file['Tag'] = tag
    
    file2 = pd.read_csv(argv[2])
    arg2 = argv[2]
    tag2 = arg2[:-4]
    file2['Tag'] = tag2
    
    # Create new DF and add two files into it
    new_file = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume','OpenInt','Tag'])
    new_file = pd.concat([new_file, file])
    new_file = pd.concat([new_file, file2])
    
    # Sort new DF
    new_file = new_file.sort_values(by=['Date'], ascending = False)
    
    name = tag + '_' + tag2 + '.csv'
    # Save new csv file
    new_file.to_csv(name)
    


if __name__ == '__main__':
    argv = sys.argv
    main(argv)

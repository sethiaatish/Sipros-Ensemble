'''
Created on Apr 29, 2016
Updated on July 26th, 2021 -- Part of turboPy Program

@author: Guo, Xuan
@author: Sethi, Aatish
'''

import argparse, os, sys
import platform

parser = argparse.ArgumentParser(description="Replace restricted characters in the protein description.",
                                 prog='restricted_char_remover.py',  # program name
                                 prefix_chars='-',  # prefix for options
                                 fromfile_prefix_chars='@',  # if options are read from file, '@args.txt'
                                 conflict_handler='resolve',  # for handling conflict options
                                 add_help=True,  # include help in the options
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter  # print default values for options in help message
                                 )
# # input files and directories
parser.add_argument("-i", "--input", help="target file/folder", dest='sInput', required=True)
# # process database
parser.add_argument("-f", help="target(s) is/are database", dest='bDatabase', default=False, action="store_true")
# # process sip file
parser.add_argument("-s", help="target(s) is/are sip file(s)", dest='bSip', default=False, action="store_true")
# # output files and directories
parser.add_argument("-o", "--out", help="output file/folder", dest='sOut', required=True)


def main(argv=None):
    # try to get arguments and error handling
    if argv is None:
        args = parser.parse_args()
    
    lInputList = []
    lOutList = []
    sLine = ""
    sInput = args.sInput
    sOut = args.sOut
    
    if args.bSip:
        if os.path.isfile(sInput):
            lInputList.append(sInput)
            lOutList.append(sOut)
        else:
            if platform.system() == 'Windows':
                if sInput[-1] != '\\':
                    sInput = sInput + '\\'
                if sOut[-1] != '\\':
                    sOut = sOut + '\\'
            else:
                if sInput[-1] != '/':
                    sInput = sInput + '/'
                if sOut[-1] != '/':
                    sOut = sOut + '/'
        for sFile in os.path.abspath(sInput):
            if sFile.endswith(".sip"):
                lInputList.append(sInput + sFile)
                lOutList.append(sOut + sFile)
        for iIndex, sFile in enumerate(lInputList):
            sys.stdout.write('Processing '+sFile)
            with open(sFile, 'r') as f:
                with open(lOutList[iIndex], 'w') as w:
                    while(1):
                        sLine = f.readline()
                        if not sLine:
                            break
                        if sLine[0] != '#':
                            if sLine.find('[') != -1 or sLine.find(']') != -1:
                                sLine = sLine.replace("[", "(")
                                sLine = sLine.replace("]", ")")
                            if sLine.find('{') != -1 or sLine.find('}') != -1:
                                sLine = sLine.replace('{', '(')
                                sLine = sLine.replace('}', ')')
                            if sLine.find('=') != -1:
                                sLine = sLine.replace('=', ' ')
                            if sLine.find('#') != -1:
                                sLine = sLine.replace('#', ' ')
                            if sLine.find('/') != -1:
                                sLine = sLine.replace('/', ' ')
                            if sLine.find('"') != -1:
                                sLine = sLine.replace('"', ' ')
                        w.write(sLine)
            sys.stdout.write(' -> Done\n')                            
        return
    
    
    if args.bDatabase:
        if os.path.isfile(sInput):
            lInputList.append(sInput)
            lOutList.append(sOut)
        else:
            if platform.system() == 'Windows':
                if sInput[-1] != '\\':
                    sInput = sInput + '\\'
                if sOut[-1] != '\\':
                    sOut = sOut + '\\'
            else:
                if sInput[-1] != '/':
                    sInput = sInput + '/'
                if sOut[-1] != '/':
                    sOut = sOut + '/'
        for sFile in os.path.abspath(sInput):
            if sFile.endswith(".fasta") or sFile.endswith(".fa") or sFile.endswith(".fna"):
                lInputList.append(sInput + sFile)
                lOutList.append(sOut + sFile)
        for iIndex, sFile in enumerate(lInputList):
            sys.stdout.write('Processing '+sFile)
            with open(sFile, 'r') as f:
                with open(lOutList[iIndex], 'w') as w:
                    while(1):
                        sLine = f.readline()
                        if not sLine:
                            break
                        if sLine[0] == '>':
                            if sLine.find('[') != -1 or sLine.find(']') != -1:
                                sLine = sLine.replace("[", "(")
                                sLine = sLine.replace("]", ")")
                            if sLine.find('{') != -1 or sLine.find('}') != -1:
                                sLine = sLine.replace('{', '(')
                                sLine = sLine.replace('}', ')')
                            if sLine.find('=') != -1:
                                sLine = sLine.replace('=', ' ')
                            if sLine.find('#') != -1:
                                sLine = sLine.replace('#', ' ')
                            if sLine.find('/') != -1:
                                sLine = sLine.replace('/', ' ')
                            if sLine.find('"') != -1:
                                sLine = sLine.replace('"', ' ')
                        w.write(sLine)
            sys.stdout.write(' -> Done\n')
        return
    

if __name__ == '__main__':
    main()
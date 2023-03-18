# Group 2: Baculi, Cavaynero, Gado, Homillano, Jimenez, Joaquin, Tugadi, Vicario
# This program is a lexical analyzer that is only available for the MANA programming language.


RE_Special_Characters = (
    "\\", '@', '#', '$', '{', '}', '[', ']', '>', '<', '?', '.', ':', "'", '"')
RE_Operators = ('+', '-', '*', '=', '/', '^' '&', '<', '>', '!', '~', '|')
delimbracklist = ('[', ']', '{', '}', ';', ':', '.', ',','(',')')

parselist =[]
def catch_illegal(chara, type,tokennum):  # check if there are illegal characters
    if chara.isalnum() or chara in RE_Operators or chara in RE_Special_Characters or chara == ';':
        while (chara.isalnum() or chara in RE_Operators or chara in RE_Special_Characters or chara == ';'):
            OutputFile.write(chara)
            chara = fp.read(1)
        OutputFile.write("\t\t\t\t\tIlegal_na_karakter\n")
        parselist.append(100)
        fp.seek(fp.tell()-1)
    else:
        OutputFile.write("\t\t" + type + "\n")
        
        parselist.append(tokennum)


def catch_illegal2(chara, type,tokennum):  # catch for unary operators only
    ilegall = 0
    if chara in RE_Operators or chara in RE_Special_Characters or chara == ';':
        while (chara.isalnum() or chara in RE_Operators or chara in RE_Special_Characters or chara == ';'):
            OutputFile.write(chara)
            chara = fp.read(1)
        OutputFile.write("\t\t\t\tIlegal_na_karakter\n")
        fp.seek(fp.tell()-1)
    elif chara.isalnum():   # if alphabet or number, then a loop will happen
        #chara = red(chara,fp)
        while True:
            chara = red(chara, fp)
            # if any chara is found to be an operator or special character, then this will be an ilegal na karakter
            if chara in RE_Operators or chara in RE_Special_Characters or chara.isalnum():
                ilegall = 1
            elif chara == ' ':  # if white space, new line,end of file or tabspace, then the loop will end
                break
            elif chara == '\n':
                break
            elif chara == '\t':
                break
            elif not chara:
                break

        if ilegall == 1:  # if any chara is found to be an operator or special character, then this will be an ilegal na karakter
            OutputFile.write("\t\t\t\tIlegal_na_karakter\n")
            parselist.append(100)
        else:  # if not, then this will be an unaryo operator
            OutputFile.write("" + type + "\n")
            parselist.append(tokennum)
    else:
        OutputFile.write("" + type + "\n")
        parselist.append(tokennum)


def catch_illegal3(chara10, fp10):
    if chara10 == ' ' or chara10 == '\n' or chara10 == '\t':
        pass
    else:
        while 1:
            chara10 = red(chara10, fp)
            if chara10 == ' ' or chara10 == '\n' or chara10 == '\t' or chara10 in delimbracklist:
                break

    OutputFile.write("\t\t\t\tIlegal_na_karakter\n")
    delimbrack(chara10)


def is_literal(chara):  # identify literals/pisi
    if chara == '\"':  # if chara is " then it will loop until the next " is found
        while 1:
            chara = red(chara, fp)
            if chara == '\\':
                chara = red(chara, fp)
                if chara == '"':
                    chara = red(chara, fp)
            if chara == '\"':
                OutputFile.write(chara)
                break
            if not chara:  # an error will be written if the end of file is reached while not finding the next "
                OutputFile.write(
                    '\nError! You are missing some double quotation mark \'\"\'!\n')
                return 1
        # token literal will be given if the loop above is successful
        OutputFile.write('\t\tLiteral\n')
        parselist.append(75)
        return 1
    else:  # if the chara is not " then nothing will happen
        pass


def is_operator(chara):  # identify operators
    if chara == '+':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t+=',58)
            #parselist.append(1+58)
        elif chara == '+':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t++',55)
            #parselist.append(1+55)
        else:
            catch_illegal2(chara, '\t\t\t\t\t+',39)
            #parselist.append(1+39)
        return -1  # the return is -1 because there is a return that has 1 or more
    elif chara == '-':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t-=',60)
            #parselist.append(1+60)
        elif chara == '-':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t--',56)
            #parselist.append(1+56)
        else:
            catch_illegal2(chara, '\t\t\t\t\t-',40)
            #parselist.append(1+40)
        return -1
    elif chara == '=':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t==',46)
            #parselist.append(1+46)
        else:
            catch_illegal(chara, '\t\t\t=',57)
            #parselist.append(1+57)
        return -1
    elif chara == '/':
        chara = fp.read(1)
        if chara == '=':
            chara = fp.read(1)
            catch_illegal2(chara, '/= \t\t\t\t\t/=',61)
        elif chara == '*':
            commentlinecount = comment(chara)
            return commentlinecount  # the return here is positive number
        elif chara == '/':
            commentlinecount = 1
            comment(chara)
            return commentlinecount
        else:
            OutputFile.write('/')
            catch_illegal(chara, '\t\t\t/',42)
            #parselist.append(1+42)
        return -1
    elif chara == '^':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t^=',64)
        else:
            catch_illegal(chara, '\t\t\t^',45)
        return -1
    elif chara == '%':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t%=', 62)
        else:
            catch_illegal(chara, '\t\t\t%',44)
        return -1
    elif chara == '*':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t*=',59)
        else:
            catch_illegal(chara, '\t\t\t*', 41)
        return -1
    elif chara == '~':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal2(chara, '\t\t\t\t\t~=',63)
        else:
            catch_illegal(chara, '\t\t\t~',43)
        return -1
    elif chara == '!':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t!=',47)
        else:
            catch_illegal(chara, '\t\t\t!',52)
        return -1
    elif chara == '<':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t<=',51)
        else:
            catch_illegal(chara, '\t\t\t<',49)
        return -1
    elif chara == '>':
        chara = red(chara, fp)
        if chara == '=':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t>=',50)
        else:
            catch_illegal(chara, '\t\t\t>',48)
        return -1
    elif chara == '&':
        chara = red(chara, fp)
        if chara == '&':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t&&',53)
        else:
            catch_illegal3(chara, fp)

        return -1
    elif chara == '|':
        chara = red(chara, fp)
        if chara == '|':
            chara = red(chara, fp)
            catch_illegal(chara, '\t\t\t||',54)
        else:
            catch_illegal3(chara, fp)
        return -1
    # else:
        # return 0


def comment(chara):  # recognize single and multi-comments
    commentlinecount = 0
    if chara == '*':  # if the current chara is * then a loop will happen until the next */ is found
        OutputFile.write('This is a Multiline Comment: ')
        while (1):
            chara = fp.read(1)
            if chara == '*':
                chara = fp.read(1)
                if chara == '/':
                    chara = fp.read(1)
                    if chara == '\n':
                        commentlinecount += 1
                        OutputFile.write(chara)
                    OutputFile.write('')
                    break
                elif chara == '\n':
                    fp.seek(fp.tell()-1)
                else:
                    OutputFile.write(chara)
            elif chara == '\n':  # if the chara is next line, then it will start a new line and start a new 'this is a comment:' line
                commentlinecount += 1
                OutputFile.write(chara)
                OutputFile.write('This is a Multiline Comment: ')
            elif not chara:  # error will be written if the end of file is reached while not finding the next */
                OutputFile.write("\nError! You are missing some '*/'!\n")
                return 0
            else:
                OutputFile.write(chara)
    else:  # if the chara is /, then a loop will happen until new line is found
        OutputFile.write('This is a Single Comment: ')
        while chara != '\n':
            if not chara:
                break
            chara = fp.read(1)
            OutputFile.write(chara)
            commentline = 1

        commentlinecount = 1
    return commentlinecount


def ident(chara1, fp1, lettercount):  # check if identifier
    notid = 0
    while 1:  # if chara is alphabet, number, _ or $, then the loop will happen until it is false
        if lettercount < 31:  # this will also check whether the letter count is less than 100
            if chara1 == ' ' or chara1 == '\n' or chara1 == '\t' or chara1 in delimbracklist:
                break
            elif chara1 == '_' or chara1 == '$':
                pass

            elif chara1.isalnum() == False:
                notid = 1

            OutputFile.write(chara1)
            chara1 = fp1.read(1)
            lettercount += 1
        else:  # if letter count is more than 100, an error will be written
            OutputFile.write(
                "\nError! Identifiers can only have 31 or less characters\n")
            return 0
    '''if chara1 == '\n':  #if the character that caused the loop above to be false is \n, then the current position of reader will be go back by 1
                        # so that it will start again and read the \n in the main program below
        pass
    
    elif chara1 in RE_Operators:  #then if chara the chara that cause the loop above to be false is in the list of operators, it will be considered as ilegal na karakter
        while 1:    #loop until white space or new line or end of file is found
            if chara1 == ' ':
                break
            elif chara1 == '\n':
                fp1.seek(fp1.tell()-1)
                break
                
            elif chara1 == '\t':
                break
            elif not chara1:
                break
            chara1 = red(chara1,fp1)
            
        OutputFile.write('\t\t\t\tIlegal_na_Karakter\n')'''

    # else :  #if it the character is a white space, newline, delimeter or bracket, then the token will be identifier
    # and will also check if it is in delimter or bracket
    if notid == 0:
        OutputFile.write('\t\t\tID\n')
        
        parselist.append(0)
    elif notid == 1:
        OutputFile.write('\t\t\t\tError! Invalid Token.\n')
    #delimbrack(chara1)


def red(chara2, fp2):  # write current char and return next char
    OutputFile.write(chara2)
    return fp2.read(1)


def elsekeyident(chara4, fp4, lettercount4):  # check if identifier or keyword
    # if chara is alphabet, number, _ or $ then it is an identifier
    if chara4 ==' ' or chara4 == '\n' or chara4 == '\t' or chara4 in delimbracklist:
        return -20

    elif chara4 in RE_Operators:  # if chara is operator, then it will be an ilegal na karakter
        while 4:
            if chara4 == ' ':
                break
            elif chara4 == '\n':
                fp4.seek(fp4.tell()-1)
                break
            elif chara4 == '\t':
                break

            elif not chara4:
                break
            chara4 = red(chara4, fp4)

        OutputFile.write('\t\t\t\tIlegal_na_Karakter\n')
    else:  # if it the character is a white space, newline, delimeter or bracket, then the token will be keyword
        # and will also check if it is in delimter or bracket
        ident(chara4, fp4, lettercount4)
        


# check if identifier or reserved word, almost the same as elsekeyident but the end will have reserve word
def elseresident(chara4, fp4, lettercount4):
    if chara4.isalnum():
        ident(chara4, fp4, lettercount4)

    elif chara4 in RE_Operators:
        while 1:
            if chara4 == ' ':
                break
            elif chara4 == '\n':
                fp4.seek(fp4.tell()-1)
                break
            elif chara4 == '\t':
                break

            elif not chara4:
                break
            chara4 = red(chara4, fp4)

        OutputFile.write('\t\t\t\tIlegal_na_karakter\n')
    else:
        OutputFile.write('\t\t\t\tReserve_Word\n')
        delimbrack(chara4)


# check if identifier or noise word, almost the same as elsekeyident but the end will have reserve word
def elsenoiseident(chara4, fp4, lettercount4):
    if chara4.isalnum():
        ident(chara4, fp4, lettercount4)

    elif chara4 in RE_Operators:
        while 1:
            if chara4 == ' ':
                break
            elif chara4 == '\n':
                fp4.seek(fp4.tell()-1)
                break
            elif chara4 == '\t':
                break

            elif not chara4:
                break
            chara4 = red(chara4, fp4)

        OutputFile.write('\t\t\t\t\tIlegal_na_karakter\n')
    else:
        OutputFile.write('\t\t\t\tNoise_Word\n')
        delimbrack(chara4)


def delimbrack(chara5):  # identify delimeters and brackets
    if chara5 == ';':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t;\n')
        parselist.append(72)
        return 1
    elif chara5 == '(':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t(\n')
        parselist.append(69)
        return 1
    elif chara5 == ')':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t)\n')
        parselist.append(70)
        return 1
    elif chara5 == '[':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t[\n')
        parselist.append(67)
        return 1
    elif chara5 == ']':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t]\n')
        parselist.append(68)
        return 1
    elif chara5 == '{':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t{\n')
        parselist.append(65)
        return 1
    elif chara5 == '}':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t}\n')
        parselist.append(66)
        return 1
    elif chara5 == ':':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t:\n')
        parselist.append(71)
        return 1
    elif chara5 == ',':
        OutputFile.write(chara5)
        OutputFile.write('\t\t\t\t\t,\n')
        parselist.append(73)
        return 1
    else:
        pass


def constantnum(chara6, fp6):  # idetify if karosa and intedyer
    isfloat = 0
    dotcount = 0
    notnum = 0
    while 1:  # loop until the chara is not number
        if chara6 == '.':   # if . is found then it will be considered as a float
            dotcount += 1
            '''if dotcount >1:
                OutputFile.write(' : <Karosa>\n')
                fp6.seek(fp6.tell()-1)
                return 0
            else:'''

            OutputFile.write(chara6)
            chara6 = fp6.read(1)
            isfloat = 1
            # if the next chara after '.' is not number, then it will be considered as karosa and end the loop
            if chara6.isnumeric() == False and dotcount == 1:

                OutputFile.write('0 : <Karosa>\n')
                parselist.append(1+27)
                return 0
            elif chara6.isnumeric() == False and dotcount > 1:

                OutputFile.write('0 : Error! Invalid Token\n')
                return 0
        elif chara6 == ' ' or chara6 == '\n' or chara6 == '\t' or chara6 in delimbracklist:
            break
        elif chara6.isnumeric() == False:
            notnum = 1

        OutputFile.write(chara6)
        chara6 = fp6.read(1)
    if notnum == 1:
        OutputFile.write('\t\t\t\tError! Invalid Token\n')

    elif isfloat == 0:  # written if '.' is not found
        OutputFile.write('\t\t\t\tIntedyer\n')
        parselist.append(1+26)
    elif isfloat != 0:  # written if '.' is found
        if dotcount == 1:
            OutputFile.write('\t\t\t\tKarosa\n')
            parselist.append(1+27)
        elif dotcount > 1:
            OutputFile.write('\t\t\t\tError! Invalid Token\n')
    delimbrack(chara6)


def is_char(chara7, fp7):  # check for karakter and pisi
    charcount = 0
    if chara7 == '\'':  # if chara is ' then a loop will happen until the next ' is found
        while 1:
            chara7 = red(chara7, fp)
            if chara7 == '\\':
                chara7 = red(chara7, fp)
                if chara7 == '\'':
                    chara7 = red(chara, fp)
            if chara7 == '\'':
                OutputFile.write(chara7)
                break
            if not chara7:  # if end of file is reached and the next ' is not found, and error will be written
                OutputFile.write(
                    '\nError! You are missing some quotation mark \"\'\"!\n')
                return 0
            charcount += 1

        if charcount > 1:  # if charcount is more than 1 then it will be pisi
            OutputFile.write('\t\t\tPisi\n')
            parselist.append(1+28)
        else:  # if the char count is 0 or 1, then it will be karakter
            OutputFile.write('\t\t\t\tKarakter\n')
            parselist.append(1+29)
        return 1


#############################################
#
#   Start of the program here
#
#############################################
while (True):
    filename = input("\nEnter filename to read (ex. testing.mana): ")
    if filename.endswith('.mana'):
        print("\nFile opened successfully...\n")
        break
    else:
        print('\nInvalid input! Please input a file with .mana extension')
fp = open(filename, 'r', encoding='utf-8')
OutputFile = open('Symbol_Table.txt', 'w')
OutputFile.write('\tLEXEME                  TOKEN\n')
OutputFile.write('---------------------------------------\n')
chara = ''
while (1):
    ifcheck = 0
    ifcheck1 = 0
    ifcheck2 = 0
    ifcheck3 = 0
    chara = fp.read(1)  # read character 1 by 1
    # functions return 1 if any if statements is true
    ifcheck = is_literal(chara)
    # functions return 1 if any if statements is true
    ifcheck1 = delimbrack(chara)
    # functions return 1 if any if statements is true
    ifcheck2 = is_char(chara, fp)
    # functions return 1 if any if statements is true
    ifcheck3 = is_operator(chara)
    # the functions above needs to be checked if any if statements were true
    # so that the next chara will not land in the else statement below, incase that it isnt
    # in any if statements below, but is recognized in any functions above
    # keywords that starts with a
    if chara == 'a':  # check if the chara is 'a', is true, if true then chara=red() will run
        # this function will print the current chara then return the next chara.
        chara = red(chara, fp)
        if chara == 't':  # AT
            chara = red(chara, fp)
            if elsekeyident(chara,fp,6) == -20:
                OutputFile.write('\t\t\t\t\tat\n')
                parselist.append(2)
                delimbrack(chara)
            
            # This function will be seen in every end of nested if
            # It will only change if it is reserved word, noise word or keyword.
            # elsekeyident = keywords, elseresident = reserved words, elsenoiseident = noise words
        elif chara == 'n':
            chara = red(chara, fp)
            if chara == 'g':
                chara = red(chara, fp)
                if chara == 'k':
                    chara = red(chara, fp)
                    if chara == 'a':
                        chara = red(chara, fp)
                        if chara == 't':  # ANGKAT
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\tangkat\n')
                                parselist.append(1)
                            delimbrack(chara)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                elsekeyident(chara, fp, 2)

        elif chara == 'k':
            chara = red(chara, fp)
            if chara == 't':
                chara = red(chara, fp)
                if chara == 'e':
                    chara = red(chara, fp)
                    if chara == 'r':  # AKTER
                        chara = red(chara, fp)
                        if elsekeyident(chara,fp,5) == -20:
                            OutputFile.write('\t\t\t\takter\n')
                            parselist.append(36)

                    else:  # There is an else at every if statements, so that incase that the chara did not match any characters
                        # it will be considered as an identifier
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keywords start with B
    elif chara == 'b':
        chara = red(chara, fp)
        if chara == 'i':
            chara = red(chara, fp)
            if chara == 'l':
                chara = red(chara, fp)
                if chara == 'a':
                    chara = red(chara, fp)
                    if chara == 'n':
                        chara = red(chara, fp)
                        if chara == 'g':  # BILANG
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\tbilang\n')
                                parselist.append(3)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        elif chara == 'u':
            chara = red(chara, fp)
            if chara == 'm':
                chara = red(chara, fp)
                if chara == 'a':
                    chara = red(chara, fp)
                    if chara == 'l':
                        chara = red(chara, fp)
                        if chara == 'i':
                            chara = red(chara, fp)
                            if chara == 'k':  # BUMALIK
                                chara = red(chara, fp)
                                if elsekeyident(chara,fp,7) == -20:
                                    OutputFile.write('\t\t\t\tbumalik\n')
                                    parselist.append(4)
                            else:
                                ident(chara, fp, 6)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)

    # Keywords start with E
    elif chara == 'e':
        chara = red(chara, fp)
        if chara == 'k':
            chara = red(chara, fp)
            if chara == 's':
                chara = red(chara, fp)
                if chara == 'p':  # EKSP
                    chara = red(chara, fp)
                    if elsekeyident(chara,fp,4) == -20:
                        OutputFile.write('\t\t\t\teksp\n')
                        parselist.append(6)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        elif chara == 'd':
            chara = red(chara, fp)
            if chara == 'y':
                chara = red(chara, fp)
                if chara == 'e':
                    chara = red(chara, fp)
                    if chara == 'r':  # EDYER
                        chara = red(chara, fp)
                        if elsekeyident(chara,fp,5) == -20:
                        # This is a noiseword, so it will be elsenoiseident
                            OutputFile.write('\t\t\t\tedyer\n')
                            parselist.append(1+31)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keywords start with H
    elif chara == 'h':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 't':
                chara = red(chara, fp)
                if chara == 'i':  # HATI
                    chara = red(chara, fp)
                    OutputFile.write('\t\t\t\thati\n')
                    parselist.append(8)
                else:
                    ident(chara, fp, 3)
            elif chara == 'b':
                chara = red(chara, fp)
                if chara == 'a':
                    chara = red(chara, fp)
                    if chara == 'n':
                        chara = red(chara, fp)
                        if chara == 'g':  # HABANG
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                        # This is a reserved word, so it will be elseresident
                                OutputFile.write('\t\t\t\thabang\n')
                                parselist.append(7)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        elif chara == 'u':
            chara = red(chara, fp)
            if chara == 'w':
                chara = red(chara, fp)
                if chara == 'a':
                    chara = red(chara, fp)
                    if chara == 'd':  # HUWAD
                        chara = red(chara, fp)
                        if elsekeyident(chara,fp,6) == -20:
                            OutputFile.write('\t\t\t\thuwad\n')
                            parselist.append(1+22)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keywords start with I
    elif chara == 'i':
        chara = red(chara, fp)
        if chara == 'n':
            chara = red(chara, fp)
            if chara == 't':  # INT
                chara = red(chara, fp)
                if elsekeyident(chara,fp,3) == -20:
                    OutputFile.write('\t\t\t\t\tint\n')
                    parselist.append(10)
            elif chara == 'i':  # INI
                chara = red(chara, fp)
                if elsekeyident(chara,fp,3) == -20:
                    OutputFile.write('\t\t\t\t\tini\n')
                    parselist.append(1+33)
            else:
                if elsekeyident(chara,fp,2) == -20:
                    OutputFile.write('\t\t\t\t\tin\n')
                    parselist.append(38)

        elif chara == 'b':
            chara = red(chara, fp)
            if chara == 'a':
                chara = red(chara, fp)
                if elsekeyident(chara,fp,3) == -20:
                    OutputFile.write('\t\t\t\t\tiba\n')
                    parselist.append(9)
            else:
                ident(chara, fp, 2)

        
    # Keywords starts with K
    elif chara == 'k':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 'p':
                chara = red(chara, fp)
                if chara == 'a':
                    chara = red(chara, fp)
                    if chara == 'g':
                        chara = red(chara, fp)
                        if chara == 'd':
                            chara = red(chara, fp)
                            if chara == 'i':  # KAPAGDI
                                chara = red(chara, fp)
                                if elsekeyident(chara,fp,7) == -20:
                                    OutputFile.write('\t\t\t\tkapagdi\n')
                                parselist.append(13+1)
                            else:
                                ident(chara, fp, 6)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            elif chara == 'r':
                chara = red(chara, fp)
                if chara == 'o':
                    chara = red(chara, fp)
                    if chara == 's':
                        chara = red(chara, fp)
                        if chara == 'a':  # KAROSA
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\tkarosa\n')
                                parselist.append(12+1)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:  # KAR
                    if elsekeyident(chara,fp,3) == -20:
                        OutputFile.write('\t\t\t\t\tkar\n')
                        parselist.append(11+1)
            else:  # KA
                if elsekeyident(chara,fp,2) == -20:
                    OutputFile.write('\t\t\t\t\tka\n')
                    parselist.append(35)
        
                
    # KEYWORD THAT STARTS WITH M
    elif chara == 'm':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 'i':
                chara = red(chara, fp)
                if chara == 'n':  # MAIN
                    chara = red(chara, fp)
                    if elsekeyident(chara,fp,4) == -20:
                        OutputFile.write('\t\t\t\tmain\n')
                        parselist.append(74)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # keywords that starts with l
    elif chara == 'l':
        chara = red(chara, fp)
        if chara == 'i':
            chara = red(chara, fp)
            if chara == 'm':
                chara = red(chara, fp)
                if chara == 'b':
                    chara = red(chara, fp)
                    if chara == 'a':
                        chara = red(chara, fp)
                        if chara == 'g':  # LIMBAG
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\tlimbag\n')
                                parselist.append(16+1)

                        else:
                            ident(chara, fp, 5)

                    else:
                        ident(chara, fp, 4)
                

                else:
                    ident(chara, fp, 4)
            else:
                ident(chara, fp, 3)
        elif chara == 'o':
            chara = red(chara, fp)
            if chara == 'o':
                chara = red(chara, fp)
                if chara == 'b':  # LOOB
                    chara = red(chara, fp)
                    if elsekeyident(chara,fp,4) == -20:
                        OutputFile.write('\t\t\t\tloob\n')
                        parselist.append(17+1)

                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)

        else:
            ident(chara, fp, 1)
        delimbrack(chara)
        # Keywords start with p
    elif chara == 'p':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 'r':
                chara = red(chara, fp)
                if chara == 'a':  # PARA
                    chara = red(chara, fp)
                    if elsekeyident(chara,fp,4) == -20:
                        OutputFile.write('\t\t\t\tpara\n')
                        parselist.append(19+1)
                else:
                    ident(chara, fp, 3)

            elif chara == 'g':  # PAG
                chara = red(chara, fp)
                if elsekeyident(chara,fp,3) == -20:
                    OutputFile.write('\t\t\t\t\tpag\n')
                    parselist.append(18+1)
            else:  # PA
                if elsekeyident(chara,fp,2) == -20:
                    OutputFile.write('\t\t\t\t\tpa\n')
                    parselist.append(32+1)
        elif chara == 'i':
            chara = red(chara, fp)
            if chara == 's':
                chara = red(chara, fp)
                if chara == 'i':  # PISI
                    chara = red(chara, fp)
                    OutputFile.write('\t\t\t\tpisi\n')
                    parselist.append(20+1)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # keywords that starts with t
    elif chara == 't':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 'n':
                chara = red(chara, fp)
                if chara == 'g':
                    chara = red(chara, fp)
                    if chara == 'g':
                        chara = red(chara, fp)
                        if chara == 'a':
                            chara = red(chara, fp)
                            if chara == 'p':  # TANGGAP
                                chara = red(chara, fp)
                                if elsekeyident(chara,fp,7) == -20:
                                    OutputFile.write('\t\t\t\ttanggap\n')
                                    parselist.append(21+1)
                            else:
                                ident(chara, fp, 6)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)

        elif chara == 'u':
            chara = red(chara, fp)
            if chara == 'w':
                chara = red(chara, fp)
                if chara == 'i':
                    chara = red(chara, fp)
                    if chara == 'r':
                        chara = red(chara, fp)
                        if chara == 'a':
                            chara = red(chara, fp)
                            if chara == 'n':  # TUWIRAN reserved word
                                chara = red(chara, fp)
                                if elsekeyident(chara,fp,7) == -20:
                                    OutputFile.write('\t\t\t\ttuwiran\n')
                                    parselist.append(24+1)
                            else:
                                ident(chara, fp, 6)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)

            elif chara == 'm':
                chara = red(chara, fp)
                if chara == 'p':
                    chara = red(chara, fp)
                    if chara == 'a':
                        chara = red(chara, fp)
                        if chara == 'k':  # TUMPAK reserved word
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\ttumpak\n')
                                parselist.append(23+1)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)

            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keywords start with W
    elif chara == 'w':
        chara = red(chara, fp)
        if chara == 'a':
            chara = red(chara, fp)
            if chara == 'l':
                chara = red(chara, fp)
                if chara == 'a':  # WALA reserved word
                    chara = red(chara, fp)
                    if elsekeyident(chara,fp,4) == -20:
                        OutputFile.write('\t\t\t\twala\n')
                        parselist.append(25+1)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keywords start with letter D
    elif chara == 'd':
        chara = red(chara, fp)
        if chara == 'i':
            chara = red(chara, fp)
            if chara == 'l':
                chara = red(chara, fp)
                if chara == 'o':
                    chara = red(chara, fp)
                    if chara == 'o':
                        chara = red(chara, fp)
                        if chara == 'b':  # DILOOB
                            chara = red(chara, fp)
                            if elsekeyident(chara,fp,6) == -20:
                                OutputFile.write('\t\t\t\tdiloob\n')
                                parselist.append(5)
                        else:
                            ident(chara, fp, 5)
                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)
            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keyword start with letter o
    elif chara == 'o':
        chara = red(chara, fp)
        if chara == 'n':
            chara = red(chara, fp)
            if chara == 'e':
                chara = red(chara, fp)
                if chara == 'n':
                    chara = red(chara, fp)
                    if chara == 't':  # ONENT
                        chara = red(chara, fp)
                        if elsekeyident(chara,fp,5) == -20:
                            OutputFile.write('\t\t\t\tonent\n')
                            parselist.append(30+1)

                    else:
                        ident(chara, fp, 4)
                else:
                    ident(chara, fp, 3)

            else:
                ident(chara, fp, 2)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # Keyword start with letter s
    elif chara == 's':
        chara = red(chara, fp)
        if chara == 'a':  # SA
            chara = red(chara, fp)
            if elsekeyident(chara,fp,2) == -20:
                OutputFile.write('\t\t\t\t\tsa\n')
                parselist.append(37)
        else:
            ident(chara, fp, 1)
        delimbrack(chara)
    # if the chara is numeric, then it will call the function to know if it is karosa or intedyer
    elif chara.isnumeric() or chara == '.':
        constantnum(chara, fp)

    # elif (chara.isalpha() or chara =='_' or chara == '$'):    #if the chara is an alphabet letter and did not match any chara above, then it will land here
        # and will be considered as an identifier
       # ident(chara,fp,1)
    elif chara == '\n':  # if the chara is a new line, then it will be considered but will do nothing
        pass
    elif not chara:  # this is the checking whether if the end of file is found
        parselist.append(100)
        break
    # the ifchecks will be checked here whether any of the if statements were true,
    elif ifcheck != None or ifcheck1 != None or ifcheck2 != None or ifcheck3 != None:
        # and if any statements were true, nothing will happen
        pass
    # if the chara is a whitespace or tabspace, then it will be considered but will do
    elif chara == ' ' or chara == '\t':
        pass
    else:  # then if the chara is not recognized in any if statements above, then it will land here.

        ident(chara, fp, 1)
        #OutputFile.write('\n'+ chara + ' this character is not recognized!\n')


fp.close()
OutputFile.close()
print('Symbol Table Created...')
def tokennumbers():
    return parselist
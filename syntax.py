
import manaCode5


class parse:
    def __init__(self, tokens, tokennum):
        self.tokens = tokens
        self.tokennum = tokennum
        self.exprlist = []
        self.outlist = []
        self.exprcount = 0

    def peek(self):

        return self.tokennum+1

    def main(self):
        while (self.tokennum != len(self.tokens)):
            if self.tokens[self.tokennum] == 19:
                self.tokennum += 1
                print(' pag ', end='')
                self.pag(0)
            elif self.tokens[self.tokennum] == 27:
                self.expr(0)
                print(self.exprlist[0], end='')
                self.removeall()
                print('\n')
                self.tokennum += 1
            elif self.tokens[self.tokennum] == 69:
                self.expr(0)
                print(*self.exprlist[0], end='')
                self.removeall()
                print('\n')
                self.tokennum += 1
            elif self.tokens[self.tokennum] == 0:
                if self.tokens[self.peek()] > 56 and self.tokens[self.peek()] < 65:
                    self.assgnmntstmt()
                    print('\n')
            elif self.tokens[self.tokennum] == 17:
                self.tokennum += 1
                self.outputstmt()
            elif self.tokens[self.tokennum] == 12 or self.tokens[self.tokennum] == 13 or self.tokens[self.tokennum] == 10 or self.tokens[self.tokennum] == 67:
                self.declarationstmt()
            elif self.tokens[self.tokennum] == 20:
                self.forexpr()
            elif self.tokens[self.tokennum] == 7:
                self.whileexpr()
            else:
                self.tokennum += 1

    def removeall(self):
        self.exprlist.pop()
        for x in self.exprlist:
            self.exprlist.pop()

    def pag(self, rec):
        concheck = 0
        if self.tokens[self.tokennum] == 69:
            self.tokennum += 1
            print(' ( ', end='')
            self.expr(0)
            print(*self.exprlist, end='')
            if self.tokens[self.tokennum] == 70 or self.tokens[self.tokennum-1] == 70:
                print(' ) ', end='')
            else:
                print('Error! missing some )')
        else:
            print(' Error! expression needed')
            return 0
        self.tokennum += 1
        if self.tokens[self.tokennum] == 65:
            self.tokennum += 1
            print(' { ', end='')
            self.stmts()
            self.tokennum -= 1

            if self.tokens[self.tokennum+1] == 66:
                print(' } ', end='')
                self.tokennum += 1
            elif self.tokens[self.tokennum+1] == 99:
                self.tokennum += 1
            else:
                print('eror! missing some }')
            self.tokennum += 1
        else:
            self.stmt()
            '''
            if self.tokens[self.tokennum]== 72:
                print(' ; ',end='')
                self.tokennum+=1
            else: 
                print(self.tokens[self.tokennum])
                print('eror! missing ;')
                '''
        if self.tokens[self.tokennum] == 14:
            self.elseif()
            concheck = 2
        elif self.tokens[self.tokennum] == 9:
            self.tokennum += 1
            print(' iba ', end='')
            if self.tokens[self.tokennum] == 65:
                self.tokennum += 1
                print(' { ', end='')
                self.stmts()
                if self.tokens[self.tokennum] == 66:
                    print(' } ', end='')
                else:
                    print('eror! missing some }')
                self.tokennum += 1
            else:
                self.stmt()
            concheck = 1
        else:
            pass
        if concheck == 0 and rec == 0:
            print(' = <if_stmt>\n')
        elif concheck == 1 and rec == 0:
            print(' = <if_else_stmt>\n')
        elif concheck == 2 and rec == 0:
            print(' = <if_elseif_else_stmt>\n')

    def elseif(self):
        print(' kapagdi ', end='')
        self.tokennum += 1
        self.pag(1)

    def stmts(self):
        self.stmt()
        if self.tokens[self.tokennum] == 12 or self.tokens[self.tokennum] == 13 or self.tokens[self.tokennum] == 10 or self.tokens[self.tokennum] == 67:
            self.stmts()
        elif self.tokens[self.tokennum] == 17:
            self.stmts()
        elif self.tokens[self.tokennum] == 0:
            self.stmts()
        elif self.tokens[self.tokennum] == 19:
            self.stmts()
        elif self.tokens[self.tokennum] == 20:
            self.stmts()
        elif self.tokens[self.tokennum] == 7:
            self.stmts()

        elif self.tokens[self.tokennum] == 14 or self.tokens[self.tokennum] == 9 or self.tokens[self.tokennum] == 19:
            print('Error! missing some \'}\'')
            self.tokens = self.tokens[:self.tokennum] + \
                [99] + self.tokens[self.tokennum:]

    def stmt(self):
        if self.tokens[self.tokennum] == 12 or self.tokens[self.tokennum] == 13 or self.tokens[self.tokennum] == 10 or self.tokens[self.tokennum] == 67:
            self.declarationstmt()
        elif self.tokens[self.tokennum] == 17:
            self.tokennum += 1
            self.outputstmt()
        elif self.tokens[self.tokennum] == 0:
            if self.tokens[self.peek()] > 56 and self.tokens[self.peek()] < 65:
                self.assgnmntstmt()
        elif self.tokens[self.tokennum] == 19:
            self.tokennum += 1
            print(' pag ', end='')
            self.pag(0)
        elif self.tokens[self.tokennum] == 20:
            self.forexpr()
        elif self.tokens[self.tokennum] == 7:
            self.whileexpr()

    def outputstmt(self):
        print(' limbag ', end='')
        if self.tokens[self.tokennum] == 69:
            self.tokennum += 1
            print(' ( ', end='')
            if self.tokens[self.tokennum] == 75:
                print(' Literal ', end='')
            else:
                print('Error! wrong token')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 39:
                print(' + ', end='')
                self.tokennum += 1
                self.expr(0)
                if len(self.exprlist) == 1:
                    self.tokennum += 2
                print(*self.exprlist, end='')

            if self.tokens[self.tokennum] == 70:
                print(' ) ', end='')

            else:
                print(' Error! missing some )')
                self.tokens = self.tokens[:self.tokennum] + \
                    [99] + self.tokens[self.tokennum:]
        else:
            print('Error! missing some (')
            self.tokennum += 1
            return 0
        self.tokennum += 1
        if self.tokens[self.tokennum] == 72:
            print(' ; ', end='')
            self.tokennum += 1
        else:
            self.semicolonrec()
        print(' => <output_stmt>')

    def forexpr(self):
        if self.tokens[self.tokennum] == 20:
            print(' para ', end='')
            self.tokennum += 1

            if self.tokens[self.tokennum] == 69:
                self.tokennum += 1
                print(' ( ', end='')

                if self.tokens[self.tokennum] == 10:
                    self.tokennum += 1
                    print(' int ', end='')
                    self.assgnmntstmt()
                    self.tokennum += 1
                    if self.tokens[self.tokennum] == 0:

                        print(' ID ', end='')
                        self.tokennum += 1
                        if self.tokens[self.tokennum] == 46:
                            print(' == ', end='')
                            self.tokennum += 1
                        elif self.tokens[self.tokennum] == 47:
                            print(' != ', end='')
                            self.tokennum += 1
                        elif self.tokens[self.tokennum] == 48:
                            print(' > ', end='')
                            self.tokennum += 1

                            if self.tokens[self.tokennum] == 0:
                                print(' ID ', end='')
                                self.tokennum += 1
                            elif self.tokens[self.tokennum] == 27:
                                print(' Intedyer ', end='')
                                self.tokennum += 1

                            else:
                                print('error! Wrong token')
                            if self.tokens[self.tokennum] == 72:
                                print(' ; ', end='')
                                self.tokennum += 1
                                if self.tokens[self.tokennum] == 55:
                                    print(' ++ ', end='')
                                    self.tokennum += 1
                                    if self.tokens[self.tokennum] == 0:
                                        print(' ID ', end='')
                                        self.tokennum += 1

                                        if self.tokens[self.tokennum] == 70:
                                            print(' ) ', end='')
                                        else:
                                            print('Error! missing some )')

                                        self.tokennum += 1
                                        if self.tokens[self.tokennum] == 65:
                                            self.tokennum += 1
                                            print(' { ', end='')
                                            self.stmts()
                                            if self.tokens[self.tokennum] == 66:
                                                print(' } ', end='')
                                            else:
                                                print('Error! missing some }')
                                        else:
                                            self.stmt()
                                    else:
                                        print(
                                            'error! missing variable')
                                else:
                                    print('error! Missing unary operator')
                            else:
                                print('error! missing some ;')
                        else:
                            print('error! Missing operator')
                    else:
                        print('error! Missing some variable')
                else:
                    print('error! Missing some variable')
            else:
                print('error! Missing some (')
        print('=> <iterative_stmt>')

    def whileexpr(self):
        if self.tokens[self.tokennum] == 7:
            print(' habang ', end='')
            self.tokennum += 1

        if self.tokens[self.tokennum] == 69:
            self.tokennum += 1
            print(' ( ', end='')

            if self.tokens[self.tokennum] == 0:
                print(' ID ', end='')
                self.tokennum += 1
                if self.tokens[self.tokennum] == 46:
                    print(' == ', end='')
                    self.tokennum += 1
                elif self.tokens[self.tokennum] == 47:
                    print(' != ', end='')
                    self.tokennum += 1
                elif self.tokens[self.tokennum] == 48:
                    print(' > ', end='')
                    self.tokennum += 1
                elif self.tokens[self.tokennum] == 49:
                    print(' < ', end='')
                    self.tokennum += 1

                if self.tokens[self.tokennum] == 0:
                    print(' ID ', end='')
                    self.tokennum += 1
                elif self.tokens[self.tokennum] == 27:
                    print(' Intedyer ', end='')
                    self.tokennum += 1

                    if self.tokens[self.tokennum] == 70:
                        print(' ) ', end='')
                    else:
                        print('Error! missing some )')

                    self.tokennum += 1
                    if self.tokens[self.tokennum] == 65:
                        self.tokennum += 1
                        print(' { ', end='')
                        self.stmts()
                        if self.tokens[self.tokennum] == 55:
                            print(' ++ ', end='')
                            self.tokennum += 1
                            if self.tokens[self.tokennum] == 0:
                                print(' ID ', end='')
                                self.tokennum += 1
                        elif self.tokens[self.tokennum] == 56:
                            print(' -- ', end='')
                            self.tokennum += 1

                            if self.tokens[self.tokennum] == 0:
                                print(' ID ', end='')
                                self.tokennum += 1

                                if self.tokens[self.tokennum] == 72:
                                    print(' ; ', end='')
                                    self.tokennum += 1

                        if self.tokens[self.tokennum] == 66:
                            print(' } ', end='')
                        else:
                            print('error! missing some }')
                    else:
                        self.stmt()
                else:
                    print('error! Missing some variables')
            else:
                print('error! Missing some variables')

        print('=> <iterative_stmt>')


    def declarationstmt(self):
        if self.tokens[self.tokennum] == 10:
            print(" Intedyer ", end='')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 0:
                print(' ID ', end='')
                self.tokennum += 1

        elif self.tokens[self.tokennum] == 12:
            print(" Kar ", end='')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 0:
                print(' ID ', end='')
                self.tokennum += 1

        elif self.tokens[self.tokennum] == 13:
            print(" Karosa ", end='')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 0:
                print(' ID ', end='')
                self.tokennum += 1

        elif self.tokens[self.tokennum] == 67:
            print(' [ ', end='')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 10:
                print(' Intedyer ', end='')
                self.tokennum += 1
            else:
                print('Error! wrong token')
                self.tokennum += 1
                if self.tokens[self.tokennum] == 68:
                    print(' ] ', end='')
                    self.tokennum += 1

                else:
                    print('Error! missing some ]')
        else:
            print('Error!')

        if self.tokens[self.tokennum] == 57:
            print(' = ', end='')
            self.tokennum += 1
            self.expr(0)
            print(*self.exprlist, end='')
            if len(self.exprlist) > 1:
                self.tokennum += 1
            else:
                self.tokennum += 2
        elif self.tokens[self.tokennum] == 69:
            print(' ( ',end='')
            self.tokennum+=1
            if self.tokens[self.tokennum] == 10:
                print(' int ', end ='')
                self.tokennum+=1
            elif self.tokens[self.tokennum] == 12:
                print(' kar ', end ='')
                self.tokennum+=1
            elif self.tokens[self.tokennum] == 13:
                print(' karosa ', end ='')
                self.tokennum+=1
            elif self.tokens[self.tokennum] == 21:
                print(' pisi ', end ='')
                self.tokennum+=1
            else:
                print(' Error! Must be datatype first ', end ='')

            if self.tokens[self.tokennum] == 0:
                print(' ID ', end ='')
                self.tokennum+=1
            else:
                print(' Error! Must be Identifier ', end ='')
            if self.tokens[self.tokennum] == 70:
                print(' ) ', end ='')
                self.tokennum+=1
            else: 
                print(' Error! Missing ) ', end ='')

            if self.tokens[self.tokennum] == 65:
                print(' { ', end ='')
            self.tokennum+=1
            self.stmts()
            if self.tokens[self.tokennum] == 66:
                print(' } ', end ='')
                print(' => <fn_declaration>')
                return
            else:
                print(' Error! Missing } ', end ='')
                print(' => <fn_declaration>')
                return

        if self.tokens[self.tokennum] == 72:
            print(' ; ', end='')
            self.tokennum += 1
        else:
            print('Error! missing ;')
        print(' => <ID_declaration>')

    def assgnmntstmt(self):
        if self.tokens[self.tokennum] == 0:
            print(' ID ', end='')
            self.tokennum += 1
            if self.tokens[self.tokennum] == 57:
                if self.tokens[self.peek()] == 22:
                    print(' = ', end='')
                    print(' tanggap ', end='')
                    self.tokennum += 2
                    if self.tokens[self.tokennum] == 69:

                        print(' ( ', end='')
                        self.tokennum += 1
                    else:
                        print('Error! Missing (', end='')
                    if self.tokens[self.tokennum] == 70:

                        print(' ) ', end='')
                        self.tokennum += 1
                    else:
                        print('Error! missing )')
                    print(' <= <input_stmt>', end='')
                    return 0
                else:

                    print(' <Assignment_Op> ', end='')
                    self.tokennum += 1
                if self.tokens[self.tokennum] == 27:
                    print(" Intedyer ", end='')
                    self.tokennum += 1
                    if self.tokens[self.tokennum] == 72:
                        print(' ; ', end='')
                        print(' => <assignment_stmt>', end='')
                    else:
                        print('error! missing ;')
                elif self.tokens[self.tokennum] == 0:
                    print(" ID ", end='')
                    self.tokennum += 1
                    if self.tokens[self.tokennum] == 72:
                        print(' ; ', end='')
                        print(' => <assignment_stmt>')
                    else:
                        print('error! missing ;')
            elif self.tokens[self.tokennum] == 58:
                print(' <Assignment_Op> ', end='')
                self.tokennum += 1
                if self.tokens[self.tokennum] == 27:
                    print(' Intedyer ', end='')
                    self.tokennum += 1
                    if self.tokens[self.tokennum] == 39:
                        print(' + ', end='')
                        self.tokennum += 1
                        if self.tokens[self.tokennum] == 27:
                            print(' Intedyer ', end='')
                            self.tokennum += 1
                            if self.tokens[self.tokennum] == 72:
                                print(' ; ', end='')
                                print(' => <assignment_stmt> ', end='')
                            else:
                                print('error! missing ;')
                    elif self.tokens[self.tokennum] == 40:
                        print(' - ', end='')
                        self.tokennum += 1
                        if self.tokens[self.tokennum] == 27:
                            print(' Intedyer ', end='')
                            self.tokennum += 1
                            if self.tokens[self.tokennum] == 72:
                                print(' ; ', end='')
                                print(' => <assignment_stmt> ', end='')
                            else:
                                print('Error! missing ;')
                    elif self.tokens[self.tokennum] == 41:
                        print(' * ', end='')
                        self.tokennum += 1
                        if self.tokens[self.tokennum] == 27:
                            print(' Intedyer ', end='')
                            self.tokennum += 1
                            if self.tokens[self.tokennum] == 72:
                                print(' ; ', end='')
                                print(' => <assignment_stmt> ', end='')
                            else:
                                print('Error! missing ;')
                    elif self.tokens[self.tokennum] == 42:
                        print(' / ', end='')
                        self.tokennum += 1
                        if self.tokens[self.tokennum] == 27:
                            print(' Intedyer ', end='')
                            self.tokennum += 1
                            if self.tokens[self.tokennum] == 72:
                                print(' ; ', end='')
                                print(' =>  <assignment_stmt> ', end='')
                            else:
                                print('Error! missing ;')

    def id(self):
        if self.tokens[self.tokennum] == self.var():
            pass
        elif self.tokens[self.tokennum] == self.consts():
            pass


    def getexpr(self):
        self.exprlist = []
        self.exprcount = 0
        if (self.tokens[self.peek()] >= 39 and self.tokens[self.peek()] <= 56) or self.tokens[self.tokennum] == 69:
            while 1:
                self.exprlist.append(self.tokens[self.tokennum])
                self.tokennum += 1
                if self.tokens[self.tokennum] < 39 and self.tokens[self.tokennum] > 30:
                    break
                elif self.tokens[self.tokennum] < 27 and self.tokens[self.tokennum] > 0:
                    break
                elif self.tokens[self.tokennum] > 56 and self.tokens[self.tokennum] < 69:
                    break
                elif self.tokens[self.tokennum] > 70:
                    break
                elif self.tokens[self.tokennum] == 70 and self.tokens[self.tokennum+1] not in [0, 39, 27, 28, 30, 75, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70]:
                    self.tokennum += 1
                    break
        elif self.tokens[self.tokennum] == 27 or self.tokens[self.tokennum] == 28 or self.tokens[self.tokennum] == 0:
            self.exprlist.append(self.tokens[self.tokennum])
        self.exprlist = [self.exprlist]
        self.tokennum -= 1

    def expr(self, red):
        logor = [54]
        logand = [53]
        eq = [46, 47]
        rel = [48, 49, 50, 51]
        addit = [39, 40]
        mult = [41, 42, 43, 44]
        una = [55, 56]
        pare = [69, 70]
        terms = [0, 27, 28, 30, 75]
        if self.tokens[self.tokennum] == -1:
            pass
        elif red == 1:
            pass
        else:
            self.getexpr()
        count = 0
        while 1:
            testing = 0
            for k in self.exprlist:
                if isinstance(k, list) == True:
                    testing += 1
            if testing == 0:
                break
            self.exprcheck(logor, 1)
            self.exprcheck(logand, 2)
            self.exprcheck(eq, 3)
            self.exprcheck(rel, 4)
            self.exprcheck(addit, 5)
            self.exprcheck(mult, 6)
            self.exprcheck(una, 7)
            self.exprcheck(terms, 8)
            count += 1
            if count > 20:
                exit()

    def exprcheck(self, opelist, ope):
        temp2 = []
        indexnow = 0
        indextemp = 0
        onn = 0
        changed = 0
        parencount = 0

        while indexnow < len(self.exprlist[self.exprcount]):
            if self.exprlist[self.exprcount][indexnow] == 69 and ope != 8:
                for e, x in reversed(list(enumerate(self.exprlist[self.exprcount]))):
                    if x == 70:
                        for r, z in list(enumerate(self.exprlist[self.exprcount])):
                            if z == 69:
                                indexnow += e

                                break
                        break
            elif self.exprlist[self.exprcount][indexnow] in opelist:
                if ope == 1:
                    self.logical_or_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return
                if ope == 2:
                    self.logical_and_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return
                if ope == 3:
                    self.equality_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return
                if ope == 4:
                    self.relational_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return
                if ope == 5:
                    self.additive_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return
                if ope == 6:
                    self.multiplicative_expr(
                        self.exprlist[self.exprcount][indexnow], indexnow)
                    return

                if ope == 7:
                    self.unary_expr(self.exprlist[indexnow])
                    return

                if ope == 8:

                    if self.exprlist[self.exprcount][0] == 0:
                        self.exprlist[self.exprcount] = 'ID'
                    elif self.exprlist[self.exprcount][0] == 27:
                        self.exprlist[self.exprcount] = 'Intedyer'
                    elif self.exprlist[self.exprcount][0] == 28:
                        self.exprlist[self.exprcount] = 'Karosa'
                    elif self.exprlist[self.exprcount][0] == 30:
                        self.exprlist[self.exprcount] = 'Kar'
                    elif self.exprlist[self.exprcount][0] == 75:
                        self.exprlist[self.exprcount] = 'Literal'
                    elif self.exprlist[self.exprcount][0] == 69:
                        temp = self.exprlist
                        indextemp = indexnow

                        for e, x in reversed(list(enumerate(self.exprlist[self.exprcount]))):
                            if x == 70:
                                for r, z in list(enumerate(self.exprlist[self.exprcount])):
                                    if z == 69:
                                        temp2 = self.exprlist[self.exprcount][r+1:e]
                                        break
                                break
                        indexnow = indextemp
                        temp3 = self.exprlist[self.exprcount+1:]
                        self.exprlist[self.exprcount] = temp2
                        self.exprlist = [temp2]
                        tempexprcount = self.exprcount
                        parencount = 1
                        self.exprcount = 0
                        self.expr(1)
                        self.exprcount = tempexprcount
                        temp2 = self.exprlist
                        self.exprlist = temp
                        temp2 = ['(']+temp2+[')']
                        self.exprlist[self.exprcount:self.exprcount+1] = temp2
                        self.exprcount += len(temp2)+1
                        break
                        print(self.exprlist, end='')
                    else:
                        self.exprlist[self.exprcount] = 'Wrong token'
                    self.exprcount += 2
                    return
            indexnow += 1

    def logical_or_expr(self, token3, indexagain):
        if token3 == 54:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '-',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '-', self.exprlist[self.exprcount][countagain+2:]]

    def logical_and_expr(self, token3, indexagain):
        if token3 == 53:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '-',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '&&', self.exprlist[self.exprcount][countagain+2:]]

    def equality_expr(self, token3, indexagain):
        if token3 == 46:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '==',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '==', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 47:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '!=',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '!=', self.exprlist[self.exprcount][countagain+2:]]

    def relational_expr(self, token3, indexagain):
        if token3 == 48:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '>',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '>', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 49:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '<',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '<', self.exprlist[self.exprcount][countagain+2:]]
        if token3 == 50:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '>=',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '>=', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 51:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '<=',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '<=', self.exprlist[self.exprcount][countagain+2:]]

    def additive_expr(self, token3, indexagain):
        if token3 == 39:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '+',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '+', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 40:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '-',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '-', self.exprlist[self.exprcount][countagain+2:]]

    def multiplicative_expr(self, token3, indexagain):
        if token3 == 41:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '*',
                                 self.exprlist[self.exprcount][countagain+2:]]
                listagain2 = self.exprlist[countagain+1:]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '*', self.exprlist[self.exprcount][countagain+2:]]
                listagain2 = self.exprlist[countagain+1:]
        elif token3 == 42:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '/',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '/', self.exprlist[self.exprcount][countagain+2:]]
        if token3 == 43:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '~',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '~', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 44:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '%',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '%', self.exprlist[self.exprcount][countagain+2:]]

    def unary_expr(self, token3, indexagain):
        if token3 == 55:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '++',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '++', self.exprlist[self.exprcount][countagain+2:]]
        elif token3 == 56:
            listagain = []
            countagain = 0
            if len(self.exprlist) == 1:
                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x

                self.exprlist = [listagain, '--',
                                 self.exprlist[self.exprcount][countagain+2:]]
            else:

                for x in range(0, indexagain):
                    listagain.append(self.exprlist[self.exprcount][x])
                    countagain = x
                self.exprlist[self.exprcount:self.exprcount+1] = [listagain,
                                                                  '--', self.exprlist[self.exprcount][countagain+2:]]

    def term(self, token):
        if token in [27, 28, 29, 30]:
            return self.consts(token)
        elif token == 0:
            return 'ID'
        else:
            print('Wrong token!')

    def var(self, token):
        if token == 0:
            if token == 67:
                print(' <id> ', end='')
                print(' [ ', end='')
                self.expr()
                print(self.exprlist[0], end='')
                self.removeall()
                if self.tokens[self.tokennum] == 68:
                    print(' ] ', end='')
                    self.tokennum += 1
                else:
                    print('Error! missing some ]')

            else:
                return '<id>'

    def consts(self, token):
        if token == 27:
            return 'Intedyer'
        elif token == 28:
            return 'Karosa'
        elif token == 75:
            return 'Literal'
        elif token == 30:
            return 'Kar'

    def semicolonrec(self):
        print('Error! missing some \';\'')
tokenss = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 8, 10, 6, 99]
tokens2 = manaCode5.tokennumbers()
pars = parse(tokens2, 0)
pars.main()

'''
TOKENS AT TOKEN NUMBERS
id = 0, 
angkat = 1
at = 2
bilang = 3
bumalik = 4
diloob = 5
eksp = 6
habang =7 
hait = 8
iba =9
int = 10
isubok=11
kar = 12
karosa =13
kapagdi=14
klase=15
liban =16
limbag=17
loob=18
pag=19
para=20
pisi=21
tanggap=22
huwad=23
tumpak=24
tuwiran=25
wala=26
intedyer=27
karosaconst=28
pisi=29
karakter=30
onent=31
edyer=32
pa=33
ini=34
ka=35
akter=36
sa=37
in=38
+ =39
- =40
* =41
/ =42
~ =43
% =44
^ =45
== = 46
!= = 4
> =48
< =49
>= =50
<= = 51
! = 52
&& = 53
|| = 54
++  = 55
-- = 56
= = 57
+= = 58
*= = 59
-= = 60
/= = 61
%= = 62
~= = 63
^= = 64
{ = 65
} = 66
[ = 67 
] = 68
( = 69
) =70
: = 71
; = 72
, = 73
main = 74
literal = 75
endoffile = 100
'''

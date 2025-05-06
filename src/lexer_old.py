from utils import *

words='qwertyuiopasdfghjklzxcvbnmΔ'
words+=words.upper()
numbers='0123456789'
syntax='{}[]()\',:"    \t.'
opators='!@#$%^&*_+-=|/\\<>'

linEnds='\n;'
keyword=('if','fn','type','opt','return','true','false','enum','loop','break','while','continue','next','gen','yield','for','pub','prv')
blocks={'(':')','[':']','{':'}'}
commentsConfig=[('#','\n'),('//','\n'),('##','##'),("'","'")]
commentsConfig.sort(key=lambda value:len(value[0]),reverse=True)
commentsBegin=[comment[0] for comment in commentsConfig]
commentsEnd={b:e for b,e in commentsConfig}

def lexer(input:str)->list[token]:
    lexed:list[token]=[]


    line=1
    column=0

    # Tokenization

    for char in input:
        column+=1

        if char in words:
            kind=tokenKind.word
        elif char in numbers:
            kind=tokenKind.number
        elif char in opators:
            kind=tokenKind.operator
        elif char in syntax:
            kind=tokenKind.syntax
        elif char in linEnds:
            kind=tokenKind.newLine
        else:
            print(f'error: unknown char {char.__repr__()} at {line}:{column}')
            quit(1)

        lexed.append(token(kind,char,Location(line,column)))

        if char=='\n':
            line+=1
            column=0

    oldLexed:list[token]=lexed
    lexed:list[token]=[]

    # strings and comments
    i=0
    print(oldLexed)
    while i<len(oldLexed):
        tok=oldLexed[i]
        
        check=False #tok.symbol in commentsBegin

        for comment in commentsBegin:
            if tok.symbol==comment[0]:
                if len(comment)==1:
                    check=True
                else:
                    for ii in range(1,len(comment)):
                        if oldLexed[i+ii].symbol!=commentsBegin[ii]:
                            break
                    else:
                        check=True

        if check:

            start=i+1
            endTok=token(None,None,None)
            end=start

            check=False

            while not(check and (oldLexed[end-1].symbol!='\\' or tok.symbol!="'")):
                check=False
                
                if endTok.symbol==comment[0]:
                    if len(comment)==1:
                      check=True
                    else:
                        for ii in range(1,len(comment)):
                            if oldLexed[end+ii].symbol!=commentsBegin[ii]:
                                break
                        else:
                            check=True
                if check:
                    break
                try: endTok=oldLexed[end]
                except IndexError:
                    print(f'error: string or comment at {tok.location} never closed')
                    quit(1)

                end+=1
            if tok.symbol=="'":
                string=''
                for piece in oldLexed[start:end-1]:
                    if piece.symbol[0]=='\\':
                        assert False
                    string+=piece.symbol
                lexed.append(token(tokenKind.string,string,tok.location))
            i+=end-start
        else:
            lexed.append(tok)
        i+=1


    oldLexed:list[token]=lexed
    lexed:list[token]=[]
    # token merging
    for i,tok in enumerate(oldLexed):
        
        if len(lexed)!=0 and tok.kind!=tokenKind.syntax and (
            tok.kind==lexed[-1].kind or 
            (tok.kind in (tokenKind.number,tokenKind.word) and lexed[-1].kind  in (tokenKind.number,tokenKind.word)) or
            (tok.symbol=='.' and lexed[-1].kind  in (tokenKind.number,tokenKind.word))
            ):
                lexed[-1].symbol+=tok.symbol
        else:
            lexed.append(tok)


    # code blocks

    return lexed


"""

    oldLexed:list[token]=lexed
    lexed:list[token]=[]

    # strings
    i=0
    while i<len(oldLexed):
        tok=oldLexed[i]

        if tok.symbol=="'":
            start=i+1
            endTok=token(None,None,None)
            end=start
            while not(endTok.symbol=="'" and oldLexed[end-1].symbol!='\\'):
                try: endTok=oldLexed[end]
                except IndexError:
                    print(f'error: string at {tok.location.line}:{tok.location.column} never close')
                    quit(1)

                end+=1

            string=''

            for piece in oldLexed[start:end-1]:
                if piece.symbol[0]=='\\':
                    assert False
                string+=piece.symbol
            lexed.append(token(tokenKind.string,string,tok.location))
            i+=end-start
        else:
            lexed.append(tok)
        i+=1


"""
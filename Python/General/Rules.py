open_brackets = [
    "(",
    "[",
    "{"
]
close_brackets = [
    ")",
    "]",
    "}"
]
brackets = open_brackets + close_brackets



simple_rules = {
    "P and Q":"Q and P",                                        #COMMUNATIVE and
    "P or Q":"Q or P",                                          #COMMUNATIVE or
    "( P and Q ) and R":"P and ( Q and R )",                    #ASSOSIATIVE and
    "( P or Q ) or R":"P or ( Q or R )",                        #ASSOSIATIVE or
    "not P and not Q": "not ( P or Q )",                        #DE MORGAN 1
    "not P or not Q": "not ( P and Q )",                        #DE MORGAN 2
    "P => Q":"not P or Q",                                      #Implication
    "not ( not P ) ":"P",                                       #Double Negation
    "P <=> Q":"( P => Q ) and ( Q => P )",                      #Def of Equivilence
    "P":"P or Q",                                               #Addition
}
complex_rules = {
    "P , P => Q": "Q",                                          #Moden Ponens
    "not Q , P => Q": "not P" ,                                 #Moden Tolens
    "P, Q": "P and Q",                                          #Conjunction
    "P and Q":"P, Q",                                           #Simplification
    "A => B , B => C": "A => C"                                 #Hypothetical Syllogism- HS
}


keyTokens = {
    "or": "or",
    "and": "and",
    "(": "(",
    ")": ")",
    "not":"not",
    "nor":"nor",
    "nand":"nand",
    "xor":"xor",
    "=>":"=>",
    "=":"="
}
grammar Expr;
options{
language=Python3;
}
/** The start rule; begin parsing here. */
prog:   stat+ ; 

stat:   expr NEWLINE            #STATE_EXPR   
    |   ID '=' expr NEWLINE     #STATE_ID   
    |   NEWLINE                 #STATE_NEWLINE  
    ;

expr:   expr ('*'|'/') expr   #EXPR_MD
    |   expr ('+'|'-') expr   #EXPR_AM
    |   INT                   #EXPR_INT 
    |   ID                    #EXPR_ID
    |   '(' expr ')'          #EXPR_C
    ;

ID  :   [a-zA-Z\u4f60]+ ;      // match identifiers <label id="code.tour.expr.3"/>
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace

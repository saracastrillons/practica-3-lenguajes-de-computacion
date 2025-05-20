
import re
PIEZA = r"[KQRBN]"  
CASILLA = r"[a-h][1-8]"  
DIGITO = r"[1-9]\d*"  

DESAMB = r"(?:[a-h]|\d|[a-h][1-8])"  
CAPT = r"x"  
PROM = r"(?:=[KQRBN])?"  
JAQ = r"[+#]?"  


ENROQUE_RE = re.compile(r"^(O-O|O-O-O)$")
MOV_PIEZA_RE = re.compile(rf"^{PIEZA}{DESAMB}?{CAPT}?{CASILLA}{PROM}{JAQ}$")
MOV_PEON_AV_RE = re.compile(rf"^{CASILLA}{PROM}{JAQ}$")
MOV_PEON_CAP_RE= re.compile(rf"^[a-h]x{CASILLA}{PROM}{JAQ}$")

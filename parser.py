import re
from san_grammar import ENROQUE_RE, MOV_PIEZA_RE, MOV_PEON_AV_RE, MOV_PEON_CAP_RE

class SANParser:
    def __init__(self, text):
        self.text = text.strip()

    def parse(self):
        
        turns = []
        TURN_RE = re.compile(r'(\d+)\.\s*([^\s]+)(?:\s+([^\s]+))?')
        for m in TURN_RE.finditer(self.text):
            num = int(m.group(1))
            for idx, jug in enumerate((m.group(2), m.group(3))):
                if not jug:
                    continue
                if not self._valid_move(jug):
                    color = 'blancas' if idx == 0 else 'negras'
                    reason = self._reason_invalid(jug)
                    raise ValueError(f"Jugada inválida: '{jug}' en turno {num} ({color}): {reason}")
            turns.append((num, m.group(2), m.group(3)))
        return turns

    def _valid_move(self, m):
        for regex in (ENROQUE_RE, MOV_PIEZA_RE, MOV_PEON_AV_RE, MOV_PEON_CAP_RE):
            if regex.fullmatch(m):
                return True
        return False

    def _reason_invalid(self, m):
        if m.startswith('O-O') and m not in ('O-O', 'O-O-O'):
            return "enroque inválido"
        if '=' in m and not re.search(r'=[KQRBN]$', m):
            return "promoción inválida"
    
        cas = re.search(r'([a-zA-Z])(\d)', m)
        if cas:
            letra, num = cas.groups()
            if letra.lower() not in 'abcdefgh':
                return f"columna inválida '{letra}'"
            if num not in '12345678':
                return f"fila inválida '{num}'"
    
        if m.startswith('P') and not ENROQUE_RE.fullmatch(m):
            return "no usar 'P' para peones"

        return "no coincide con ninguna regla de SAN"

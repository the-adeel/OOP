class DNABase:
    def __init__(self, nucleotide):
        self.base = nucleotide

    @staticmethod
    def _valid_base_setup(self, input_val):
        allowed = [('a', 'adenine'),('c', 'cystosine'), ('g', 'guanine'), ('t', 'thymine')]
        
        for b in allowed:
            if input_val.lower().strip() in b:
                return b[1]
            
            return False
        
    def set_base(self, base):
        final_base = self._valid_base_setup(base)

        if final_base:
            self._base = final_base
        else:
            raise ValueError(f"{base} is not a recognised DNA nucleotide")
        
    def get_base(self):
        return self._base
    
    base = property(fget=get_base, fset=set_base)

    def __repr__(self):
        return f"{type(self).__name__}(nucleotide={self.base})"

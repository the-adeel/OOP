class Contact:
    def __init__(self, fname, lname, ph = None, email = None, display_mode = "masked"):
        self.fname = fname
        self.lname = lname
        self.ph = ph
        self.email = email
        self.display_mode = display_mode
    
    def __format__(self, format_spec):
        if format_spec == "unmasked":
            self.display_mode = "unmasked"
            return repr(self)

    def __eq__(self, other):
        if self.ph or self.email:
            return self.ph == other.ph or self.email == other.email
        else:
            return self.fname == other.fname or self.lname == other.lname
        
    def __repr__(self):
        lf = len(self.fname) - 2
        ll = len(self.lname) - 1
        if self.display_mode == "masked":
            return f"Contact({self.fname[0]}{self.fname[1]}{('*' * lf)}, {self.lname[0]}{('*' * ll)})"
        else:
            return f"{self.fname}, {self.lname}, {self.ph}, {self.email}"
        
    def __str__(self):
        return f"{self.fname[0]}{self.lname[0]}"

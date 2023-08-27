from molextract.rule import Rule


class SCFEnergy(Rule):
    START_TAG = "::    Total SCF energy"
    END_TAG = "\s+"

    def __init__(self):
        super().__init__(self.START_TAG, self.END_TAG)
        self.state = {"total_scf_energy": None, "one_e_energy": None,
                      "two_e_energy": None}

    def process_lines(self, start_line: str):
        for line in self:
            last = line.split()[-1]
            if "Total SCF energy" in line:
                self.state["total_scf_energy"] = float(last)
            elif "One-electron energy" in line:
                self.state["one_e_energy"] = float(last)
            elif "Two-electron energy" in line:
                self.state["two_e_energy"] = float(last)

    def reset(self):
        tmp = self.state.copy()
        self.state = {"total_scf_energy": None, "one_e_energy": None,
                      "two_e_energy": None}
        return tmp
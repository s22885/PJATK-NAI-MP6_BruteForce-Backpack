class Backpack:
    data: list
    curr_agr: list
    tmp_agr: list
    curr_val: float
    ia: int

    def __init__(self, data: list):
        self.data = data
        self.tmp_agr = [0 for i in range(data[1])]
        self.curr_val = 0

    def calc(self, pos, val):
        if self.data[1] == pos:
            self.ia += 1
            tmp_val = 0
            tmp_wei = 0
            for i in range(self.data[1]):
                if self.tmp_agr[i]==1:
                    tmp_val+=self.data[3][i]
                    tmp_wei+=self.data[2][i]
            if tmp_wei <= self.data[0]:
                if tmp_val > self.curr_val:
                    print(f"iteration:({self.ia}), size=({tmp_wei}), value=({tmp_val}), node = {self.tmp_agr}")
                    self.curr_agr = self.tmp_agr.copy()
                    self.curr_val = tmp_val
            return
        else:
            if pos != -1:
                self.tmp_agr[pos] = val
            tmp_pos = pos + 1
            self.calc(tmp_pos, 0)
            self.calc(tmp_pos, 1)

    def start(self):
        self.ia = 0
        self.calc(-1, 0)

    @staticmethod
    def create_Backpack(data: list):
        if len(data) != 4:

            return None
        if len(data[3]) != data[1] or len(data[2]) != data[1]:
            return None
        return Backpack(data)

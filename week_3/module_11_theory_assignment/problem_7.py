class Get_unique_subset:
    def sub_sets(self, sset):
        return self.generate_unique_sset([], sorted(sset))
    
    def generate_unique_sset(self, current, sset):
        if sset:
            return self.generate_unique_sset(current, sset[1:]) + self.generate_unique_sset(current + [sset[0]], sset[1:])
        return [current]

print(Get_unique_subset().sub_sets([4,5,6]))

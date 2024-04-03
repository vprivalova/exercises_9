class StrandsDNA:
    all_strands = []

    @staticmethod
    def add_strands(strands):
        StrandsDNA.all_strands.extend(strands.split())

    @staticmethod
    def get_max_strands():
        mx_length = 0
        result = []
        for elem in StrandsDNA.all_strands:
            if len(elem) > mx_length:
                mx_length = len(elem)

        for elem in StrandsDNA.all_strands:
            if len(elem) == mx_length:
                if elem not in result:
                    result.append(elem)
        result.sort()
        return ' '.join(result)


dna = StrandsDNA()
dna.add_strands('dnbdnd nkljioklk nnb mkmj nnm nnm kjuytrlkm')
print(dna.get_max_strands())

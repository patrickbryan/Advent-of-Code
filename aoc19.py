def day19a():
    rules = [['Al', 'ThF'], ['Al', 'ThRnFAr'], ['B', 'BCa'], ['B', 'TiB'], ['B', 'TiRnFAr'], ['Ca', 'CaCa'], ['Ca', 'PB'], ['Ca', 'PRnFAr'], ['Ca', 'SiRnFYFAr'], ['Ca', 'SiRnMgAr'], ['Ca', 'SiTh'], ['F', 'CaF'], ['F', 'PMg'], ['F', 'SiAl'], ['H', 'CRnAlAr'], ['H', 'CRnFYFYFAr'], ['H', 'CRnFYMgAr'], ['H', 'CRnMgYFAr'], ['H', 'HCa'], ['H', 'NRnFYFAr'], ['H', 'NRnMgAr'], ['H', 'NTh'], ['H', 'OB'], ['H', 'ORnFAr'], ['Mg', 'BF'], ['Mg', 'TiMg'], ['N', 'CRnFAr'], ['N', 'HSi'], ['O', 'CRnFYFAr'], ['O', 'CRnMgAr'], ['O', 'HP'], ['O', 'NRnFAr'], ['O', 'OTi'], ['P', 'CaP'], ['P', 'PTi'], ['P', 'SiRnFAr'], ['Si', 'CaSi'], ['Th', 'ThCa'], ['Ti', 'BP'], ['Ti', 'TiTi'], ['e', 'HF'], ['e', 'NAl'], ['e', 'OMg']]
    molecule = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
    uniqueMolecules = []

    for rule in rules:
        i = 1
        mIndex = find_nth_overlapping(molecule, rule[0], i)
        while (mIndex > -1):
            newMolecule = replaceNth(molecule, rule[0], rule[1], i)
            if newMolecule not in uniqueMolecules:
                uniqueMolecules.append(newMolecule)
            i += 1
            mIndex = find_nth_overlapping(molecule, rule[0], i)
    
    print (len(uniqueMolecules))

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def replaceNth(s, source, target, n):
    inds = [i for i in range(len(s) - len(source)+1) if s[i:i+len(source)]==source]
    if len(inds) < n:
        return  # or maybe raise an error
    s = list(s)  # can't assign to string slices. So, let's listify
    s[inds[n-1]:inds[n-1]+len(source)] = target  # do n-1 because we start from the first occurrence of the string, not the 0-th
    return ''.join(s)

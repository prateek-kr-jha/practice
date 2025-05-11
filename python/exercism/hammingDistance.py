def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    return sum(data_point_a != data_point_b for data_point_a, data_point_b in zip(strand_a, strand_b) )


print(distance("GGACGGATTCTG", "AGGACGGATTCT"))
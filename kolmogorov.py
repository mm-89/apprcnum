import zlib

def kolmogorov_complexity(string):
    """
    Based on the slides:
    https://github.com/xbeat/Machine-Learning/blob/main/Kolmogorov%20Complexity%20and%20Algorithmic%20Randomness%20in%20Python.md
    """
    return len(zlib.compress(string.encode('utf-8')))

def normalized_information_distance(string1, string2):
    """
    Based on Paul M. B et al. 2008 (chapter 3) 
    (equation 3.3)
    https://arxiv.org/abs/0809.2553
    """
    c_x = kolmogorov_complexity(string1)
    c_y = kolmogorov_complexity(string2)
    c_xy = kolmogorov_complexity(string1 + string2)
    c_yx = kolmogorov_complexity(string2 + string1)
    
    # Approssimazione per la complessità condizionale
    k_x_y = c_xy - c_y
    k_y_x = c_yx - c_x
    
    return max(k_x_y, k_y_x) / max(c_x, c_y)

def normalized_compression_distance(string1, string2):
    """
    Based on Paul M. B et al. 2008 (chapter 3)
    (equation 3.5)
    https://arxiv.org/abs/0809.2553
    """
    c_x = kolmogorov_complexity(string1)
    c_y = kolmogorov_complexity(string2)
    c_xy = kolmogorov_complexity(string1 + string2)
    
    return (c_xy - min(c_x, c_y)) / max(c_x, c_y)

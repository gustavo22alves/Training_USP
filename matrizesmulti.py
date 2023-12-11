# m1 = [[1],[3],[5]]
# m2 = [[1,2,3]]



def sao_multiplicaveis(m1, m2):
    num_colunas_m1 = len(m1[0])
    num_linhas_m2 = len(m2)
    
    if num_colunas_m1 == num_linhas_m2:
        return True
    else:
        return False
    
# print(sao_multiplicaveis(m1,m2))
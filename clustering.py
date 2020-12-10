import numpy as np
import pandas as pd
import sklearn.cluster as cluster
import scipy.spatial.distance as sdist

def novo_centroide(d):
  
    div0 = d.loc[d['cluster'] == 0].mean()
    div1 = d.loc[d['cluster'] == 1].mean()
    div2 = d.loc[d['cluster'] == 2].mean()

    novo_centroides = np.array([[div0[0],div0[1]],
                                [div1[0],div1[1]],
                                [div2[0],div2[1]]])

    #print(div0)
    #print(div1)
    #print(div2)
    #print(novo_centroides)

    return novo_centroides

def kmeans(pontos, centroide):
    #1ª iteracao
    #criação do dataframe e centroides
    print("Primeira iteração")
    df = pd.DataFrame(pontos)
    #setup de kmeans
    kmeans = cluster.KMeans(n_clusters=3, init=C, n_init=1, max_iter=3, random_state=0).fit(pontos)
    #definição de qual cluster 
    df['cluster'] = kmeans.labels_
    #distancia euclidiana em relação a cada centroide
    distsf = pd.DataFrame(sdist.cdist(pontos, centroide), columns=['dist_{}'.format(i) for i in range(len(centroide))], index=df.index)
    df = pd.concat([df, distsf], axis=1)
    print(df)

    #2ª iteracao
    #criação do dataframe e centroides
    print("Segunda iteração")
    dg = pd.DataFrame(pontos)
    #setup de kmeans
    centroide_n = novo_centroide(df)
    kmeans = cluster.KMeans(n_clusters=3, init=centroide_n, n_init=1, max_iter=3, random_state=0).fit(pontos)
    #definição de qual cluster 
    dg['cluster'] = kmeans.labels_
    #distancia euclidiana em relação a cada centroide
    distsg = pd.DataFrame(sdist.cdist(pontos, centroide_n), columns=['dist_{}'.format(i) for i in range(len(centroide_n))], index=dg.index)
    dg = pd.concat([dg, distsg], axis=1)
    print(dg)

    #3ª iteracao
    #criação do dataframe e centroides
    print("Segunda iteração")
    ds = pd.DataFrame(pontos)
    #setup de kmeans
    centroide_m = novo_centroide(dg)
    kmeans = cluster.KMeans(n_clusters=3, init=centroide_m, n_init=1, max_iter=3, random_state=0).fit(pontos)
    #definição de qual cluster 
    ds['cluster'] = kmeans.labels_
    #distancia euclidiana em relação a cada centroide
    distss = pd.DataFrame(sdist.cdist(pontos, centroide_m), columns=['dist_{}'.format(i) for i in range(len(centroide_m))], index=ds.index)
    ds = pd.concat([ds, distss], axis=1)
    print(ds)

    return df, dg, ds


X = np.array([[1.9,7.3], 
        [3.4,7.5], 
        [2.5,6.8],
        [1.5,6.5],
        [3.5,6.4],
        [2.2,5.8],
        [3.4,5.2],
        [3.6,4],
        [5,3.2],
        [4.5,3.2],
        [6,2.6],
        [1.9,3],
        [1,2.7],
        [1.9,2.4],
        [0.8,2],
        [1.6,1.8],
        [1,1]])

C = np.array([[1,5],
              [0.5,1.5],
              [3.7,2.3]])
              
(t,d,f)  = (kmeans(X,C))


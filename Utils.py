def cluster(df):
    import math
    from sklearn.cluster import KMeans
    df.columns = ['ID', 'Latitude', 'Longitude', 'isSOS', 'isCamp', 'isUnsafe']
    #print(df)
    # df1=df['isSOs'==0,'isCamp'==0,'isUnsafe'==0]
    df1 = df.loc[df['isSOS'] == 0]
    df1 = df1.loc[df1['isCamp'] == 0]
    df1 = df1.loc[df1['isUnsafe'] == 0]
    df1 = df1.iloc[:, 0:3]
    minlat = df1['Latitude'].min()
    maxlat = df1['Latitude'].max()
    minlong = df1['Longitude'].min()
    maxlong = df1['Longitude'].max()
    # print(minlat,maxlat,minlong,maxlong)
    spanlat = maxlat - minlat
    # print(spanlat)
    spanlong = maxlong - minlong
    k1 = spanlat / 0.017
    k2 = spanlong / 0.017
    k = math.ceil(k1 * k2)
    # print(k)

    kmeans = KMeans(n_clusters=5, random_state=0).fit(df1.iloc[:, 1:3])
    labelss = kmeans.labels_
    clus_centres = kmeans.cluster_centers_
    # print(clus_centres)
    dict1 = []
    for i in range(len(clus_centres)):
        temp = {"icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png", 'lat': clus_centres[i][0],
                "lng": clus_centres[i][1], 'infobox': None}
        dict1.append(temp)
    arr = df.values
    for i in range(arr.shape[0]):
        if arr[i][3] == 1:
            temp = {"icon": "http://maps.google.com/mapfiles/ms/icons/red-dot.png", 'lat': arr[i][1], "lng": arr[i][2],
                    'infobox': None}
            dict1.append(temp)
        if arr[i][4] == 1:
            temp = {"icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png", 'lat': arr[i][1],
                    "lng": arr[i][2], 'infobox': None}
            dict1.append(temp)
        if arr[i][5] == 1:
            temp = {"icon": "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png", 'lat': arr[i][1],
                    "lng": arr[i][2], 'infobox': None}
            dict1.append(temp)

    return dict1

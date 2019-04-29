###Find the clustering of the Big-4 Tech Companies
details_df.loc[details_df['name']== 'GOOG', ['name','cluster']]

details_df.loc[details_df['name']== 'AAPL', ['name','cluster']]

details_df.loc[details_df['name']== 'MSFT', ['name','cluster']]

details_df.loc[details_df['name']== 'FB', ['name','cluster']]


##Find the length of all 4 clusters
print(len(details_df.loc[details_df['cluster']== 0, ['name','cluster']]))
print(len(details_df.loc[details_df['cluster']== 1, ['name','cluster']]))
print(len(details_df.loc[details_df['cluster']== 2, ['name','cluster']]))
print(len(details_df.loc[details_df['cluster']== 3, ['name','cluster']]))
print(len(details_df.loc[details_df['cluster']== 4, ['name','cluster']]))
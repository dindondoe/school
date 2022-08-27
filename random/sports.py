
def medals_by_gender(countries=['Japan']):
    
    #scatterplot with count_male as X-axis and count_female as Y-axis, type of medal is a colour
    chart = alt.Chart(medal_count_by_gender.loc[medal_count_by_gender['Team/NOC'].isin(countries)], 
                      title='Total medals earned by female and male athlets').mark_circle(size=300).encode(
        x=alt.X('count_male', title='Male Athlets'),
        y=alt.Y('count_female', title='Female Athlets'),
        color=alt.Color('Medal type',
                        scale=alt.Scale(domain=['Gold','Silver','Bronze'],
                                        range=['orange','grey','brown'])),
        tooltip=['Team/NOC', 'Medal type','count_female','count_male']
    ).properties(
        width=600,
        height=400
    )
    
    #adding a line to devide areas with more female medals vs more male medals
    line = alt.Chart(pd.DataFrame({'var1': [0, 30], 'var2': [0, 30]})
                    ).mark_line(color='grey',
                                opacity=.3,
                                strokeDash=[5,5]
                               ).encode(alt.X('var1'),
                                        alt.Y('var2')
                                       )
    return chart+line


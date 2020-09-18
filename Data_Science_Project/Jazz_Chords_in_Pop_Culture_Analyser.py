def Jazz_Chords_in_Pop_Culture_Analyser():
    import pandas as pd
    import csv
    import matplotlib.pyplot as plt
    import numpy as np

    # url = 'https://en.wikipedia.org/wiki/List_of_Billboard'+ term + elem
    # df = pd.read_html(url)
    def billboard_to_pickle():
        import pandas as pd
        groups = ['_of_the_1940s', '_from_1950_to_1958', '_from_1958_to_1969' \
            , '_of_the_1970s', '_of_the_1980s', '_of_the_1990s', '_of_the_2000s', \
                  '_of_the_2010s', '_of_the_2020s']
        term1 = '_number-one_singles'
        term2 = '_Hot_100_number-one_singles'
        wiki_num = 3
        x = 0
        for elem in groups:
            term = term1
            if x > 1:
                term = term2
            url = 'https://en.wikipedia.org/wiki/List_of_Billboard' + term + elem
            df = pd.read_html(url)
            df = df[wiki_num]
            new_cols = [x[0] for x in df.columns]
            df.columns = new_cols
            df.rename(columns={'Reachednumber one': 'Reached number one', 'Issue date': 'Reached number one',
                               'Weeks atnumber one': 'Weeks at number one', 'Weeks atNo. 1[B]': 'Weeks at number one',
                               'Single[B]': 'Single', 'Artist(s)[B]': 'Artist(s)'}, inplace=True)
            for col in ['Reference', 'References', 'Ref', '#', 'No.', 'Unnamed: 5_level_0', 'Unnamed: 6_level_0',
                        'Record label']:
                if col in df.columns:
                    df = df.drop(columns=[col])
            wiki_num = 2
            print(elem)
            if x == 0:
                df_ = df
            else:
                df_ = pd.concat([df_, df])
            x += 1
        years = [str(x) for x in range(1940, 2021)]
        df_ = df_[~df_.isin(years)].dropna()
        print(df_)
        df_.to_pickle("billboard.pkl")

    def string_df_to_df():
        chh = ["Chord_" + str(p) for p in range(39)]
        DF_ = pd.DataFrame(columns=['Artist(s)', 'Single'] + chh)
        print(DF_)
        rows = []
        for v in range(330):
            row = ['']
            chrds = open('chrds', 'r')
            for line in chrds:
                # print(line.split(" ")[0])
                # print(str(v))
                if line.split(" ")[0] == str(v):
                    # print(line)
                    for lip in line.split("  "):
                        if lip not in row:
                            row.append(lip.split("\n")[0])
            c_row = [s for s in row if s != '']
            print(c_row)
            DF_row = pd.DataFrame([c_row], columns=['Artist(s)', 'Single'] + chh[:len(c_row) - 2])
            if v == 0:
                DF_ = DF_row
            else:
                DF_ = pd.concat([DF_, DF_row], axis=0, ignore_index=True)
            print(DF_)
        DF_.to_pickle("chords_p1.pkl")

    def join_data():
        df_a = pd.read_pickle("chords_p1.pkl")
        df_b = pd.read_pickle("chords_p2.pkl")
        #print(df_a.columns,df_b.columns)
        df_a1 = df_a.drop(columns=['Artist(s)'])
        df_a1.columns = df_a.columns[:-1]
        #print(df_a1.head(),"\n\n", df_b.head())
        df_chfl = pd.concat([df_a1, df_b], axis=0, ignore_index=True)
        df_chfl.index = [x for x in range(len(df_chfl))]
        #print(df_chfl.head(),"\n\n",df_chfl.tail())
        df_chfl.to_pickle("chords.pkl")
    #join_data()

    def data_clean(data):
        df_chord = data
        #df_chord = pd.read_pickle("/Users/g/Desktop/Datasets/chords.pkl")
        # replace_terms = ['[Chorus]','[Bridge]','']
        # for term in replace_terms:
        # df_chord = df_chord.replace(term,np.nan)
        cut_list = ['Capo', 'Break', 'Chorus', 'Bridge', 'NaN', 'Finale', 'Chords', 'Coda' \
            , 'Bring', 'OPEN', 'DUUD', 'DUU', 'DD', 'Again', 'Baby!', '{P.Diddy}', 'Diddy' \
            , 'Bass', 'CHORDS', 'VErse', 'Verse', 'Don\'t', 'Girl', 'Fill', 'Bend', 'VERSE' \
            , 'Dia-na!', 'CHORUS', 'BRIDGE', 'KEY', 'Key', 'Baby', 'End', 'END', 'DGBE', 'Bennie' \
            , 'Brown', 'SUNG', 'NC', '\\t', 'Crept', 'Go', 'Convoy', 'ing', 'Aah', 'Deep', 'RIFF' \
            , 'Riff', 'Fade', 'CHO', 'OOWWEEE', 'TABS', 'Chorous', 'Fall', 'GUITAR', 'Enjoy','UUD','Fergie' \
            ,'Cold','\'Cause','!', 'Ashanti', 'PRIE','CAPO','TELSTAR','BREAK','BALTIMORE','Donate','SONG' \
            ,'Ahhhhh','Best','Dme','DATE']
        for x in range(38):
            col = 'Chord_' + str(x)
            df_chord[col] = df_chord[col].astype(str)
            # for cut in cut_list:
            # df_chord[col] = df_chord[col].replace(cut,np.nan)
            # df_chord[col] = df_chord[col].astype(str)
            new_lis = []
            lis = df_chord[col].tolist()
            for x in range(len(lis)):
                # new_lis.append(lis[x].split("[")[0].split("|")[0])
                l = lis[x]
                for y in '[]|():*\t.-,{}':
                    l = l.replace(y, '')
                for cut in cut_list:
                    l = l.replace(cut, '')
                new_lis.append(l)
                # new_lis.append(lis[x].replace("[")[0].split("|")[0])
            df_chord[col] = new_lis
        df_chord = df_chord.replace('', np.nan).replace(' ', np.nan)
        #print(df_chord)
        return df_chord
        #df_chord.to_pickle("/Users/g/Desktop/Datasets/cho.pkl")

    def data_merge():
        df_chord = pd.read_pickle("chords.pkl")
        df_chord = df_chord.set_index(['Artist(s)', 'Single'])
        # print(df_chord)
        df_bill = pd.read_pickle("billboard.pkl")
        # print(df_bill)
        df_bill = df_bill.set_index(['Artist(s)', 'Single'])
        # print(df_bill)
        df_full = df_bill.merge(df_chord, how='left', left_index=True, right_index=True)
        df_full = df_full.reset_index()
        df_full['Reached number one'] = pd.to_datetime(df_full['Reached number one'])
        df_full = df_full.sort_values('Reached number one')
        df_full.index = [x for x in range(len(df_full))]
        # print(df_full.head(),"\n\n",df_full.tail())

    def data_chord_col(data):
        cols = []
        xe = []
        chhh = []
        for x in range(50):
            cols.append(list(map(str, data["Chord_" + str(x)].tolist())))
        for x in range(len(data)):
            chhhe = ''
            for col in cols:
                # if all(col != x for x in ['nan','NaN']):
                chhhe += col[x] + ","
            xe.append(chhhe.split(",nan")[0].split("nan")[0].replace(" ", ''))
        # for nan in xe:
        # nan.replace(",nan",'')
        # print(xe)
        data['Chords'] = xe
        data = data[[ 'Artist(s)', 'Single', 'Chords']]
        print(data)
        data.to_pickle("EMPTY.pkl")

    def plot_1(data):
        def clear(x):
            if '*' in x:
                return x.replace('*', '')
            else:
                return x

        #df_proj = pd.read_pickle("/Users/g/Desktop/Datasets/project.pkl")
        df_proj = data
        df_proj['Weeks at number one'] = df_proj['Weeks at number one'].astype(str)
        df_proj['Weeks at number one'] = df_proj['Weeks at number one'].apply(clear).astype(int)
        pd.set_option('display.width', 20000)

        def seventh(x):
            if "7" in x:
                return True
            else:
                if x == '':
                    return np.nan
                else:
                    return False

        df_proj['7th'] = df_proj['Chords'].apply(seventh)
        # print(df_proj)
        yes = df_proj[df_proj['7th'] == True]
        no = df_proj[df_proj['7th'] == False]
        unknown = df_proj[df_proj['7th'].isna() == True]
        plots = [yes,no,unknown]
        colours = ['red','deepskyblue','white']
        plots = plots[0:2]
        colours = colours[0:2]
        print(yes)
        plt.figure()
        n = 0
        for plot in plots:
            data = {'a':plot['Reached number one'].tolist(),
                    'b':plot['Weeks at number one'].tolist()}
            size = [x for x in data['b']]
            plt.scatter(x='a',y='b',c=colours[n],data=data,s=size,alpha=0.2)
            n += 1
        plt.show()


    def merge_scraps():
        df_proj = pd.read_pickle("/Users/g/Desktop/Datasets/project.pkl")
        pd.set_option('display.width', 20000)
        df_empty = pd.read_pickle("/Users/g/Desktop/Datasets/empty.pkl")
        df_proj = df_proj.set_index(['Artist(s)', 'Single'])
        df_empty = df_empty.set_index(['Artist(s)', 'Single'])
        df_full = df_proj.merge(df_empty, how='left', left_index=True, right_index=True)
        df_full = df_full.reset_index()
        df_full['Reached number one'] = pd.to_datetime(df_full['Reached number one'])
        df_full = df_full.sort_values('Reached number one')
        df_full.index = [x for x in range(len(df_full))]

        def fun(x):
            if x == '':
                return df_full['Chords_x']
            else:
                return x

        for x in range(len(df_full)):
            if df_full['Chords_x'].loc[x] == '':
                df_full['Chords_x'].loc[x] = df_full['Chords_y'].loc[x]
        print(df_full.columns)
        df_full = df_full.drop(columns=['Chords_y'])
        df_full = df_full.rename(columns={'Chords_x': 'Chords'})
        df_full = df_full.replace(np.nan, '')
        df_full = df_full[['Reached number one', 'Artist(s)', 'Single', 'Weeks at number one', 'Chords']]
        df_full.to_pickle("fullt.pkl")
        print(df_full)

    def plots(data):
        plt.figure()
        data = {'a': data['Reached number one'].tolist(),
                'b': data['Weeks at number one'].tolist(),
                'c': data['7ths'].tolist()}
        size = [30 * x for x in data['b']]
        #col = [1000 * x for x in data['c']]
        plt.scatter(x='a', y='b', c='c', cmap='rainbow', data=data, alpha=0.5, s=size, label="Songs coloured by number of complex chords")
        plt.title("Chord Complexity of Billboard 100 Songs (1940-2020)")
        plt.xlabel("Date")
        plt.ylabel("Weeks at Number One")
        plt.legend()
        plt.colorbar()
        plt.show()

    def refine_df():
        df_fproj = pd.read_pickle("full_project.pkl")
        pd.set_option('display.width', 20000)
        data = df_fproj
        def clear(x):
            if '*' in x:
                return x.replace('*', '')
            else:
                return x

        data['Weeks at number one'] = data['Weeks at number one'].astype(str)
        data['Weeks at number one'] = data['Weeks at number one'].apply(clear).astype(int)

        def sevenths(val):
            if val != '':
                jazz_count = sum([val.count(str(x)) for x in range(6, 14)]) + val.count('aug') + val.count('dim')
                if jazz_count > 12:
                    jazz_count = 12
                return jazz_count
            else:
                return np.nan

        data['7ths'] = data['Chords'].apply(sevenths)
        data = data.drop_duplicates()
        print(data)
        data.to_pickle("full_project.pkl")

    df_fproj = pd.read_pickle("full_project.pkl")
    pd.set_option('display.width', 20000)
    print(df_fproj)
    plots(data=df_fproj)

Jazz_Chords_in_Pop_Culture_Analyser()

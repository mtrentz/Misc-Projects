import imdb
import csv
import re

# Used imdb API to export info of TV Show into a csv file with ShowTitle/Ep.Title/Ep.Rating/Votes/Ep.Summary etc..

imdb = imdb.IMDb()

print("Type the TV Show or Movie wanted: ")
name = input('>')

search = imdb.search_movie(name)

count = 1
print("The top five searhed items are:")
for index in search[0:5]:
    print(str(count) +". " + index['title'] + " (" + str(index['year']) + ")")
    count+=1

print("Please select the one you want: [1-5]")
selection = input('>')
select_id = search[int(selection)-1].getID()
item = imdb.get_movie(select_id)

#Add check for TVshow/movie and a way to get back to previous search
imdb.update(item, 'episodes')

item_basic_info = {
"title" : item['title'],
"type" : item['kind'],
"year" : item['year'],
"nr_seasons" : len(item['episodes'])
}

print("The selected item is: ")
print(item_basic_info['title'])
print(item_basic_info['year'])
print(item_basic_info['type'])
print("Nr. of seasons:" + str(item_basic_info['nr_seasons']))

print("Press 1. for brief version, press 2 for detailed one (Takes several minutes)")
detail_choice = int(input('>'))

print("Type the name of you final .csv file")
name_out = input('>')
name_out = re.sub("[\.+].*", "", name_out) + ".csv"

#%%
#Detailed Version (Takes forever)
if detail_choice == 2:
    id_list = []
    season_id_list = []
    for season in range(1,len(item['episodes'])+1):
        for ep in range(0,len(item['episodes'][season])+1):
            try:
                season_id_list.append(item['episodes'][season][ep].getID())
            except:
                pass
        id_list.append(season_id_list)
        season_id_list = []

    csv_file = open(name_out, 'w', newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Season', 'Ep. Number', 'Ep. Name', 'Plot', 'Rating', 'Votes'])

    for season in id_list:
        for ep in season:
            fetch_ep = imdb.get_movie(ep)
            # This is to get the plot, since there are 2 small plots and they require some changes
            plot = re.sub('[:]{2}[A-Za-z0-9_-]*', "", fetch_ep['plot'][0]) + "\n" + re.sub('[:]{2}[A-Za-z0-9_-]*', "", fetch_ep['plot'][1])
            csv_writer.writerow(
            [fetch_ep['season'], fetch_ep['episode'], fetch_ep['title'], plot, fetch_ep['plot'], fetch_ep['votes']]
            )

    csv_file.close()

#%%
    
#Brief info
elif detail_choice == 1:
    print("Creating new file")
    csv_file = open(name_out, 'w', newline = "")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Season', 'Ep. Number', 'Ep. Name', 'Plot', 'Rating', 'Votes'])

    for season in range(1,len(item['episodes'])+1):
        for ep in range(0,len(item['episodes'][season])+1):
            try:
                ep_season = item['episodes'][season][ep]['season']
                ep_epnum = item['episodes'][season][ep]['episode']
                ep_name = item['episodes'][season][ep]['title']
                ep_plot = item['episodes'][season][ep]['plot']
                ep_rating = item['episodes'][season][ep]['rating']
                ep_votes = item['episodes'][season][ep]['votes']
                csv_writer.writerow([ep_season, ep_epnum, ep_name, ep_plot, round(ep_rating,2), ep_votes])
            except:
                pass

    csv_file.close()

print("Done")
#%%    
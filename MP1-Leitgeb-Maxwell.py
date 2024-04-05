import random   # Needed for Pt 4

# You are running an online video channel. Your subscribers
# pay to watch videos on your channel of different lengths.
# You also have a competing channel - will your subscribers
# spend more time watching your videos than your competitor's?
# Who will be more successful?!

# Part 1 - Part 1 - What are the titles of the videos in your channel?
print("Part 1 - What are the titles of the videos in your channel? ")
print("Press Enter when you are done")
videos = []
title = input('Add a video title: ')


while title != '': #title input stops when the user simply hits the enter key rather than typing another title
    videos.append(title)
    title = input('Add a video title: ')

print('The titles of your videos include:', videos) #lists out all the titles


# Part 2 - How long is each video in your channel?
print("Part 2 - How long is each video in your channel?")
lengths = {}
lengths_list = []
index = 0
for i in videos:
    vid_length = float(input('How many minutes is the video ' + '"' + videos[index] + '" ?')) #User enters input for each video 
    lengths[videos[index]] = vid_length
    lengths_list.append(vid_length)
    index += 1

print('The lengths of your videos are as follows:', lengths) #Lists of lengths
print("The shortest video is", min(lengths_list), 'minutes.') #Minimum
print("The longest video is", max(lengths_list), 'minutes.') #Maximum

length_index = 0
total = 0
for i in lengths_list: #Calculation for the total minutes
    total += lengths_list[length_index]
    length_index += 1

average = total/len(lengths_list) #Calculation for the average
print('The average video length is', "{:.3f}".format(average), 'minutes.')

# Part 3 - Let's talk about subscribers!
print("Part 3 - Let's talk about subscribers.")

subs = int(input('How many subscribers do you have?')) #User enters number of subscribers
sub_video = []
for i in range(subs):
    sub_video.append(random.choice(videos)) #assigns each subscriber a random video from the titles list


total_min = 0    
for i in sub_video:
    total_min += lengths[i] #calculation of total minutes
print('The total time spent watching was', total_min, 'minutes.')

sub_video_no_dup = []
for i in sub_video: #code to eliminate any duplicates from showing
    if i not in sub_video_no_dup:
        sub_video_no_dup.append(i)
print('The videos watched by your subscribers were:', sub_video_no_dup)

# Part 4 - Let's compare our channel to our competitor!
print("Part 4 - Let's compare our channel to our competitor!")
comp_subs = random.randrange(1, 101) #random generation of subscribers from 1-100
print('Your competitor has', comp_subs, 'subscribers.')
comp_total_min = 0
for i in range(comp_subs): #calculation of length per video per subscriber
    minutes = random.randrange(1, 6)
    comp_total_min  += minutes
print('Your competitor had', comp_total_min, 'minutes of watch time')

if total_min > comp_total_min: #comparison of minutes watched
    print('Your channel had more watch time!')
elif total_min < comp_total_min:
    print('Your competitor had more watch time.')
elif total_min == comp_total_min:
    print('You and your competitor had the same amount of watch time')

print('Your watch time was', total_min, 'minutes.') #printing out each watch time to verify comparison
print('Your competitors watch time was', comp_total_min, 'minutes.')

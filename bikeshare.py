import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name= ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\n What is the name you want to analyze ? (Hint: input for city (chicago, new york city, washington) \n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("city not found! ,Please input either chicago, new york city or washington.\n")
         

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\n What is the name if the month you want to filter ? (Hint: Input either 'all' to apply no month filter or january, february, ... , june)")
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
        else:
            print("month not found! ,Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\n What is the name if the day you want to filter? (Hint: Input either 'all' to apply no day filter or monday, tuesday, ... sunday)\n)")
        if day_name.lower() in DAY_DATA:
            day =  day_name.lower()
        else:
            print("day not found! , Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df ['Start Time'].dt.month
    df['day_of_week'] = df ['Start Time'].dt.weekday_name
    df['hour'] = df ['Start Time'].dt.hour
    
    #month filter
    if month != 'all' :
        month = MONTH_DATA.index(month)
        
        df = df.loc[df['month']==month]
    
    #day filter
    if day != 'all' :
        df = df.loc[df['day_of_week'] == day.title()]
        
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month  is: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day is :" + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :" + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("most commonly used start station is : " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("  most commonly used end station is : " + common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is :  " +  str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is :" + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types is : \n " + str(user_types) )

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The counts of gender is : \n" + str(gender))
        

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_bitth = df['Birth Year'].min()
        print("The earliest birth is : " + str(earliest_bitth) + "\n")
        
        most_recent_bitth = df['Birth Year'].max()
        print("The most recent birth is : " + str(most_recent_bitth) + "\n")
        
        
        most_common_bitth = df['Birth Year'].mode()[0]
        print("The most common birth is : " + str(most_common_bitth) + "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def view (df):
    ''' show the data that user request  '''
    print(df.head())
    i = 0
    while True :
        display_request = input("do you want to view next five raw ? Enter Yes or No .\n")
        if display_request.lower() != 'yes' :
            return
        i += 5
        print(df.iloc[i : i + 5])

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        while True :
            display_request = input("do you want to view next five raw ? Enter Yes or No .\n")
            if display_request.lower() != 'yes':
                break
            
            view(df)
            break
            
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
